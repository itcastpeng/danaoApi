from django.shortcuts import render
from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import time
import datetime
from publicFunc.condition_com import conditionCom
from zhugedanao.forms.lianjie_tijiao import AddForm, UpdateForm, SelectForm, UpdateTaskForm
import json
import re

# cerf  token验证 用户展示模块
@csrf_exempt
@account.is_token(models.zhugedanao_userprofile)
def lianjie_tijiao(request):
    response = Response.ResponseObj()
    if request.method == "GET":
        print('查询任务列表=========================', request.GET)
        forms_obj = SelectForm(request.GET)
        if forms_obj.is_valid():
            current_page = forms_obj.cleaned_data['current_page']
            length = forms_obj.cleaned_data['length']
            order = request.GET.get('order', '-create_date')
            field_dict = {
                'id': '',
                'task_name': '',
                'task_status': '',
                'task_progress': '',
                'create_date': '',
                'user_id':''
            }
            q = conditionCom(request, field_dict)
            print('q -->', q)
            objs = models.zhugedanao_lianjie_task_list.objects.filter(q).order_by(order)
            count = objs.count()        # 任务列表总数
            if length != 0:
                start_line = (current_page - 1) * length
                stop_line = start_line + length
                objs = objs[start_line: stop_line]
            # 返回的数据
            ret_data = []
            for obj in objs:
                # print(type(datetime.datetime.now()))
                next_datetime_addoneday = (datetime.datetime.now() - datetime.timedelta(minutes=30))
                # print(type(next_datetime_addoneday))
                # print('=========next--->',next_datetime_addoneday, type(next_datetime_addoneday))
                if obj.create_date < next_datetime_addoneday:
                    obj.is_update = 1
                    obj.save()
                detail_task_count = models.zhugedanao_lianjie_tijiao.objects.filter(tid=obj.id)

                # 该任务执行总数
                detail_count = detail_task_count.filter(is_zhixing=0).count()
                detail_count_jindu = detail_task_count.filter(is_zhixing=1).count()

                jindu = 0
                if obj.count_taskList:
                    jindu = int((int(detail_count_jindu) / int(obj.count_taskList)) * 100)

                yiwancheng_obj = 0
                if count != 0:
                    yiwancheng_obj = int(obj.count_taskList - detail_count)
                if yiwancheng_obj == obj.count_taskList:
                    obj.task_status = True
                    obj.save()
                zhuangtai = '未完成'
                if obj.task_status:
                    zhuangtai = '已完成'

                ret_data.append({
                    'id': obj.id,                                            # 任务id
                    'task_name': obj.task_name,                              # 任务名称
                    'task_status':zhuangtai,                                 # 任务状态 完成 未完成
                    'task_progress': jindu,                                  # 进度条
                    'create_date': obj.create_date.strftime('%Y-%m-%d %H:%M:%S'),# 创建时间
                    'count_taskList':obj.count_taskList,                     # 详情数量
                    'yiwancheng_obj': yiwancheng_obj,                        # 已完成数量
                    'is_update':int(obj.is_update)                           # 是否可以修改和删除 1不可以 0可以
                })
            response.code = 200
            response.msg = '查询成功'
            response.data = {
                'ret_data': ret_data,
                'data_count': count,    # 任务总数
            }
        else:
            response.code = 301
            # response.msg = "请求异常"
            response.data = json.loads(forms_obj.errors.as_json())
    else:
        response.code = 402
        response.msg = "请求异常"

    return JsonResponse(response.__dict__)


@csrf_exempt
@account.is_token(models.zhugedanao_userprofile)
def lianjie_tijiao_detail(request):
    response = Response.ResponseObj()
    if request.method == "GET":
        print('任务详情------------',request.GET)
        forms_obj = SelectForm(request.GET)
        if forms_obj.is_valid():
            current_page = forms_obj.cleaned_data['current_page']
            length = forms_obj.cleaned_data['length']
            tid = request.GET.get('tid')
            order = request.GET.get('order', 'id')
            field_dict = {
                'id': '',
                'url': '__contains',
                'tid':tid
            }
            print('tid---------> ',tid)
            if tid:
                q = conditionCom(request, field_dict)
                print('q -->', q)
                objs = models.zhugedanao_lianjie_tijiao.objects.filter(q).order_by(order)
                count = objs.count()
                print('count----> ',count)
                if length != 0:
                    start_line = (current_page - 1) * length
                    stop_line = start_line + length
                    objs = objs[start_line: stop_line]

                # 返回的数据
                ret_data = []
                for obj in objs:
                    tijiaocishu = models.zhugedanao_lianjie_tijiao_log.objects.filter(
                        zhugedanao_lianjie_tijiao_id=obj.id
                    ).count()
                    obj.count = tijiaocishu
                    obj.save()
                    #  将查询出来的数据 加入列表
                    ret_data.append({
                        'id': obj.id,
                        'url': obj.url,
                        'count': obj.count,                         # 详情数据提交次数
                        'status_text': obj.get_status_display(),    # 查询状态
                    })
                #  查询成功 返回200 状态码
                response.code = 200
                response.msg = '查询成功'
                response.data = {
                    'ret_data': ret_data,
                    'data_count': count,
                }
        else:
            response.code = 301
            # response.msg = "请求异常"
            response.data = json.loads(forms_obj.errors.as_json())
    else:
        response.code = 402
        response.msg = "请求异常"
    return JsonResponse(response.__dict__)


#  增删改
#  csrf  token验证
@csrf_exempt
@account.is_token(models.zhugedanao_userprofile)
def lianjie_tijiao_oper(request, oper_type, o_id):
    response = Response.ResponseObj()
    if request.method == "POST":
        print('进入------')
        if oper_type == "add":
            print('链接提交  add')
            form_data = {
                'oper_user_id': request.GET.get('user_id'),
                'name': request.POST.get('name'),
                'url': request.POST.get('url')
            }
            #  创建 form验证 实例（参数默认转成字典）
            forms_obj = AddForm(form_data)
            if forms_obj.is_valid():
                print("验证通过")
                #  添加数据库
                print('forms_obj.cleaned_data-->',forms_obj.cleaned_data)
                url_list = forms_obj.cleaned_data.get('url')
                name = forms_obj.cleaned_data.get('name')
                oper_user_id = forms_obj.cleaned_data.get('oper_user_id')
                now_datetime = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                querysetlist = []
                objs_id = models.zhugedanao_lianjie_task_list.objects.create(
                    task_name = name,
                    create_date = now_datetime,
                    count_taskList=len(url_list),
                    user_id_id=oper_user_id,
                )
                for url in url_list:
                    querysetlist.append(
                        models.zhugedanao_lianjie_tijiao(
                            create_date=now_datetime,
                            tid_id=objs_id.id,
                            url=url
                        )
                    )
                models.zhugedanao_lianjie_tijiao.objects.bulk_create(querysetlist)
                response.code = 200
                response.msg = "添加成功"
            else:
                print("验证不通过")
                # print(forms_obj.errors)
                response.code = 301
                # print(forms_obj.errors.as_json())
                response.msg = json.loads(forms_obj.errors.as_json())

        # 删除任务
        elif oper_type == "delete":
            # 删除 ID
            objs = models.zhugedanao_lianjie_task_list.objects.filter(id=o_id)
            if objs:
                task_id = objs[0].id
                task_detail_objs = models.zhugedanao_lianjie_tijiao.objects.filter(tid=task_id)
                task_detail_objs.delete()
                objs.delete()
                response.code = 200
                response.msg = "删除成功"
            else:
                response.code = 302
                response.msg = '删除ID不存在'

        # 确认修改
        elif oper_type == "update_task":
            print('修改任务详情数据------------')
            form_data = {
                'o_id': o_id,
                'name': request.POST.get('name'),
                'url': request.POST.get('url')
            }
            forms_obj = UpdateTaskForm(form_data)
            if forms_obj.is_valid():
                print("验证通过")
                # print(forms_obj.cleaned_data)
                #  添加数据库
                # print('forms_obj.cleaned_data-->', forms_obj.cleaned_data)
                # models.zhugedanao_userprofile.objects.create(**forms_obj.cleaned_data)
                url_list = forms_obj.cleaned_data.get('url')
                name = forms_obj.cleaned_data.get('name')
                # oper_user_id = forms_obj.cleaned_data.get('oper_user_id')
                now_datetime = datetime.datetime.today().strftime('%Y-%m-%d %H-%M-%S')
                models.zhugedanao_lianjie_task_list.objects.filter(id=o_id).update(
                    task_name=name,
                    # create_date=now_datetime,
                    count_taskList=len(url_list)
                )
                querysetlist = []
                print('url_list-----------> ', url_list)
                objs_id = models.zhugedanao_lianjie_task_list.objects.filter(id=o_id)
                if objs_id:
                    models.zhugedanao_lianjie_tijiao.objects.filter(tid=o_id).delete()
                    for url in url_list:
                        querysetlist.append(
                            models.zhugedanao_lianjie_tijiao(
                                tid_id=objs_id[0].id,
                                url=url
                            )
                        )
                    models.zhugedanao_lianjie_tijiao.objects.bulk_create(querysetlist)
                response.code = 200
                response.msg = "修改成功"
            else:
                print("验证不通过")
                response.code = 301
                response.msg = json.loads(forms_obj.errors.as_json())

        # 获取修改前数据
        elif oper_type == 'update_show_data':
            forms_obj = SelectForm(request.GET)
            if forms_obj.is_valid():
                current_page = forms_obj.cleaned_data['current_page']
                length = forms_obj.cleaned_data['length']
                objs = models.zhugedanao_lianjie_tijiao.objects.select_related('tid').filter(tid=o_id)
                if length != 0:
                    start_line = (current_page - 1) * length
                    stop_line = start_line + length
                    objs = objs[start_line: stop_line]
                data_list = []
                for obj in objs:
                    print('obj.url------> ',obj.url)
                    data_list.append(obj.url)
                data_temp = {
                    'name':objs[0].tid.task_name,
                    'url':'\r\n'.join(data_list)
                }
                print('data_temp---> ',data_temp)
                response.code = 200
                response.data = data_temp
            else:
                print("验证不通过")
                response.code = 301
                response.msg = json.loads(forms_obj.errors.as_json())
            return JsonResponse(response.__dict__)



        elif oper_type == "update":
            # 获取需要修改的信息
            form_data = {
                'o_id': o_id,
                'name': request.POST.get('name'),
                'url': request.POST.get('url')
            }

            forms_obj = UpdateForm(form_data)
            if forms_obj.is_valid():
                print("验证通过")
                print(forms_obj.cleaned_data)
                o_id = forms_obj.cleaned_data['o_id']
                name = forms_obj.cleaned_data['name']
                url = forms_obj.cleaned_data['url']
                #  查询数据库  用户id
                objs = models.zhugedanao_lianjie_tijiao.objects.filter(
                    id=o_id,
                )
                #  更新 数据
                if objs:
                    objs.update(
                        name=name,
                        url=url
                    )
                    response.code = 200
                    response.msg = "修改成功"
                else:
                    response.code = 303
                    response.msg = json.loads(forms_obj.errors.as_json())

            else:
                print("验证不通过")
                # print(forms_obj.errors)
                response.code = 301
                # print(forms_obj.errors.as_json())
                #  字符串转换 json 字符串
                response.msg = json.loads(forms_obj.errors.as_json())

        elif oper_type == "update_status":
            status = request.POST.get('status')
            company_id = request.GET.get('company_id')
            print('status -->', status)
            objs = models.zhugedanao_userprofile.objects.filter(id=o_id, company_id=company_id)
            if objs:
                objs.update(status=status)
                response.code = 200
                response.msg = "状态修改成功"
            else:
                response.code = 301
                response.msg = "用户ID不存在"

    else:
        response.code = 402
        response.msg = "请求异常"

    return JsonResponse(response.__dict__)
