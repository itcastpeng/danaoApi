from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
import time
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import datetime


response = Response.ResponseObj()
# 收录查询 判断是否有任务
@csrf_exempt
def shouLuChaXunDecideIsTask(request):
    now_time = int(time.time())
    q = Q()
    q.add(Q(is_zhixing=0), Q.AND)
    q.add(Q(time_stamp__isnull=True) | Q(time_stamp__lte=now_time), Q.AND)
    objs = models.zhugedanao_shoulu_chaxun.objects.filter(q)[0:1]
    flag = False
    response.code = 403
    response.msg = '无任务'
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
    q.add(Q(time_stamp__isnull=True) | Q(time_stamp__lte=now_time), Q.AND)
    objs = models.zhugedanao_shoulu_chaxun.objects.filter(q)[0:1]
    if objs:
        objs[0].time_stamp = time_stamp20
        objs[0].save()
        response.data = {
            'o_id':objs[0].id,
            'url':objs[0].url,
            'search':objs[0].search,
        }
        response.msg = '查询成功'
    else:
        response.code = 403
        response.data = {}
        response.msg = '无任务'
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
        shoulu = 2
        if int(is_shoulu) == 1:
            shoulu = 1
        models.zhugedanao_shoulu_chaxun.objects.filter(id=o_id).update(
            title=title,
            is_shoulu=shoulu,
            kuaizhao_time=kuaizhao_time,
            status_code=status_code,
            is_zhixing = 1,
        )
        response.code = 200
        response.msg = '完成'

    else:
        response.code = 402
        response.msg = '请求异常'
    response.data = {}
    return JsonResponse(response.__dict__)
