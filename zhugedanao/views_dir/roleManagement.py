from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from zhugedanao.forms.role_management import AddForm, UpdateForm, SelectForm
import json, datetime
from publicFunc.condition_com import conditionCom
from zhugedanao.views_dir.permissions import init_data
# cerf  token验证 用户展示模块
@csrf_exempt
@account.is_token(models.zhugedanao_userprofile)
def roleManagementShow(request):
    response = Response.ResponseObj()
    user_id = request.GET.get('user_id')
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
            roleObjs = models.zhugedanao_role.objects.filter(q).order_by(order)
            roleCount = roleObjs.count()
            # 分页
            if length != 0:
                start_line = (current_page - 1) * length
                stop_line = start_line + length
                roleObjs = roleObjs[start_line: stop_line]
            retData = []
            for obj in roleObjs:
                permissionsData = []
                if obj.quanxian:
                    permissionsList = [i['id'] for i in obj.quanxian.values('id')]
                    print('permissionsList=========> ',permissionsList)
                    permissionsData = init_data(selected_list=permissionsList)
                retData.append({
                    'id':obj.id,
                    'name':obj.name,
                    'createDate':obj.create_date.strftime('%Y-%m-%d %H:%M:%S'),
                    'permissionsData':permissionsData,
                })
            response.code = 200
            response.msg = '查询成功'
            response.data = {
                'retData':retData,
                'roleCount':roleCount
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
def roleManagementOper(request, oper_type, o_id):
    response = Response.ResponseObj()
    if request.method == "POST":
        # 增加角色任务
        if oper_type == "add":
            role_name = request.POST.get('role_name')
            quanxian_list = request.POST.get('quanxian_list')
            now_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            objs = models.zhugedanao_role.objects.create(
                name=role_name,
                create_date=now_date
            )
            quanxian = quanxian_list if quanxian_list else []
            if quanxian:
                for i in json.loads(quanxian):
                    objs.quanxian.add(i)
            response.code = 200
            response.msg = "添加成功"
            response.data = {}
        # if oper_type == 'beforeUpdate':
        #     objs = models.zhugedanao_role.objects.filter(id=o_id)
        #     if objs:
        #         roleName = objs[0].name
        #         rules_list = [i['title'] for i in objs[0].quanxian.values('title')]
        #         # data_list = []
        #         # model_quanxian = objs[0].quanxian.all()
        #         # if model_quanxian:
        #         #     for quanXianTitle in model_quanxian:
        #         #         data_list.append(quanXianTitle.title)
        #         response.code = 200
        #         response.msg = '查询成功'
        #         response.data = {
        #             'roleName':roleName,
        #             'permissionList':rules_list
        #         }
        if oper_type == 'afterUpdate':
            form_data = {
                'o_id': o_id,
                'roleName' : request.POST.get('roleName'),
                'permissionList' : request.POST.get('permissionList')
            }
            roleObjs = models.zhugedanao_role.objects

            forms_obj = UpdateForm(form_data)
            if forms_obj.is_valid():
                objs = roleObjs.filter(id=o_id)
                if objs:
                    objs.update(
                        name=forms_obj.cleaned_data.get('roleName')
                    )
                    objs[0].quanxian = forms_obj.cleaned_data.get('permissionList')
                    response.code = 200
                    response.msg = '修改成功'
                else:
                    response.code = 302
                    response.msg = '修改的ID不存在'
            else:
                response.code = 303
                response.msg = json.loads(forms_obj.errors.as_json())

        if oper_type == 'delete':
            roleObjs = models.zhugedanao_role.objects
            objs = roleObjs.filter(id=o_id)
            if objs:
                if objs[0].zhugedanao_userprofile_set.all().count() > 0:
                    response.code = 304
                    response.msg = '含有子级数据,请先删除或转移子级数据'
                else:
                    objs.delete()
                    response.code = 200
                    response.msg = '删除成功'
            else:
                response.code = 302
                response.msg = '删除ID不存在'
            response.data = {}
    else:
        # 获取角色对应的权限
        if oper_type == "get_rules":
            objs = models.zhugedanao_role.objects.filter(id=o_id)
            if objs:
                obj = objs[0]
                rules_list = [i['title'] for i in obj.quanxian.values('title')]
                response.data = {
                    'rules_list': rules_list
                }
                response.code = 200
                response.msg = "查询成功"
        else:
            response.code = 402
            response.msg = "请求异常"

    return JsonResponse(response.__dict__)



















