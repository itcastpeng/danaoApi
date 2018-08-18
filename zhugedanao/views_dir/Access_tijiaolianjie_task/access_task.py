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
    q.add(Q(create_date__lte=next_datetime_addoneday), Q.AND)
    objs = models.zhugedanao_lianjie_tijiao.objects.filter(q).filter(is_zhixing=0)
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
    q.add(Q(create_date__lte=next_datetime_addoneday), Q.AND)
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
    else:
        response.data = {}
    response.code = 200
    response.msg = '查询成功'
    return JsonResponse(response.__dict__)

# 连接提交 获取id 更改状态
@csrf_exempt
def get_task_for(request):
    now_date =  datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    urlId = request.GET.get('urlId')
    ip_addr= request.GET.get('ip_addr')
    address= request.GET.get('address')
    print('urlId----> ', urlId, ip_addr, address)
    objs = models.zhugedanao_lianjie_tijiao.objects.filter(id=urlId)
    if objs:
        objs.update(
            is_zhixing=1
        )
        models.zhugedanao_lianjie_tijiao_log.objects.create(
            zhugedanao_lianjie_tijiao_id=objs[0].id,
            ip=ip_addr,
            address=address,
            create_date=now_date,
        )
    response.code = 200
    response.msg = '请求成功'
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
    objs = models.zhugedanao_lianjie_tijiao.objects.filter(q)
    print('objs---> ', objs)
    flag = False
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
    q.add(Q(status=1) & Q(is_zhixing=1) & Q(submit_date__lte=next_datetime_addoneday) & Q(status=1), Q.AND)
    q.add(Q(time_stamp__isnull=True) | Q(time_stamp__lt=now_time_stamp), Q.AND)
    objs = models.zhugedanao_lianjie_tijiao.objects.filter(q)[0:1]
    print('objs---> ',objs)
    if objs:
        obj = objs[0]
        count_obj = models.zhugedanao_lianjie_tijiao_log.objects.filter(zhugedanao_lianjie_tijiao_id=obj.id).count()
        if count_obj < 3:
            obj.time_stamp = time_stamp20
            obj.save()
            response.data = {
                'o_id':obj.id,
                'url':obj.url
            }
        else:
            obj.status = 2
            obj.save()
        response.msg = '查询成功'
    else:
        response.data = {}
        response.msg = '无任务'
    response.code = 200
    return JsonResponse(response.__dict__)

# 链接提交 收录查询返回数据
@csrf_exempt
def linksShouLuReturnData(request):
    if request.method == 'POST':
        o_id = request.POST.get('o_id')
        is_shoulu = request.POST.get('shoulu')
        if is_shoulu and o_id:
            models.zhugedanao_lianjie_tijiao.objects.filter(id=o_id).update(
                status=is_shoulu
            )
        response.code = 200
        response.msg = '已完成'
    else:
        response.code = 401
        response.msg = '请求异常'
    response.data = {}
    return JsonResponse(response.__dict__)



# 收录查询 判断是否有任务
@csrf_exempt
def shouLuChaXunDecideIsTask(request):
    now_time = int(time.time())
    time_stamp20 = now_time + 20
    q = Q()
    q.add(Q(is_zhixing=0), Q.AND)
    q.add(Q(time_stamp__isnull=True) | Q(time_stamp__lte=time_stamp20), Q.AND)
    objs = models.zhugedanao_shoulu_chaxun.objects.filter(q)[0:1]
    flag = False
    if objs:
        flag = True
    response.code = 200
    response.msg = '查询成功'
    response.data = {'flag':flag}
    return JsonResponse(response.__dict__)

# 收录查询 查询收录获取任务
@csrf_exempt
def shouluHuoQuRenWu(request):
    now_time = int(time.time())
    time_stamp20 = now_time + 20
    q = Q()
    q.add(Q(is_zhixing=0), Q.AND)
    q.add(Q(time_stamp__isnull=True) | Q(time_stamp__lte=time_stamp20), Q.AND)
    objs = models.zhugedanao_shoulu_chaxun.objects.filter(q)[0:1]
    if objs:
        objs[0].time_stamp = time_stamp20
        objs[0].save()
        response.data = {
            'o_id':objs[0].id,
            'url':objs[0].url,
            'search':objs[0].search,
        }
    else:
        response.data = {}
    response.code = 200
    return JsonResponse(response.__dict__)

# 收录查询 查询完收录 返回数据
@csrf_exempt
def shouluTiJiaoRenWu(request):
    if request.method == 'POST':
        o_id = request.POST.get('o_id')
        title = request.POST.get('title')
        kuaizhao_time = request.POST.get('kuaizhao_time')
        status_code = request.POST.get('status_code')
        is_shoulu = request.POST.get('is_shoulu')
        print('-----------', o_id, title, kuaizhao_time, status_code, is_shoulu)
        models.zhugedanao_shoulu_chaxun.objects.filter(id=o_id).update(
            title=title,
            is_shoulu=is_shoulu,
            kuaizhao_time=kuaizhao_time,
            status_code=status_code,
            is_zhixing = 1,
        )
        response.code = 200
        response.msg = '完成'
        response.data = {}
        return JsonResponse(response.__dict__)



