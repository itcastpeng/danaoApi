from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
import time
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import datetime

response = Response.ResponseObj()

# 连接提交 判断链接提交 当前时间大于创建时间+30分钟 celery定时更新
@csrf_exempt
def panduan_shijian(request):
    q = Q()
    next_datetime_addoneday = (datetime.datetime.now() - datetime.timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S')
    q.add(Q(create_date__lte=next_datetime_addoneday), Q.AND)
    objs = models.zhugedanao_lianjie_task_list.objects.filter(q)
    for obj in objs:
        obj.is_update = 1
    response.code = 200
    response.data = {}
    return JsonResponse(response.__dict__)

"""每个接口 都要判断是否还有任务 方便celery调度 节约资源"""

# 链接提交 判断是否还有任务
@csrf_exempt
def decideIsTask(request):
    q = Q()
    next_datetime_addoneday = (datetime.datetime.now() - datetime.timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S')
    q.add(Q(create_date__lte=next_datetime_addoneday) & Q(count__lt=3), Q.AND)
    objs = models.zhugedanao_lianjie_tijiao.objects.filter(q).filter(is_zhixing=0)[0:1]
    flag = False
    if objs:
        flag = True
    response.code = 200
    response.msg = '查询成功'
    response.data = {'flag': flag}
    return JsonResponse(response.__dict__)

# 链接提交 api
@csrf_exempt
def set_task_access(request):
    now_time_stamp = int(time.time())
    next_datetime_addoneday = (datetime.datetime.now() - datetime.timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S')
    time_stampadd600 = now_time_stamp + 600
    now_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    q = Q()
    q.add(Q(create_date__lte=next_datetime_addoneday) & Q(count__lt=3), Q.AND)
    q.add(Q(time_stamp__isnull=True) | Q(time_stamp__lte=now_time_stamp), Q.AND)
    print('q------> ', q)
    objs = models.zhugedanao_lianjie_tijiao.objects.filter(is_zhixing=0).filter(q)[0:1]
    if objs:
        obj = objs[0]
        obj.submit_date = now_date
        obj.time_stamp = time_stampadd600
        obj.save()
        response.data = {
            'tid': obj.id,
            'url': obj.url
        }
        response.msg = '查询成功'
    else:
        response.data = {}
        response.msg = '无任务'
    response.code = 200
    return JsonResponse(response.__dict__)

# 连接提交 获取id 更改状态
@csrf_exempt
def get_task_for(request):
    if request.method == 'POST':
        now_date =  datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        o_id = request.POST.get('o_id')
        urlId = request.POST.get('urlId')
        ip_addr = request.POST.get('ip_addr')
        address = request.POST.get('address')
        print('urlId----> ',o_id, urlId, ip_addr, address)
        if urlId:
            models.zhugedanao_lianjie_tijiao_log.objects.create(
                zhugedanao_lianjie_tijiao_id=urlId,
                ip=ip_addr,
                address=address,
                create_date=now_date,
            )
            log_count = models.zhugedanao_lianjie_tijiao_log.objects.filter(zhugedanao_lianjie_tijiao_id=urlId).count()
            if log_count:
                objs = models.zhugedanao_lianjie_tijiao.objects.filter(id=urlId)
                if objs:
                    tid=objs[0].tid.id
                    count_list = objs.filter(tid=tid).count()
                    zhixing_count = objs.filter(is_zhixing=1).count()
                    jindutiao = 0
                    if zhixing_count:
                        jindutiao = int((zhixing_count / count_list) * 100)
                    print(count_list)
                    task_status = 0
                    if zhixing_count == count_list:
                        task_status = 1
                    objs.update(
                        is_zhixing=1,
                        count=log_count
                    )
                    models.zhugedanao_lianjie_task_list.objects.filter(id=tid).update(
                        task_progress=jindutiao,
                        task_status=task_status
                    )
            response.code = 200
            response.msg = '请求成功'
        else:
            response.code = 303
            response.msg = 'urlid不能为空'
    else:
        response.code = 402
        response.msg = '请求异常'
    return JsonResponse(response.__dict__)



# 链接提交 判断收录是否有任务
@csrf_exempt
def tiJiaoLianJieDecideIsTask(request):
    next_datetime_addoneday = (datetime.datetime.now() - datetime.timedelta(hours=24))
    now_time_stamp = int(time.time())
    time_stamp20 = now_time_stamp + 20
    q = Q()
    print(next_datetime_addoneday)
    # status 收录状态
    q.add(Q(status=1) & Q(is_zhixing=1) & Q(submit_date__lte=next_datetime_addoneday), Q.AND)
    q.add(Q(time_stamp__isnull=True) | Q(time_stamp__lt=now_time_stamp), Q.AND)
    objs = models.zhugedanao_lianjie_tijiao.objects.filter(q)[0:1]
    flag = False
    response.code = 403
    response.msg = '无任务'
    if objs:
        flag = True
        response.code = 200
        response.msg = '查询成功'
    response.data = {'flag':flag}
    return JsonResponse(response.__dict__)

# 链接提交 收录查询
@csrf_exempt
def linksToSubmitShouLu(request):
    now_time_stamp = int(time.time())
    next_datetime_addoneday = (datetime.datetime.now() - datetime.timedelta(hours=24))
    time_stamp20 = now_time_stamp + 20
    q = Q()
    q.add(Q(status=1) & Q(is_zhixing=1) & Q(submit_date__lte=next_datetime_addoneday), Q.AND)
    q.add(Q(time_stamp__isnull=True) | Q(time_stamp__lt=now_time_stamp), Q.AND)
    objs_tijiao = models.zhugedanao_lianjie_tijiao.objects
    objs = objs_tijiao.filter(q)[0:1]
    if objs:
        obj = objs[0]
        count_obj = models.zhugedanao_lianjie_tijiao_log.objects.filter(zhugedanao_lianjie_tijiao_id=objs[0].tid.id).count()
        print('=========> ', objs[0].tid.id, count_obj)
        if count_obj <= 3:
            objs_tijiao.filter(id=obj.id).update(time_stamp=time_stamp20)
            response.data = {
                'o_id':objs[0].id,
                'url':objs[0].url
            }
        response.msg = '查询成功'
        response.code = 200
    else:
        response.code = 403
        response.data = {}
        response.msg = '无任务'
    return JsonResponse(response.__dict__)

# 链接提交 收录查询返回数据
@csrf_exempt
def linksShouLuReturnData(request):
    if request.method == 'POST':
        o_id = request.POST.get('o_id')
        is_shoulu = request.POST.get('shoulu')
        ip_addr = request.POST.get('ip_addr')
        address = request.POST.get('address')
        if is_shoulu and o_id:
            # create_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            # models.zhugedanao_lianjie_tijiao_log.objects.create(
            #     zhugedanao_lianjie_tijiao_id=o_id,
            #     ip=ip_addr,
            #     address=address,
            #     create_date=create_date
            # )

            objs_tijiaolianjie = models.zhugedanao_lianjie_tijiao.objects
            objs = objs_tijiaolianjie.filter(id=o_id)
            if objs:
                tid = objs[0].tid_id  # 列表id
                count_list = models.zhugedanao_lianjie_tijiao_log.objects.filter(zhugedanao_lianjie_tijiao_id=o_id).count()
                # print('返回数据----------> ', o_id, count_list, '是否收录---> ',is_shoulu)
                shoulu_num = objs_tijiaolianjie.filter(tid=tid).filter(status=2).count()
                models.zhugedanao_lianjie_task_list.objects.filter(id=tid).update(shoulu_num=shoulu_num)
                print('count_list=======> ',objs[0].id,  count_list)
                if int(count_list) < 3 and int(is_shoulu) == 3:
                    objs.update(status=1, is_zhixing=0, time_stamp = None)
                elif int(count_list) >= 3 and int(is_shoulu) == 3:
                    objs.update(status=3)
                else:
                    objs.update(
                        status=is_shoulu,
                    )

                response.code = 200
                response.msg = '已完成'
            else:
                response.code = 302
                response.msg = '对应ID不存在'
        else:
            response.code = 303
            response.msg = '参数错误'
    else:
        response.code = 402
        response.msg = '请求异常'
    response.data = {}
    return JsonResponse(response.__dict__)







