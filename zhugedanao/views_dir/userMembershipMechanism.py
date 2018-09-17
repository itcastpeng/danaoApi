from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from zhugedanao.forms.userMemberShip import AddForm, SelectForm
import json, base64
# cerf  token验证 用户展示模块
@csrf_exempt
@account.is_token(models.zhugedanao_userprofile)
def userMembershipShow(request):
    response = Response.ResponseObj()
    if request.method == "GET":
        forms_obj = SelectForm(request.GET)
        if forms_obj.is_valid():
            current_page = forms_obj.cleaned_data['current_page']
            length = forms_obj.cleaned_data['length']
            role_id = request.GET.get('role_id')
            mouth = forms_obj.cleaned_data.get('mouth')
            level = forms_obj.cleaned_data.get('level')
            objs = models.zhugedanao_user_level_permissions.objects.filter(theOpeningTime=1)
            if level == 2:
                objs = models.zhugedanao_user_level_permissions.objects.filter(
                    membershipGrade_id=2)
            elif level == 3:
                objs = models.zhugedanao_user_level_permissions.objects.filter(
                membershipGrade_id=3)
            riqi = 1
            if mouth:
                if int(mouth) == 3:
                    riqi = 2
                elif int(mouth) == 5:
                    riqi = 3
                elif int(mouth) == 10:
                    riqi = 4
                objs = objs.filter(theOpeningTime=riqi)
            # 分页
            if length != 0:
                start_line = (current_page - 1) * length
                stop_line = start_line + length
                objs = objs[start_line: stop_line]
            obj_count = objs.count()
            data_list = []
            for obj in objs:
                decode_username = base64.b64decode(obj.oper_user.username)
                username = str(decode_username, 'utf-8')
                data_list.append({
                   'membershipGrade' :obj.membershipGrade.name,
                   'theOpeningTime' :obj.get_theOpeningTime_display(),
                   'price' :obj.price,
                   'shouLuChaXunNum' :obj.shouLuChaXunNum,
                   'fuGaiChaXunNum' :obj.fuGaiChaXunNum,
                   'zhongDianCiNum' :obj.zhongDianCiNum,
                   'pingTaiWaJueNum' :obj.pingTaiWaJueNum,
                   'baiDuXiaLaNum' :obj.baiDuXiaLaNum,
                   'oper_user' :username,
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
def userMembershipOper(request, oper_type, o_id):
    response = Response.ResponseObj()
    user_id = request.GET.get('user_id')
    if request.method == "POST":
        if oper_type == "addUserIntegral":
            form_data = {
                'membershipGrade': request.POST.get('membershipGrade'),  # 会员等级
                'theOpeningTime': request.POST.get('theOpeningTime'),    # 时长
                'price': request.POST.get('price'),                      # 钱数
                'shouLuChaXunNum': request.POST.get('shouLuChaXunNum'),  # 收录查询
                'fuGaiChaXunNum': request.POST.get('fuGaiChaXunNum'),    # 覆盖查询
                'zhongDianCiNum': request.POST.get('zhongDianCiNum'),    # 重点词
                'pingTaiWaJueNum': request.POST.get('pingTaiWaJueNum'),  # 平台挖掘
                'baiDuXiaLaNum': request.POST.get('baiDuXiaLaNum')       # 百度下拉
            }
            forms_obj = AddForm(form_data)
            if forms_obj.is_valid():
            # 添加数据库
                models.zhugedanao_user_level_permissions.objects.create(
                    oper_user_id=user_id,
                    membershipGrade_id=forms_obj.cleaned_data.get('membershipGrade'),
                    theOpeningTime=forms_obj.cleaned_data.get('theOpeningTime'),
                    price=forms_obj.cleaned_data.get('price'),
                    shouLuChaXunNum=forms_obj.cleaned_data.get('shouLuChaXunNum'),
                    fuGaiChaXunNum=forms_obj.cleaned_data.get('fuGaiChaXunNum'),
                    zhongDianCiNum=forms_obj.cleaned_data.get('zhongDianCiNum'),
                    pingTaiWaJueNum=forms_obj.cleaned_data.get('pingTaiWaJueNum'),
                    baiDuXiaLaNum=forms_obj.cleaned_data.get('baiDuXiaLaNum')
                )

                response.code = 200
                response.msg = '添加成功'
            else:
                response.code = 301
                response.msg = json.loads(forms_obj.errors.as_json())
            response.data = {}
        elif oper_type == 'updateUserIntegral':
            form_data = {
                'membershipGrade': request.POST.get('membershipGrade'),  # 会员等级
                'theOpeningTime': request.POST.get('theOpeningTime'),  # 时长
                'price': request.POST.get('price'),  # 钱数
                'shouLuChaXunNum': request.POST.get('shouLuChaXunNum'),  # 收录查询
                'fuGaiChaXunNum': request.POST.get('fuGaiChaXunNum'),  # 覆盖查询
                'zhongDianCiNum': request.POST.get('zhongDianCiNum'),  # 重点词
                'pingTaiWaJueNum': request.POST.get('pingTaiWaJueNum'),  # 平台挖掘
                'baiDuXiaLaNum': request.POST.get('baiDuXiaLaNum')  # 百度下拉
            }
            forms_obj = AddForm(form_data)
            if forms_obj.is_valid():
                # 添加数据库
                objs = models.zhugedanao_user_level_permissions.objects.filter(id=o_id)
                objs.update(
                    oper_user_id=user_id,
                    membershipGrade_id=forms_obj.cleaned_data.get('membershipGrade'),
                    theOpeningTime=forms_obj.cleaned_data.get('theOpeningTime'),
                    price=forms_obj.cleaned_data.get('price'),
                    shouLuChaXunNum=forms_obj.cleaned_data.get('shouLuChaXunNum'),
                    fuGaiChaXunNum=forms_obj.cleaned_data.get('fuGaiChaXunNum'),
                    zhongDianCiNum=forms_obj.cleaned_data.get('zhongDianCiNum'),
                    pingTaiWaJueNum=forms_obj.cleaned_data.get('pingTaiWaJueNum'),
                    baiDuXiaLaNum=forms_obj.cleaned_data.get('baiDuXiaLaNum')
                )
                response.code = 200
                response.msg = '修改成功'
                response.data = {}
    else:
        # 添加前查询
        if oper_type == 'queryBeforeAdding':
            objs = models.zhugedanao_user_level_permissions.status_choices
            billingList = []
            for obj in objs:
                billingList.append({
                    obj[0]: obj[1]
                })
            levelObjs = models.zhugedanao_level.objects.all()
            levelList = []
            for levelObj in levelObjs:
                levelList.append({
                    'id':levelObj.id,
                    'name':levelObj.name
                })
            response.code = 200
            response.msg = '查询成功'
            response.data = {
                'billingList':billingList,
                'levelList':levelList
            }
        elif oper_type == 'delete':
            objs = models.zhugedanao_user_level_permissions.objects.filter(id=o_id)
            if objs:
                objs.delete()
                response.code = 200
                response.msg = '删除成功'
            else:
                response.code = 302
                response.msg = '无此会员机制'
            response.data = {}
        else:
            response.code = 402
            response.msg = "请求异常"
    return JsonResponse(response.__dict__)
