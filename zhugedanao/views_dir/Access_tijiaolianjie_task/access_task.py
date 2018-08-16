from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
import time
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt, csrf_protect


response = Response.ResponseObj()

# 判断是否还有任务
def decideIsTask(request):
    objs = models.zhugedanao_lianjie_tijiao.objects.filter(tid__is_update=1).filter(is_zhixing=0)
    flag = False
    if objs:
        flag = True
    response.code = 200
    response.msg = '查询成功'
    response.data = {'flag':flag}
    return JsonResponse(response.__dict__)


# api 返回十条任务
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
            'tid':obj.id,
            'url':obj.url
        })
    response.code = 200
    response.msg = '查询成功'
    response.data = {'data_list':data_list}
    return JsonResponse(response.__dict__)

# 获取id 更改状态
@csrf_exempt
def get_task_for(request):
    print('请求-')
    urlId = request.POST.get('urlId')
    print('urlId----> ',urlId)
    models.zhugedanao_lianjie_tijiao.objects.filter(id=urlId).update(
        is_zhixing=1,
        status=1
    )
    response.code = 200
    response.msg = '请求成功'
    return JsonResponse(response.__dict__)
