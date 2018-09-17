from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from zhugedanao.forms.userManagement import AddForm, SelectForm
from publicFunc.condition_com import conditionCom
import base64, sys, io
from zhugedanao.views_dir.permissions import init_data
from django.db.models import Q

# cerf  token验证 用户展示模块
@csrf_exempt
@account.is_token(models.zhugedanao_userprofile)
def userIntegralShow(request):
    response = Response.ResponseObj()
    if request.method == "GET":
        forms_obj = SelectForm(request.GET)
        if forms_obj.is_valid():
            current_page = forms_obj.cleaned_data['current_page']
            length = forms_obj.cleaned_data['length']
            order = request.GET.get('order', '-create_date')
            role_id = request.GET.get('role_id')
            # encode_username = request.GET.get('username')
            field_dict = {
                'id': '',
                'username': '__contains',
                'create_date': '',
                'role_id': role_id,
            }
            q = conditionCom(request, field_dict)
            print('q----------> ',q)
            objs = models.zhugedanao_userprofile.objects.select_related('role').filter(q).order_by(order)
            obj_count = objs.count()
            # 分页
            if length != 0:
                start_line = (current_page - 1) * length
                stop_line = start_line + length
                objs = objs[start_line: stop_line]
            data_list = []
            for obj in objs:
                role_id = 0
                role_name = ''
                if obj.role:
                    role_name = obj.role.name
                    role_id = obj.role.id
                decode_username = base64.b64decode(obj.username)
                username = str(decode_username, 'utf-8')
                data_list.append({
                    'o_id':obj.id,
                    'username' : username,
                    'level_id':obj.level_name.id,
                    'level' : obj.level_name.name,
                    'create_date' : obj.create_date.strftime('%Y-%m-%d %H:%M:%S'),
                    'role' : role_name,
                    'role_id':role_id
                })
            response.code = 200
            response.msg = '查询成功'
            response.data = {
                'data_list' : data_list,
                'obj_count':obj_count
            }
    return JsonResponse(response.__dict__)


# 用户积分操作
#  csrf  token验证
@csrf_exempt
@account.is_token(models.zhugedanao_userprofile)
def userIntegralOper(request, oper_type, o_id):
    response = Response.ResponseObj()
    user_id = request.GET.get('user_id')
    if request.method == "POST":
        # 调用支付二维码
        if oper_type == 'callTheDrCode':
            print('========================')

        # 添加用户积分
        if oper_type == "addUserIntegral":
            pass



    else:
        response.code = 402
        response.msg = "请求异常"
    return JsonResponse(response.__dict__)















































