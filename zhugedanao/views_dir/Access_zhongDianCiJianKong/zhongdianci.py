from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
import time
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import datetime
import json, requests


response = Response.ResponseObj()

# 立即监控
@csrf_exempt
def zhongDianCiChaXunLiJiJianKong(request):
    id_list = request.GET.get('id_list')
    if id_list:
        id_list = json.loads(id_list)
        for id in id_list:
            print('=============', id )
            # url = 'http://127.0.0.1:8000/zhugedanao/timeToRefreshZhgongDianCi?lijijiankong={}'.format(id)
            url = 'http://api.zhugeyingxiao.com/zhugedanao/timeToRefreshZhgongDianCi?lijijiankong={}'.format(id)
            requests.get(url)
        response.code = 200
        response.msg = '监控成功'
    else:
        response.code = 303
        response.msg = 'ID不能为空'
    return JsonResponse(response.__dict__)

# 定时刷新 更改下一次执行时间
@csrf_exempt
def timeToRefreshZhgongDianCi(request):
    lijijiankong = request.GET.get('lijijiankong')
    start_time = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:59')
    if lijijiankong:
        task_list_objs = models.zhugedanao_zhongdianci_jiankong_taskList.objects.filter(id=lijijiankong)
        models.zhugedanao_zhongdianci_jiankong_taskDetail.objects.filter(tid_id=task_list_objs[0].id).update(is_perform=1)
    else:
        q = Q()
        q.add(Q(tid__task_status=2) | Q(tid__task_status=1), Q.AND)
        objs = models.zhugedanao_zhongdianci_jiankong_taskDetail.objects.filter(q).filter(
            tid__qiyong_status=1,
            tid__next_datetime__lte=start_time,
            is_perform=0
        )[:1]
        if objs:
            task_list_objs = models.zhugedanao_zhongdianci_jiankong_taskList.objects.filter(id=objs[0].tid.id)
            models.zhugedanao_zhongdianci_jiankong_taskDetail.objects.filter(tid_id=objs[0].tid.id).update(is_perform=1)
        else:
            response.code = 403
            response.msg = '无任务'
            response.data = {}
            return JsonResponse(response.__dict__)
    task_list_objs.filter(id=task_list_objs[0].id).update(
        task_status=3,
        is_zhixing=1
    )
    # next_datetime = task_list_objs[0].next_datetime
    # now_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # now_datetime = datetime.datetime.strptime(now_date, '%Y-%m-%d %H:%M:%S')
    # if next_datetime <= now_datetime:
    #     next_datetime_addoneday = (now_datetime + datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
    #     task_list_objs.update(next_datetime=next_datetime_addoneday)
    response.data = {}
    response.code = 200
    response.msg = '改值成功'

    return JsonResponse(response.__dict__)

# 判断是否有任务
@csrf_exempt
def zhongDianCiChaXunDecideIsTask(request):
    start_time = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:59')
    objs = models.zhugedanao_zhongdianci_jiankong_taskDetail.objects.filter(
        tid__task_status=3,
        tid__qiyong_status=1,
        tid__next_datetime__lte=start_time,
        is_perform=1
    )[:1]
    flag = False
    if objs:
        flag = True
    canshu = '无任务'
    response.code = 403
    response.data = {}
    if flag:
        canshu = '有任务'
        response.code = 200
        response.data = {'flag':flag}
    response.msg = '{}'.format(canshu)
    return JsonResponse(response.__dict__)

 # 获取任务
@csrf_exempt
def HuoQuRenWuzhongDianCi(request):
    now = int(time.time())
    q = Q()
    q.add(Q(is_perform=1) & Q(tid__task_status=3) & Q(tid__qiyong_status=1), Q.AND)
    q.add(Q(time_stamp__isnull=True) | Q(time_stamp__lte=now), Q.AND)
    objs = models.zhugedanao_zhongdianci_jiankong_taskDetail.objects.filter(q)[:1]
    if objs:
        now_datetime = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        time_stamp = int(time.time()) + 30
        models.zhugedanao_zhongdianci_jiankong_taskDetail.objects.filter(id=objs[0].id).update(
            time_stamp=time_stamp,
            task_start_time=now_datetime
        )
        response.code = 200
        response.msg = '查询成功'
        response.data = {
            'lianjie':objs[0].lianjie,
            'detail_id':objs[0].id,
            'search_engine':objs[0].search_engine,
            'keywords':objs[0].keyword,
            'mohupipei':objs[0].mohupipei
        }
    else:
        response.code = 403
        response.msg = '无任务'
        response.data = {}
    return JsonResponse(response.__dict__)

 # 返回任务
@csrf_exempt
def TiJiaoRenWuzhongDianCi(request):
    if request.method == 'POST':
        tid = request.POST.get('tid')
        resultObj = request.POST.get('resultObj')
        judge = request.POST.get('judge')
        json_data = json.loads(resultObj)
        now_data = datetime.date.today().strftime('%Y-%m-%d')
        paiming = 0
        if json_data['order']:
            paiming = json_data['order']
        shoulu = 0
        if json_data['shoulu']:
            shoulu = json_data['shoulu']
        if judge == 'shoulu':
            objs = models.zhugedanao_zhongdianci_jiankong_taskDetailData.objects.create(
                tid_id=tid,
                create_time=now_data,
                paiming=paiming,
                is_shoulu=shoulu,
            )
        else:
            print('=========================')
            paiming = str(','.join(map(str, json_data)))
            print(paiming, type(paiming))
            objs = models.zhugedanao_zhongdianci_jiankong_taskDetailData.objects.create(
                tid_id=tid,
                create_time=now_data,
                paiming=paiming,
            )
        task_list_objs = models.zhugedanao_zhongdianci_jiankong_taskList.objects.filter(id=tid)
        if task_list_objs:
            next_datetime = task_list_objs[0].next_datetime
            now_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            now_datetime = datetime.datetime.strptime(now_date, '%Y-%m-%d %H:%M:%S')
            if next_datetime <= now_datetime:
                next_datetime_addoneday = (now_datetime + datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
                task_list_objs.update(next_datetime=next_datetime_addoneday)
        models.zhugedanao_zhongdianci_jiankong_taskDetail.objects.filter(id=tid).update(
            is_perform=0
        )
        # detail_objs_count = objs.zhugedanao_zhongdianci_jiankong_taskdetail_set.filter(
        #     tid_id=objs.id,
        # )
        # detail_count = detail_objs_count.filter(is_perform=1).count()
        # baifenbi = 0
        # if detail_count:
        #     baifenbi = int((detail_count / detail_objs_count.count()) * 100)
        # models.zhugedanao_zhongdianci_jiankong_taskList.objects.filter(id=tid).update(
        #     task_status=1,
        #     is_zhixing=0
        # )
        response.code = 200
        response.msg = '已完成'
    else:
        response.code = ''
        response.msg = ''
        response.data = {}

    return JsonResponse(response.__dict__)























# start_time = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:59')
# print('start_time=-----> ', start_time)
# q = Q()
# q.add(Q(qiyong_status=1) & Q(next_datetime__lte=start_time), Q.AND)
# objs = models.zhugedanao_zhongdianci_jiankong_taskList.objects.filter(q)[:1]
# if objs:
#     task_id = objs[0].id
#     detail_objs = models.zhugedanao_zhongdianci_jiankong_taskDetail.objects.filter(
#         tid_id=task_id
#     )
#     if detail_objs:
#         task_list_objs = models.zhugedanao_zhongdianci_jiankong_taskList.objects.filter(id=task_id)
#         task_list_objs.update(
#             task_status=3,
#             is_zhixing=1
#         )
#         next_datetime = objs[0].next_datetime
#         now_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         now_datetime = datetime.datetime.strptime(now_date, '%Y-%m-%d %H:%M:%S')
#         if next_datetime <= now_datetime:
#             next_datetime_addoneday = (next_datetime + datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
#             task_list_objs.update(next_datetime=next_datetime_addoneday)
#
#         detail_objs.filter(tid=task_id).update(is_perform=1, task_start_time=start_time)
#     else:
#         models.zhugedanao_zhongdianci_jiankong_taskList.objects.filter(id=task_id).update(
#             qiyong_status=0
#         )
# response.code = 200
# return JsonResponse(response.__dict__)