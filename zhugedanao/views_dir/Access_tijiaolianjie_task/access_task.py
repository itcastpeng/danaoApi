from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import time
from django.db.models import Q
import json


def task_access(request):
    response = Response.ResponseObj()
    data_list = []
    while True:
        now_time_stamp = int(time.time())
        time_stamp = now_time_stamp + 30
        q = Q(time_stamp__isnull=True | time_stamp < time_stamp)
        objs = models.zhugedanao_lianjie_tijiao.objects.filter(is_zhixing=0).filter(q)[0:10]
        for obj in objs:
            models.zhugedanao_lianjie_tijiao.objects.filter(id=obj.id).update(time_stamp=time_stamp)
            data_list.append({
                'o_id':obj.id,
                'tid':obj.tid.id,
                'url':obj.url
            })

        panduan_objs = models.zhugedanao_lianjie_tijiao.objects.filter(is_zhixing=0)
        if not panduan_objs:
            break

    response.code = 200
    response.msg = '查询成功'
    response.data = {'data_list':data_list}
    return JsonResponse(response.__dict__)
