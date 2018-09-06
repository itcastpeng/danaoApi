from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
import time
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt, csrf_protect

response = Response.ResponseObj()
# 关键词排名查询 判断是否有任务
@csrf_exempt
def guanJianCiPaiMingDecideIsTask(request):
    now_time = int(time.time())
    q = Q()
    q.add(Q(is_perform=0), Q.AND)
    q.add(Q(time_stamp__isnull=True) | Q(time_stamp__lte=now_time), Q.AND)
    objs = models.zhugedanao_guanjianci_paiming_chaxun.objects.filter(q)[0:1]
    flag = False
    response.code = 403
    response.msg = '无任务'
    if objs:
        flag = True
        response.code = 200
        response.msg = '查询成功'
    response.data = {'flag':flag}
    return JsonResponse(response.__dict__)

# 关键词排名查询任务
@csrf_exempt
def guanJianCiPaiMingHuoQuRenWu(request):
    now_time = int(time.time())
    time_stamp10 = now_time + 10
    q = Q()
    q.add(Q(is_perform=0), Q.AND)
    q.add(Q(time_stamp__isnull=True) | Q(time_stamp__lte=now_time), Q.AND)
    objs = models.zhugedanao_guanjianci_paiming_chaxun.objects.filter(q).order_by('?')[0:1]
    if objs:
        objs[0].time_stamp = time_stamp10
        objs[0].save()
        response.data = {
            'o_id':objs[0].id,
            'keyword':objs[0].keyword,
            'search':objs[0].search_engine,
            'lianjie':objs[0].lianjie
        }
        response.code = 200
        response.msg = '查询成功'
    else:
        response.code = 403
        response.data = {}
        response.msg = '无任务'
    return JsonResponse(response.__dict__)

# 关键词排名查询 查询完收录 返回数据
@csrf_exempt
def guanJianCiPaiMingTiJiaoRenWu(request):
    if request.method == 'POST':
        o_id = request.POST.get('o_id')
        paiming = request.POST.get('paiming')
        if o_id:
            models.zhugedanao_guanjianci_paiming_chaxun.objects.filter(id=o_id).update(
                is_perform=1,
                paiming=paiming
            )
        response.code = 200
        response.msg = '完成'

    else:
        response.code = 402
        response.msg = '请求异常'
    response.data = {}
    return JsonResponse(response.__dict__)
