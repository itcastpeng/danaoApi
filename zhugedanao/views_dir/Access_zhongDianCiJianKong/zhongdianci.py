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

@csrf_exempt
def zhongDianCiChaXunLiJiJianKong(request):
    id_list = request.GET.get('id_list')
    if id_list:
        for id in id_list.split(','):
            print(id)
            url = 'http://127.0.0.1:8000/zhugedanao/zhongDianCiChaXunDecideIsTask?lijijiankong={}'.format(id)
            # url = 'http://api.zhugeyingxiao.com/zhugedanao/zhongDianCiChaXunDecideIsTask?lijijiankong={}'.format(id)
            requests.get(url)
    response.code = 200
    return JsonResponse(response.__dict__)

@csrf_exempt
def zhongDianCiChaXunDecideIsTask(request):
    lijijiankong = request.GET.get('lijijiankong')
    start_time = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:59')
    q = Q()
    q.add(Q(qiyong_status=1) & Q(next_datetime__lte=start_time), Q.AND)
    objs = models.zhugedanao_zhongdianci_jiankong_taskList.objects.filter(q)[:1]
    if lijijiankong:
        objs = models.zhugedanao_zhongdianci_jiankong_taskList.objects.filter(id=lijijiankong)
    flag = False
    if objs:
        task_id = objs[0].id
        detail_objs = models.zhugedanao_zhongdianci_jiankong_taskDetail.objects.filter(
            tid_id=task_id,
        )
        # 判断是任务列表是否有任务
        if detail_objs:
            task_list_objs = models.zhugedanao_zhongdianci_jiankong_taskList.objects.filter(id=task_id)
            task_list_objs.update(
                task_status=3,
                is_zhixing=1
            )
            next_datetime = objs[0].next_datetime
            now_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            now_datetime = datetime.datetime.strptime(now_date, '%Y-%m-%d %H:%M:%S')
            if next_datetime <= now_datetime:
                next_datetime_addoneday = (now_datetime + datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
                task_list_objs.update(next_datetime=next_datetime_addoneday)
            detail_objs.filter(tid=task_id).update(is_perform=1)
            flag = True
        # 任务列表没有数据任务列表改为 未启用
        else:
            models.zhugedanao_zhongdianci_jiankong_taskList.objects.filter(id=task_id).update(
                qiyong_status=0
            )
    canshu = '无任务'
    response.code = 403
    response.data = {}
    if flag:
        canshu = '有任务'
        response.code = 200
        response.data = {'flag':flag}
    response.msg = '{}'.format(canshu)
    return JsonResponse(response.__dict__)


@csrf_exempt
def HuoQuRenWuzhongDianCi(request):
    now = int(time.time())
    q = Q()
    q.add(Q(is_perform=1), Q.AND)
    q.add(Q(time_stamp__isnull=True) | Q(time_stamp__lte=now), Q.AND)
    objs = models.zhugedanao_zhongdianci_jiankong_taskDetail.objects.filter(q)[:1]
    if objs:
        now_datetime = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        time_stamp = int(time.time()) + 300
        models.zhugedanao_zhongdianci_jiankong_taskDetail.objects.filter(id=objs[0].id).update(
            time_stamp=time_stamp,
            task_start_time=now_datetime
        )
        response.code = 200
        response.msg = '查询成功'
        response.data = {
            'tid':objs[0].id,
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

@csrf_exempt
def TiJiaoRenWuzhongDianCi(request):
    if request.method == 'POST':
        tid = request.POST.get('tid')
        resultObj = request.POST.get('resultObj')
        judge = request.POST.get('judge')
        json_data = json.loads(resultObj)
        now_data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if judge == 'shoulu':
            models.zhugedanao_zhongdianci_jiankong_taskDetailData.objects.create(
                tid_id=tid,
                create_time=now_data,
                paiming=json_data['order'],
                is_shoulu=json_data['shoulu']
            )
        else:
            paiming = str(','.join(map(str, json_data)))
            print(paiming, type(paiming))
            models.zhugedanao_zhongdianci_jiankong_taskDetailData.objects.create(
                tid_id=tid,
                create_time=now_data,
                paiming=paiming,
            )
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