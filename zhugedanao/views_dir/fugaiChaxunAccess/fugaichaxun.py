

from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
import time
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import datetime
response = Response.ResponseObj()


# 覆盖查询 判断是否有任务
@csrf_exempt
def fuGaiChaXunDecideIsTask(request):
    now_time = int(time.time())
    time_stamp30 = now_time + 30
    q = Q()
    q.add(Q(is_zhixing=0), Q.AND)
    q.add(Q(time_stamp__isnull=True) | Q(time_stamp__lte=time_stamp30),Q.AND)
    objs = models.zhugedanao_fugai_chaxun.objects.filter(q)
    flag = False
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
    q.add(Q(time_stamp__isnull=True) | Q(time_stamp__lte=time_stamp30), Q.AND)
    objs = models.zhugedanao_fugai_chaxun.objects.filter(q)[0:1]
    if objs:
        objs[0].time_stamp = time_stamp30
        objs[0].save()
        response.data = {
            'o_id':objs[0].id,
            'keyword':objs[0].keyword,
            'search':objs[0].search_engine,

        }


@csrf_exempt
def fuGaiTiJiaoRenWu(request):
    pass
