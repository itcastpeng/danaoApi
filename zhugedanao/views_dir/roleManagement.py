from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from zhugedanao.forms.role_management import AddForm, SelectForm
import json, datetime


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

            yuming_objs = models.zhugedanao_pingtaiwajue_yuming.objects.filter(tid__user_id=user_id)

            # 分页
            if length != 0:
                start_line = (current_page - 1) * length
                stop_line = start_line + length
                objs = yuming_objs[start_line: stop_line]
            data_list = []


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
            print(request.POST)
            now_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            role_name = request.POST.get('role_name')
            quanxian_list = request.POST.get('quanxian_list')
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

        if oper_type == 'update':
            objs = models.zhugedanao_role.objects.filter(id=o_id)
            roleName = objs[0].name
            model_quanxian = objs[0].quanxian.all()
            print(roleName)
            for quanxian in model_quanxian:
                print(quanxian.title)


        if oper_type == 'delete':
            pass

    else:
        # 获取角色对应的权限
        if oper_type == "get_rules":
            objs = models.zhugedanao_role.objects.filter(id=o_id)
            if objs:
                obj = objs[0]
                rules_list = [i['name'] for i in obj.permissions.values('name')]
                print('dataList -->', rules_list)
                response.data = {
                    'rules_list': rules_list
                }

                response.code = 200
                response.msg = "查询成功"
        else:
            response.code = 402
            response.msg = "请求异常"

    return JsonResponse(response.__dict__)



















