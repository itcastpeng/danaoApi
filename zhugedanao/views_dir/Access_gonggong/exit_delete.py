from django.http import JsonResponse
from zhugedanao import models
from publicFunc import Response
import requests
from django.views.decorators.csrf import csrf_exempt, csrf_protect
response = Response.ResponseObj()
from publicFunc import account
import redis

redis_rc = redis.Redis(host='redis://redis_host', port=6379, db=4, decode_responses=True)
# redis_rc = redis.Redis(host='192.168.100.20', port=6379, db=4, decode_responses=True)

@csrf_exempt
@account.is_token(models.zhugedanao_userprofile)
def gonggong_exit_delete(request):
    user_id = request.GET.get('user_id')
    timestamp = request.GET.get('timestamp')
    rand_str = request.GET.get('rand_str')
    # 关闭网页 删除收录查询
    delete_shoulu_url = 'http://api.zhugeyingxiao.com/zhugedanao/shouLuChaxun/clickReturn/0?timestamp={timestamp}&rand_str={rand_str}&user_id={user_id}'.format(
    # delete_shoulu_url = 'http://127.0.0.1:8000/zhugedanao/shouLuChaxun/clickReturn/0?timestamp={timestamp}&rand_str={rand_str}&user_id={user_id}'.format(
        rand_str=rand_str,
        timestamp=timestamp,
        user_id=user_id)
    ret = requests.get(delete_shoulu_url)
    shoulu_delete = ret.status_code

    # 关闭网页 删除覆盖查询
    delete_fugai_url = 'http://api.zhugeyingxiao.com/zhugedanao/fuGaiChaXun/clickReturn/0?timestamp={timestamp}&rand_str={rand_str}&user_id={user_id}'.format(
    # delete_fugai_url = 'http://127.0.0.1:8000/zhugedanao/fuGaiChaXun/clickReturn/0?timestamp={timestamp}&rand_str={rand_str}&user_id={user_id}'.format(
        rand_str=rand_str,
        timestamp=timestamp,
        user_id=user_id)
    ret = requests.get(delete_fugai_url)
    fugai_delete = ret.status_code

    # 关闭网页 删除平台挖掘
    delete_pingtaiwajue = 'http://api.zhugeyingxiao.com/zhugedanao/pingTaiWaJue/clickReturn/0?timestamp={timestamp}&rand_str={rand_str}&user_id={user_id}'.format(
        # delete_fugai_url = 'http://127.0.0.1:8000/zhugedanao/pingTaiWaJue/clickReturn/0?timestamp={timestamp}&rand_str={rand_str}&user_id={user_id}'.format(
        rand_str=rand_str,
        timestamp=timestamp,
        user_id=user_id)
    ret = requests.get(delete_pingtaiwajue)
    pingtaiwajue_delete = ret.status_code

    if shoulu_delete and fugai_delete and pingtaiwajue_delete == 200:
        redis_rc.delete('danao_shoulu_chongfu')
        redis_rc.delete('danao_fugai_chongfu')
        redis_rc.delete('danao_pingtaiwajue_chongfu')
        redis_rc.delete('danao_baiduxiala_chongfu')
        response.code = 200
        response.msg = '退出成功'
    else:
        response.msg = '退出异常'
    return JsonResponse(response.__dict__)

