
from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse, HttpResponse
import time
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import datetime
import json, requests
import base64

def linshi(request):
    data_list = []
    for name in ['客户ID230', '客户ID34', '🌻李汉杰👵', '🌿张聪', '卢俊义', '公孙胜', '秦明', '假如', '关胜', '过客❤', 'ju do it',
                 '西门庆豪|董庆豪|合众', '梦忆🍁', '吴用', '青春不散场@',
                 '诸葛营销', '武松', '刘鹏', '林敏', '张清', '柴进', '李应', '花荣', '硕子😁 🏀', '胡蓉', '夏宏伟：品牌良医', '许艳', '贺～丹', '余宏亮']:
        encodestr = base64.b64encode(name.encode('utf-8'))
        encode_username = str(encodestr, encoding='utf-8')
        decode_username = base64.b64decode(encode_username)
        username = str(decode_username, encoding='utf-8')
        data_list.append(json.dumps(username))

    return HttpResponse(data_list)





