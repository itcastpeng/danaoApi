from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
import time
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import datetime

response = Response.ResponseObj()


# 判断是否还有任务
def decideIsTask(request):
    objs = models.zhugedanao_lianjie_tijiao.objects.filter(is_zhixing=0)
    flag = False
    if objs:
        flag = True
    response.code = 200
    response.msg = '查询成功'
    response.data = {'flag': flag}
    return JsonResponse(response.__dict__)


# api 返回十条任务
def set_task_access(request):
    data_list = []
    now_time_stamp = int(time.time())
    time_stampadd30 = now_time_stamp + 30
    next_datetime_addoneday = (datetime.datetime.now() - datetime.timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S')
    q = Q()
    q.add(Q(create_date__lte=next_datetime_addoneday), Q.AND)
    q.add(Q(time_stamp__isnull=True) | Q(time_stamp__lte=now_time_stamp), Q.AND)
    print('q------> ', q)
    objs = models.zhugedanao_lianjie_tijiao.objects.filter(is_zhixing=0).filter(q)
    if objs:
        obj = objs[0]
        obj.time_stamp = time_stampadd30
        response.data = {
            'tid': obj.id,
            'url': obj.url
        }

    response.code = 200
    response.msg = '查询成功'
    return JsonResponse(response.__dict__)


# 获取id 更改状态
@csrf_exempt
def get_task_for(request):
    print('请求-')
    urlId = request.POST.get('urlId')
    print('urlId----> ', urlId)
    models.zhugedanao_lianjie_tijiao.objects.filter(id=urlId).update(
        is_zhixing=1,
        status=1
    )
    response.code = 200
    response.msg = '请求成功'
    return JsonResponse(response.__dict__)


# 判断链接提交 当前时间大于创建时间+30分钟
def panduan_shijian(request):
    q = Q()
    next_datetime_addoneday = (datetime.datetime.now() - datetime.timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S')
    q.add(Q(create_date__lte=next_datetime_addoneday), Q.AND)
    objs = models.zhugedanao_lianjie_task_list.objects.filter(q)
    for obj in objs:
        obj.is_update = 1
    response.code = 200
    return JsonResponse(response.__dict__)
