from django.http import JsonResponse
from zhugedanao import models
from publicFunc import Response
import requests
from django.views.decorators.csrf import csrf_exempt, csrf_protect
response = Response.ResponseObj()


def gonggong_exit_delete(request):
    user_id = request.GET.get('user_id')
    timestamp = request.GET.get('timestamp')
    rand_str = request.GET.get('rand_str')
    delete_shoulu_url = 'http://api.zhugeyingxiao.com/zhugedanao/shouLuChaxun/clickReturn/0?timestamp={timestamp}&rand_str={rand_str}&user_id={user_id}'.format(
    # delete_shoulu_url = 'http://127.0.0.1:8000/zhugedanao/shouLuChaxun/clickReturn/0?timestamp={timestamp}&rand_str={rand_str}&user_id={user_id}'.format(
        rand_str=rand_str,
        timestamp=timestamp,
        user_id=user_id)
    ret = requests.get(delete_shoulu_url)
    shoulu_delete = ret.status_code
    delete_fugai_url = 'http://api.zhugeyingxiao.com/zhugedanao/fuGaiChaXun/clickReturn/0?timestamp={timestamp}&rand_str={rand_str}&user_id={user_id}'.format(
    # delete_fugai_url = 'http://127.0.0.1:8000/zhugedanao/fuGaiChaXun/clickReturn/0?timestamp={timestamp}&rand_str={rand_str}&user_id={user_id}'.format(
        rand_str=rand_str,
        timestamp=timestamp,
        user_id=user_id)
    ret = requests.get(delete_fugai_url)
    fugai_delete = ret.status_code
    if shoulu_delete and fugai_delete == 200:
        response.code = 200
        response.msg = '退出成功'
    else:
        response.msg = '退出异常'
    return JsonResponse(response.__dict__)

