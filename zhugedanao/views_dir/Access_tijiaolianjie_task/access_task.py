from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
import time
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt, csrf_protect


response = Response.ResponseObj()
@csrf_exempt
@account.is_token(models.zhugedanao_userprofile)
def set_task_access(request):
    data_list = []
    now_time_stamp = int(time.time())
    time_stampadd30 = now_time_stamp + 30
    q = Q()
    q.add(Q(time_stamp__isnull=True) | Q(time_stamp__lt=now_time_stamp), Q.AND)
    objs = models.zhugedanao_lianjie_tijiao.objects.filter(tid__is_update=1).filter(is_zhixing=0).filter(q)[0:10]
    for obj in objs:
        obj.time_stamp = time_stampadd30
        obj.save()
        data_list.append({
            'o_id':obj.id,
            'tid':obj.tid.id,
            'url':obj.url
        })
    response.code = 200
    response.msg = '查询成功'
    response.data = {'data_list':data_list}
    return JsonResponse(response.__dict__)


@csrf_exempt
@account.is_token(models.zhugedanao_userprofile)
def get_task_for(request):
    urlId = request.GET.get('urlId')
    print('urlId----> ',urlId)
    models.zhugedanao_lianjie_tijiao.objects.filter(id=urlId).update(
        is_zhixing=1,
        status=1
    )

    response.code = 200
    response.msg = '请求成功'
    return JsonResponse(response.__dict__)
