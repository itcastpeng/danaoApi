

from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import datetime
from zhugedanao.forms.zhongdianci_jiankong import AddForm, SelectForm
import json, time, re

# cerf  token验证 用户展示模块
@csrf_exempt
@account.is_token(models.zhugedanao_userprofile)
def zhongDianCiShowTaskList(request):
    response = Response.ResponseObj()
    user_id = request.GET.get('user_id')
    if request.method == "GET":
        print('=========================', user_id)
        forms_obj = SelectForm(request.GET)
        if forms_obj.is_valid():
            current_page = forms_obj.cleaned_data['current_page']
            length = forms_obj.cleaned_data['length']
            objs = models.zhugedanao_zhongdianci_jiankong_taskList.objects.filter(
                user_id_id=user_id)
            # 分页
            if length != 0:
                start_line = (current_page - 1) * length
                stop_line = start_line + length
                objs = objs[start_line: stop_line]
            if objs:
                is_zhixing_count = models.zhugedanao_zhongdianci_jiankong_taskDetail.objects.filter(
                    tid=objs[0].id
                ).filter(
                    is_perform=1
                ).count()
                baifenbi = 0
                if is_zhixing_count:
                    baifenbi = int((is_zhixing_count / objs.count()) * 100)
                data_list = []
                for obj in objs:
                    data_list.append({
                        "id": obj.id,
                        "qiyong_status": obj.qiyong_status,
                        "task_name": obj.task_name,
                        "task_start_time": obj.task_start_time,
                        "task_status": obj.task_status,
                        "search_engine": obj.search_engine.split(','),
                        'task_jindu': int(baifenbi),
                    })
                response.msg = '查询成功'
                response.code = 200
                response.data = {'data_list':data_list}
            else:
                response.msg = '无任务'
        else:
            response.code = 402
            response.msg = "请求异常"
            response.data = json.loads(forms_obj.errors.as_json())
    return JsonResponse(response.__dict__)


@csrf_exempt
@account.is_token(models.zhugedanao_userprofile)
def zhongDianCiDetailShowTaskList(request):
    response = Response.ResponseObj()
    user_id = request.GET.get('user_id')
    tid = request.GET.get('tid')
    forms_obj = SelectForm(request.GET)
    if forms_obj.is_valid():
        current_page = forms_obj.cleaned_data['current_page']
        length = forms_obj.cleaned_data['length']
        objs = models.zhugedanao_zhongdianci_jiankong_taskDetail.objects.select_related('tid__user_id').filter(
            tid__user_id=user_id,
            tid=tid
        )
        detail_task_count = objs.count()
        # 分页
        if length != 0:
            start_line = (current_page - 1) * length
            stop_line = start_line + length
            objs = objs[start_line: stop_line]
        if objs:
            data_list = []
            for obj in objs:
                data_list.append({
                    "id": obj.id,
                    "tid": obj.tid_id,
                    "search_engine": obj.search_engine,
                    "lianjie": obj.lianjie,
                    "keywords": obj.keyword,
                    "mohupipei": obj.mohupipei,
                    "create_time": obj.create_time,
                })
            data_dict = {
                'count':detail_task_count,
                'data_list':data_list
            }
            response.code = 200
            response.msg = '查询成功'
            response.data = {'data_dict':data_dict}
        else:
            response.msg = '无任务'
    else:
        response.code = 402
        response.msg = "请求异常"
        response.data = json.loads(forms_obj.errors.as_json())
    return JsonResponse(response.__dict__)

#  增删改
#  csrf  token验证
@csrf_exempt
@account.is_token(models.zhugedanao_userprofile)
def zhongDianCiOper(request, oper_type, o_id):
    response = Response.ResponseObj()
    user_id = request.GET.get('user_id')
    if request.method == "POST":
        # 增加收录任务
        if oper_type == "add":
            user_id = request.GET.get('user_id')
            # models.zhugedanao_shoulu_chaxun.objects.filter(user_id_id=user_id).delete()
            qiyong_status =  request.POST.get('qiyong_status'),
            mohupipei = request.POST.get('mohupipei')
            form_data = {
                'task_name' : request.POST.get('task_name'),
                'search_engine' : request.POST.get('search_engine'),
                'keywords' : request.POST.get('keywords'),
                'task_start_time' : request.POST.get('task_start_time'),
                'task_status' : request.POST.get('task_status'),
            }
            forms_obj = AddForm(form_data)
            if forms_obj.is_valid():
                keywords = forms_obj.cleaned_data.get('keywords')
                # keyword_list = list(set(keywords.split('\n')))        # 去重
                keyword_list = list(keywords.split('\n'))
                qiyongstatus = False
                if qiyong_status:
                    qiyongstatus = True
                now_date = datetime.date.today().strftime('%Y-%m-%d') # 当前年月日
                canshu = now_date + ' ' + form_data['task_start_time']
                kaishishijian = datetime.datetime.today().strptime(canshu, "%Y-%m-%d %H:%M:%S") # 传来的参数 时分秒
                now = now_date + ' ' + time.strftime("%H:%M:%S")
                now_time = datetime.datetime.today().strptime(now, "%Y-%m-%d %H:%M:%S") #当前时分秒
                next_datetime = kaishishijian
                if kaishishijian < now_time:
                    next_datetime = (kaishishijian + datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
                objs = models.zhugedanao_zhongdianci_jiankong_taskList.objects.create(
                    task_name=forms_obj.cleaned_data.get('task_name'),
                    task_status=forms_obj.cleaned_data.get('task_status'),
                    search_engine=','.join(forms_obj.cleaned_data.get('search_engine')),
                    next_datetime=next_datetime,
                    task_start_time=form_data['task_start_time'],
                    qiyong_status=qiyongstatus,
                    user_id_id=user_id
                )
                querysetlist = []
                create_time = datetime.datetime.today().strftime("%Y-%m-%d %H-%M-%S")
                for search in forms_obj.cleaned_data.get('search_engine'):
                    for keywords in keyword_list:
                        if 'http' in keywords:
                            re_keyword = re.findall("(.*)http", keywords.replace('\t', ''))
                            url_list = keywords.split(re_keyword[0])
                            url = url_list[1]
                            if url and re_keyword:
                                querysetlist.append(
                                    models.zhugedanao_zhongdianci_jiankong_taskDetail(
                                        tid_id=objs.id,
                                        search_engine=search,
                                        lianjie=url,
                                        keyword=re_keyword[0],
                                        create_time=create_time
                                    )
                                )
                        else:
                            if mohupipei:
                                querysetlist.append(
                                    models.zhugedanao_zhongdianci_jiankong_taskDetail(
                                        tid_id=objs.id,
                                        search_engine=search,
                                        keyword=keywords,
                                        mohupipei=mohupipei,
                                        create_time=create_time
                                    )
                                )
                models.zhugedanao_zhongdianci_jiankong_taskDetail.objects.bulk_create(querysetlist)
                response.code = 200
                response.msg = "添加成功"

            else:
                print("验证不通过")
                response.code = 301
                response.msg = json.loads(forms_obj.errors.as_json())
        else:
            response.code = 402
            response.msg = "请求异常"

    return JsonResponse(response.__dict__)

