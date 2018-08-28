from django.http import JsonResponse, HttpResponse
import os, sys
import json, requests
import base64
from time import sleep
# -*- coding:utf-8 -*-
import io
import sys
from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
import time
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import datetime
import json, requests
import urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

def linshi(request):
    data_list = []
    # for name in ['客户ID230', '客户ID34', '🌻李汉杰👵', '🌿张聪', '卢俊义', '公孙胜', '秦明', '假如', '关胜', '过客❤', 'ju do it',
    #              '西门庆豪|董庆豪|合众', '梦忆🍁', '吴用', '青春不散场@',
    #              '诸葛营销', '武松', '刘鹏', '林敏', '张清', '柴进', '李应', '花荣', '硕子😁 🏀', '胡蓉', '夏宏伟：品牌良医', '许艳', '贺～丹', '余宏亮']:
    objs = models.zhugedanao_userprofile.objects.all()
    for obj in objs:
        encodestr = base64.b64encode(obj.username.encode('utf-8'))
        encode_username = str(encodestr, encoding='utf-8')
        obj.username = encode_username
        obj.save()
    #     decode_username = base64.b64decode(obj.username)
    #     username = str(decode_username, 'utf-8')
    #     data_list.append(username)
    # print(data_list)
    return HttpResponse(','.join(data_list))
