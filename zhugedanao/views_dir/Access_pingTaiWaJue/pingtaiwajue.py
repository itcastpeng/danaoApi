

from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
import time
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import datetime
response = Response.ResponseObj()
import json


# 平台挖掘 判断是否有任务
@csrf_exempt
def pingTaiWaJueDecideIsTask(request):
    now_time = int(time.time())
    q = Q()
    q.add(Q(is_perform=0), Q.AND)
    q.add(Q(time_stamp__isnull=True) | Q(time_stamp__lte=now_time),Q.AND)
    objs = models.zhugedanao_pingtaiwajue_keyword.objects.filter(q)
    flag = False
    response.code = 403
    response.msg = '无任务'
    if objs:
        flag = True
        response.code = 200
        response.msg = '查询成功'
    response.data = {'flag':flag}
    return JsonResponse(response.__dict__)

# 获取任务
@csrf_exempt
def pingTaiWaJueHuoQuRenWu(request):
    now_time = int(time.time())
    time_stamp5 = now_time + 5
    q = Q()
    q.add(Q(is_perform=0), Q.AND)
    q.add(Q(time_stamp__isnull=True) | Q(time_stamp__lte=now_time), Q.AND)
    objs = models.zhugedanao_pingtaiwajue_keyword.objects.filter(q)[0:1]
    if objs:
        objs[0].time_stamp = time_stamp5
        objs[0].save()
        response.code = 200
        response.msg = '查询成功'
        response.data = {
            'task_keywords':objs[0].keyword,
            'task_id':objs[0].id,
            'task_type':objs[0].search,
            'task_page':objs[0].page_number
        }
    else:
        response.code = 403
        response.msg = '无任务'
        response.data = {}
    return JsonResponse(response.__dict__)

# 返回结果
@csrf_exempt
def pingTaiWaJueTiJiaoRenWu(request):
    if request.method == 'POST':
        print('request.POST--------> ',request.POST)
        task_id = request.POST.get('task_id')
        data = request.POST.get('data')
        if task_id:
            models.zhugedanao_pingtaiwajue_keyword.objects.filter(id=task_id).update(
                is_perform = 1
            )
            print('task_id--> ',task_id)
            print('data=-==========> ', data, type(data))
            jsonData = json.loads(data)
            querysetlist = []
            for yuming, index in jsonData.items():
                if '\\' in yuming:
                    yuming = yuming.split('\\')[0]
                create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                querysetlist.append(
                    models.zhugedanao_pingtaiwajue_yuming(
                        create_time = create_time,
                        tid_id = task_id,
                        yuming = yuming,
                        number = index
                ))
            models.zhugedanao_pingtaiwajue_yuming.objects.bulk_create(querysetlist)
            response.code = 200
            response.msg = '完成'
        else:
            response.code = 303
            response.msg = '参数错误'
    else:
        response.code = 403
        response.msg = '请求异常'
    response.data = {}
    return JsonResponse(response.__dict__)














