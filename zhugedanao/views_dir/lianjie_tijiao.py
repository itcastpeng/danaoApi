from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import datetime
from publicFunc.condition_com import conditionCom
from zhugedanao.forms.lianjie_tijiao import AddForm, UpdateForm, SelectForm, UpdateTaskForm
import json

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

                # jindu = 0
                # if obj.task_progress:
                #     jindu = int((int(obj.task_progress) / int(obj.count_taskList)) * 100)
                yiwancheng_obj = 0
                wancheng = 0
                if count != 0:
                    # yiwancheng_obj = int(obj.count_taskList - detail_count)
                    yiwancheng_obj = detail_task_count.exclude(status=1).count()
                    wancheng = detail_task_count.filter(is_zhixing=1).count()
                jindu = 0
                if wancheng:
                    jindu = int((wancheng / obj.count_taskList) * 100)
                obj.task_progress = jindu
                obj.save()
                if yiwancheng_obj == obj.count_taskList:
                    obj.task_status = True
                    obj.save()
                zhuangtai = '未完成'
                if obj.task_status:
                    zhuangtai = '已完成'
                shoulu_num = detail_task_count.filter(tid=obj.id).filter(status=2).count()
                obj.shoulu_num = shoulu_num
                obj.save()
                shoulu_num = 0
                if obj.shoulu_num:
                    shoulu_num = obj.shoulu_num
                ret_data.append({
                    'id': obj.id,                                                   # 任务id
                    'task_name': obj.task_name,                                     # 任务名称
                    'task_status':zhuangtai,                                        # 任务状态 完成 未完成
                    'task_progress': obj.task_progress,                             # 进度条
                    'create_date': obj.create_date.strftime('%Y-%m-%d %H:%M:%S'),   # 创建时间
                    'count_taskList':obj.count_taskList,                            # 详情数量
                    'yiwancheng_obj': yiwancheng_obj,                               # 已完成数量
                    'is_update':int(obj.is_update),                                 # 是否可以修改和删除 1不可以 0可以
                    'shoulu_num':shoulu_num,                                        # 已收录数量
                })
            response.code = 200
            response.msg = '查询成功'
            response.data = {
                'ret_data': ret_data,
                'data_count': count,    # 任务总数
            }
        else:
            response.code = 301
            response.msg = "数据类型验证失败"
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
                    if int(tijiaocishu) >= 3 and int(obj.status) != 2:
                        obj.status = 3
                        obj.save()
                    #  将查询出来的数据 加入列表
                    ret_data.append({
                        'id': obj.id,
                        'url': obj.url,
                        'count': obj.count,                         # 详情数据提交次数
                        'status_text':obj.get_status_display(),    # 查询状态
                        'beforeSubmit':obj.get_beforeSubmitStatus_display(),
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
            response.msg = "数据类型验证失败"
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
    user_id = request.GET.get('user_id')
    if request.method == "POST":
        print('进入------')
        if oper_type == "add":
            userObjs = models.zhugedanao_userprofile.objects.filter(id=user_id)
            userLevel = userObjs[0].level_name_id
            print('userLevel==========>',userLevel)
            form_data = {
                'oper_user_id': user_id ,
                'name': request.POST.get('name'),
                'url': request.POST.get('url'),
                'userLevel' : userLevel
            }
            #  创建 form验证 实例（参数默认转成字典）
            task_list_count = models.zhugedanao_lianjie_task_list.objects.filter(user_id_id=form_data['oper_user_id']).count()
            if userLevel == 2: # 1为一级用户 2为二级用户 判断用户为几级用户
                tijiaoCount = 9
                message = '最多创建10个任务!'
            elif userLevel == 3:
                tijiaoCount = 19
                message = '最多创建20个任务!'
            else:
                tijiaoCount = 4
                message = '最多创建5个任务!'
            if int(task_list_count) <= tijiaoCount:
                forms_obj = AddForm(form_data)
                if forms_obj.is_valid():
                    #  添加数据库
                    # print('forms_obj.cleaned_data-->',forms_obj.cleaned_data)
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
                    response.code = 301
                    response.msg = json.loads(forms_obj.errors.as_json())
            else:
                response.code = 301
                response.msg = message

        # 删除任务
        elif oper_type == "delete":
            task_list_objs = models.zhugedanao_lianjie_task_list.objects.get(id=o_id)
            task_detale_objs = task_list_objs.zhugedanao_lianjie_tijiao_set.filter(tid_id=task_list_objs.id)
            for task_detale_obj in task_detale_objs:
                print('task_detale_obj.id-------> ', task_detale_obj.id)
                models.zhugedanao_lianjie_tijiao_log.objects.filter(
                    zhugedanao_lianjie_tijiao_id=task_detale_obj.id).delete()
            task_detale_objs.delete()
            task_list_objs.delete()
            response.code = 200
            response.msg = "删除成功"

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
