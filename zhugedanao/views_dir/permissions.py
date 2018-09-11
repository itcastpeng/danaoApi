from publicFunc.condition_com import conditionCom
from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from zhugedanao.forms.permissons import AddForm, UpdateForm, SelectForm
import json


def init_data(pid=None, selected_list=None):
    """
    获取权限数据
    :param pid:  权限父级id
    :return:
    """
    print('pid------->',pid)
    result_data = []
    objs = models.zhugedanao_quanxian.objects.filter(pid_id=pid)
    for obj in objs:
        current_data = {
            'title': obj.title,
            'expand': True,
            'id': obj.id,
            'checked': False
        }
        if selected_list and obj.id in selected_list:
            current_data['checked'] = True
        children_data = init_data(obj.id)
        if children_data:
            current_data['children'] = children_data
        result_data.append(current_data)

    # print('result_data -->', result_data)
    return result_data


# cerf  token验证 用户展示模块
@csrf_exempt
@account.is_token(models.zhugedanao_userprofile)
def permissionsShow(request):
    response = Response.ResponseObj()
    if request.method == "GET":
        forms_obj = SelectForm(request.GET)
        if forms_obj.is_valid():
            current_page = forms_obj.cleaned_data['current_page']
            length = forms_obj.cleaned_data['length']
            print('forms_obj.cleaned_data -->', forms_obj.cleaned_data)
            order = request.GET.get('order', '-create_date')
            field_dict = {
                'id': '',
                'title': '__contains',
                'create_date': '',
                'oper_user__username': '__contains',
                'pid_id': '__isnull'
            }
            q = conditionCom(request, field_dict)
            print('q -->', q)

            objs = models.zhugedanao_quanxian.objects.select_related('pid').filter(q).order_by(order)
            count = objs.count()

            if length != 0:
                start_line = (current_page - 1) * length
                stop_line = start_line + length
                objs = objs[start_line: stop_line]

            # 返回的数据
            ret_data = []

            for obj in objs:
                #  如果有oper_user字段 等于本身名字
                if obj.oper_user:
                    oper_user_username = obj.oper_user.username
                else:
                    oper_user_username = ''
                # print('oper_user_username -->', oper_user_username)
                #  将查询出来的数据 加入列表
                pid_title = ''
                if obj.pid:
                    pid_title = obj.pid.title
                ret_data.append({
                    'id': obj.id,
                    'title': obj.title,
                    'pid_id': obj.pid_id,
                    'pid_title': pid_title,
                    'create_date': obj.create_date.strftime('%Y-%m-%d %H:%M:%S'),
                    'oper_user__username': oper_user_username,
                })
            #  查询成功 返回200 状态码
            response.code = 200
            response.msg = '查询成功'
            response.data = {
                'ret_data': ret_data,
                'data_count': count,
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
def permissions_oper(request, oper_type, o_id):
    response = Response.ResponseObj()
    if request.method == "POST":
        if oper_type == "add":
            form_data = {
                'title': request.POST.get('title'),
                'pid_id': request.POST.get('pid_id'),
                'oper_user_id': request.GET.get('user_id'),
            }
            #  创建 form验证 实例（参数默认转成字典）
            forms_obj = AddForm(form_data)
            if forms_obj.is_valid():
                print("验证通过")
                #  添加数据库
                print('forms_obj.cleaned_data-->',forms_obj.cleaned_data)
                models.zhugedanao_quanxian.objects.create(**forms_obj.cleaned_data)
                response.code = 200
                response.msg = "添加成功"
            else:
                print("验证不通过")
                response.code = 301
                response.msg = json.loads(forms_obj.errors.as_json())

        elif oper_type == "delete":
            # 删除 ID
            objs = models.zhugedanao_quanxian.objects.filter(id=o_id)
            if objs:
                obj = objs[0]
                if models.zhugedanao_quanxian.objects.filter(pid_id=obj.id).count() > 0:
                    response.code = 304
                    response.msg = "含有子级数据,请先删除或转移子级数据"
                else:
                    objs.delete()
                    response.code = 200
                    response.msg = "删除成功"
            else:
                response.code = 302
                response.msg = '删除ID不存在'

        elif oper_type == "update":
            # 获取需要修改的信息
            form_data = {
                'title': request.POST.get('title'),
                'pid_id': request.POST.get('pid_id'),
            }

            forms_obj = UpdateForm(form_data)
            if forms_obj.is_valid():
                print("验证通过")
                title = forms_obj.cleaned_data['title']
                pid_id = forms_obj.cleaned_data['pid_id']
                #  查询数据库  用户id
                objs = models.zhugedanao_quanxian.objects.filter(
                    id=o_id
                )
                #  更新 数据
                if objs:
                    objs.update(
                        title=title,
                        pid_id=pid_id,
                    )

                    response.code = 200
                    response.msg = "修改成功"
                else:
                    response.code = 303
                    response.msg = json.loads(forms_obj.errors.as_json())

            else:
                response.code = 301
                response.msg = json.loads(forms_obj.errors.as_json())

    else:
        print('==============')
        if oper_type == "get_tree_data":
            response.code = 200
            response.msg = "获取tree数据成功"
            response.data = {
                'ret_data': json.dumps(init_data())
            }
        else:
            response.code = 402
            response.msg = "请求异常"

    return JsonResponse(response.__dict__)
