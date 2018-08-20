

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

# 覆盖查询 判断是否有任务
@csrf_exempt
def fuGaiChaXunDecideIsTask(request):
    now_time = int(time.time())
    q = Q()
    q.add(Q(is_zhixing=0), Q.AND)
    q.add(Q(time_stamp__isnull=True) | Q(time_stamp__lte=now_time),Q.AND)
    objs = models.zhugedanao_fugai_chaxun.objects.filter(q)
    flag = False
    response.code = 403
    response.msg = '无任务'
    if objs:
        flag = True
        response.code = 200
        response.msg = '查询成功'
    response.data = {'flag':flag}
    return JsonResponse(response.__dict__)


@csrf_exempt
def fuGaiHuoQuRenWu(request):
    now_time = int(time.time())
    time_stamp30 = now_time + 30
    q = Q()
    q.add(Q(is_zhixing=0), Q.AND)
    q.add(Q(time_stamp__isnull=True) | Q(time_stamp__lte=now_time), Q.AND)
    objs = models.zhugedanao_fugai_chaxun.objects.filter(q)[0:1]
    if objs:
        objs[0].time_stamp = time_stamp30
        objs[0].save()
        response.code = 200
        response.msg = '查询成功'
        response.data = {
            'o_id':objs[0].id,
            'keyword':objs[0].keyword,
            'search':objs[0].search_engine,
            'tiaojian':objs[0].sousuo_guize
        }
    else:
        response.code = 403
        response.msg = '无任务'
        response.data = {}
    return JsonResponse(response.__dict__)

@csrf_exempt
def fuGaiTiJiaoRenWu(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        keyword = request.POST.get('keyword')
        o_id = request.POST.get('o_id')
        resultObj = request.POST.get('resultObj')
        if resultObj and o_id and keyword and search:
            json_detail_data = []
            order_list = []
            for result in eval(resultObj):
                order_list.append(result['paiming'])
                zhanwei = 0
                if result['paiming']:
                    zhanwei = 1
                json_detail_data.append({
                    'rank': result['paiming'],
                    'title': result['title'].replace('\'', '').replace('"', ''),
                    'url': result['title_url'],
                    'guize': result['sousuo_guize'],
                    'keyword': keyword,
                    'zhanwei': zhanwei,
                    'search_engine':search
                })
            str_order = '0'
            if order_list:
                str_order = ','.join(str(i) for i in set(order_list))
            models.zhugedanao_fugai_chaxun.objects.filter(id=o_id).update(
                is_zhixing=1,
                paiming_detail=str_order,
                json_detail_data=json_detail_data,
            )
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














