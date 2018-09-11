from openpyxl.styles import Font, Alignment
from openpyxl import Workbook
import os, time
from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from zhugedanao.forms.pingtai_wajue import AddForm, SelectForm

# cerf  token验证 用户展示模块
@csrf_exempt
@account.is_token(models.zhugedanao_userprofile)
def userManagementShow(request):
    response = Response.ResponseObj()
    if request.method == "GET":
        forms_obj = SelectForm(request.GET)
        if forms_obj.is_valid():
            current_page = forms_obj.cleaned_data['current_page']
            length = forms_obj.cleaned_data['length']
            objs = models.zhugedanao_userprofile.objects.all()
            obj_count = objs.count()
            # 分页
            if length != 0:
                start_line = (current_page - 1) * length
                stop_line = start_line + length
                objs = objs[start_line: stop_line]
            data_list = []
            for obj in objs:
                data_list.append({
                    'username' : obj.username,
                    'level' : obj.level_name,
                    'create_date' : obj.create_date,
                    'role' : obj.role
                })
            response.code = 200
            response.msg = '查询成功'
            response.data = {'data_list' : data_list}
    return JsonResponse(response.__dict__)



#  增删改
#  csrf  token验证
@csrf_exempt
@account.is_token(models.zhugedanao_userprofile)
def userManagementOper(request, oper_type, o_id):
    response = Response.ResponseObj()
    user_id = request.GET.get('user_id')
    if request.method == "POST":

        # 修改前数据
        if oper_type == "beforeUpdate":
            objs = models.zhugedanao_userprofile.objects.filter(id=o_id)
            obj = objs[0]
            otherData = {
                'user_level' : obj.level_name,
                'role':obj.role
            }
            response.code = 200
            response.msg = '查询成功'
            response.data = {'otherData':otherData}

        # 确认修改数据
        if oper_type == 'afterUpdate':
            objs = models.zhugedanao_userprofile.objects.filter(id=o_id)
            obj = objs[0]
            role = request.POST.get('role')
            user_level = request.POST.get('user_level')
            obj.role_id = role
            obj.level_name_id = user_level
            obj.save()
            response.code = 200
            response.msg = '修改成功'
            response.data = {}

    else:
        response.code = 402
        response.msg = "请求异常"



    return JsonResponse(response.__dict__)