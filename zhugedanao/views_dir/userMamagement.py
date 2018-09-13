from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from zhugedanao.forms.userManagement import AddForm, SelectForm
from publicFunc.condition_com import conditionCom
import base64

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
            order = request.GET.get('order', '-create_date')
            field_dict = {
                'id': '',
                'name': '__contains',
                'create_date': '',
                'oper_user__username': '__contains',
            }
            q = conditionCom(request, field_dict)

            objs = models.zhugedanao_userprofile.objects.select_related('role').filter(q).order_by('-order')
            obj_count = objs.count()
            # 分页
            if length != 0:
                start_line = (current_page - 1) * length
                stop_line = start_line + length
                objs = objs[start_line: stop_line]
            data_list = []
            for obj in objs:
                role_name = ''
                if obj.role:
                    role_name =obj.role.name
                decode_username = base64.b64decode(obj.username)
                username = str(decode_username, 'utf-8')
                data_list.append({
                    'o_id':obj.id,
                    'username' : username,
                    'level' : obj.level_name.name,
                    'create_date' : obj.create_date,
                    'role' : role_name
                })
            response.code = 200
            response.msg = '查询成功'
            response.data = {
                'data_list' : data_list,
                'obj_count':obj_count
            }
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
            if objs:
                obj = objs[0]
                roleName = '无角色'
                if obj.role:
                    roleName = obj.role.name
                levelName = ''
                if obj.level_name:
                    levelName = obj.level_name.name,
                otherData = {
                    'user_level' : levelName,
                    'role':roleName
                }
                response.code = 200
                response.msg = '查询成功'
                response.data = {'otherData':otherData}

        # 确认修改数据
        if oper_type == 'afterUpdate':
            objs = models.zhugedanao_userprofile.objects.select_related('role').filter(id=o_id)
            role = request.POST.get('role')
            user_level = request.POST.get('user_level')
            levelObjs = models.zhugedanao_level.objects.filter(id=user_level)
            roleObjs = models.zhugedanao_role.objects.filter(id=role)
            if roleObjs and levelObjs:
                objs.update(
                    role_id=role,
                    level_name_id=user_level
                )
                response.code = 200
                response.msg = '修改成功'
            else:
                response.code = 402
                response.msg = '权限或角色不存在'
            response.data = {}

    else:
        if oper_type == 'getUserLevel':
            objs = models.zhugedanao_level.objects.all()
            otherData = []
            for obj in objs:
                otherData.append({
                    'o_id':obj.id,
                    'level':obj.name
                })
            response.code = 200
            response.msg = '查询成功'
            response.data = {'otherData':otherData}
        else:
            response.code = 402
            response.msg = "请求异常"



    return JsonResponse(response.__dict__)