from openpyxl.styles import Font, Alignment
from openpyxl import Workbook
import os, time
from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import datetime
from zhugedanao.forms.pingtai_wajue import AddForm, SelectForm
import json
import random
from django.db.models import Count,Q, Sum
import threading
import redis

redis_rc = redis.Redis(host='redis_host', port=6379, db=3, decode_responses=True)
# redis_rc = redis.Redis(host='192.168.100.20', port=6379, db=4, decode_responses=True)

# cerf  token验证 用户展示模块
@csrf_exempt
@account.is_token(models.zhugedanao_userprofile)
def pingTaiWaJueShow(request):
    response = Response.ResponseObj()
    user_id = request.GET.get('user_id')
    if request.method == "GET":
        forms_obj = SelectForm(request.GET)
        if forms_obj.is_valid():
            current_page = forms_obj.cleaned_data['current_page']
            length = forms_obj.cleaned_data['length']
            task_objs = models.zhugedanao_pingtaiwajue_keyword.objects.filter(user_id_id=user_id)
            yuming_objs = models.zhugedanao_pingtaiwajue_yuming.objects.filter(tid__user_id=user_id)
            yuming_count = yuming_objs.count()

            task_count = task_objs.count()
            yiwancheng = task_objs.filter(is_perform=1).count()
            query_progress = 0
            if yiwancheng:
                query_progress = int((int(yiwancheng) / int(task_count)) * 100)
            whether_complete = False
            if yiwancheng == task_count:
                whether_complete = True
            pingtaiwajue_chongfu = redis_rc.get('danao_pingtaiwajue_chongfu')
            chongfu = 0
            if pingtaiwajue_chongfu:
                chongfu = pingtaiwajue_chongfu
            # 分页
            if length != 0:
                start_line = (current_page - 1) * length
                stop_line = start_line + length
                objs = yuming_objs[start_line: stop_line]
            data_list = []

            for obj in objs:
                if str(obj.tid.search) == '1':
                    yinqing = '百度'
                elif str(obj.tid.search) == '4':
                    yinqing = '手机百度'
                elif str(obj.tid.search) == '3':
                    yinqing = '360'
                elif str(obj.tid.search) == '6':
                    yinqing = '手机360'
                else:
                    yinqing = ''
                data_list.append({
                    'yuming':obj.yuming,
                    'number':obj.number,
                    'search':yinqing
                })
            response.code = 200
            response.msg = '查询成功'
            response.data = {
                'yuming_count':yuming_count,            # 域名数量
                'data': data_list,                      # 详情
                'objs_count':task_count,                # 总数
                'query_progress':query_progress,        # 进度
                'whether_complete':whether_complete,    # 是否完成
                'yiwancheng_obj':yiwancheng,            # 已完成
                'chongfu_num':int(chongfu)
            }
        else:
            response.code = 402
            response.msg = "请求异常"
            response.data = json.loads(forms_obj.errors.as_json())
    return JsonResponse(response.__dict__)



#  增删改
#  csrf  token验证
@csrf_exempt
@account.is_token(models.zhugedanao_userprofile)
def pingTaiWaJue(request, oper_type, o_id):
    response = Response.ResponseObj()
    user_id = request.GET.get('user_id')
    if request.method == "POST":
        # 增加下拉任务
        if oper_type == "add":
            models.zhugedanao_pingtaiwajue_yuming.objects.filter(tid__user_id_id=user_id).delete()
            models.zhugedanao_pingtaiwajue_keyword.objects.filter(user_id_id=user_id).delete()
            form_data = {
                'search' : request.POST.get('search'),
                'keywords': request.POST.get('keywords'),
                'page_number': request.POST.get('page_number'),
            }
            #  创建 form验证 实例（参数默认转成字典）
            forms_obj = AddForm(form_data)
            if forms_obj.is_valid():
                #  添加数据库
                chongfu = int(len(forms_obj.cleaned_data.get('keywords'))) - int(len(set(forms_obj.cleaned_data.get('keywords'))))
                print('chongfu============>',chongfu)
                redis_rc.set('danao_pingtaiwajue_chongfu', '{}'.format(int(chongfu)), ex=None, px=None, nx=False, xx=False)
                keywords_list = set(forms_obj.cleaned_data.get('keywords'))
                querysetlist = []
                create_time = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                for search in json.loads(form_data['search']):
                    for keyword in keywords_list:
                        querysetlist.append(
                            models.zhugedanao_pingtaiwajue_keyword(
                                user_id_id=user_id,
                                search=search,
                                keyword=keyword,
                                create_time=create_time,
                                page_number=json.loads(form_data['page_number'])
                            )
                        )
                models.zhugedanao_pingtaiwajue_keyword.objects.bulk_create(querysetlist)
                response.code = 200
                response.msg = "添加成功"
                response.data = {}
            else:
                print("验证不通过")
                response.code = 301
                response.msg = json.loads(forms_obj.errors.as_json())
                response.data = {}

    elif request.method == 'GET':
        # 点击返回 删除任务
        if oper_type == 'clickReturn':
            response.code = 200
            response.msg = '退出成功'
            models.zhugedanao_pingtaiwajue_yuming.objects.filter(
                tid__user_id_id=user_id
            ).delete()
            models.zhugedanao_pingtaiwajue_keyword.objects.filter(
                user_id_id=user_id
            ).delete()
            return JsonResponse(response.__dict__)


    else:
        response.code = 402
        response.msg = "请求异常"



    return JsonResponse(response.__dict__)