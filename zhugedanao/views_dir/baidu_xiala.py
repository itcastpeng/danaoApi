from openpyxl.styles import Font, Alignment
from openpyxl import Workbook
import os, time
from zhugedanao import models
from publicFunc import Response
from publicFunc import account
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import datetime
from zhugedanao.forms.baidu_xiala import AddForm, SelectForm
import json
import random
from django.db.models import Count,Q, Sum
import threading
chongfu = 0

# cerf  token验证 用户展示模块
@csrf_exempt
@account.is_token(models.zhugedanao_userprofile)
def baiDuXiaLaShow(request):
    response = Response.ResponseObj()
    user_id = request.GET.get('user_id')
    if request.method == "GET":
        forms_obj = SelectForm(request.GET)
        if forms_obj.is_valid():
            current_page = forms_obj.cleaned_data['current_page']
            length = forms_obj.cleaned_data['length']
            objs = models.zhugedanao_baiduxiala_chaxun.objects.filter(user_id_id=user_id)
            obj_count = objs.count()
            num = 0
            for obj in objs:
                for xiala in eval(obj.xialaci):
                    num += 1
            # 分页
            if length != 0:
                start_line = (current_page - 1) * length
                stop_line = start_line + length
                objs = objs[start_line: stop_line]
            data_list = []
            for obj in objs:
                if obj.xialaci:
                    for xialaci in eval(obj.xialaci):
                        data_list.append({
                            'keyword': obj.keyword,
                            'search': obj.search,
                            'xialaci': xialaci
                        })
                else:
                    data_list.append({
                        'keyword': obj.keyword,
                        'search': obj.search,
                        'xialaci': ''
                    })
            response.code = 200
            response.msg = '查询成功'
            response.data = {
                'retData': data_list,
                'keyword_count':obj_count,
                'obj_count':num,
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
def baiDuXiaLa(request, oper_type, o_id):
    response = Response.ResponseObj()
    user_id = request.GET.get('user_id')
    if request.method == "POST":
        # 增加下拉任务
        if oper_type == "add":
            form_data = {
                'search_list': request.POST.get('searchEngineModel'),
                'keywords_list': request.POST.get('editor_content'),
            }
            querysetlist = []
            forms_obj = AddForm(form_data)
            if forms_obj.is_valid():
                models.zhugedanao_baiduxiala_chaxun.objects.filter(user_id_id=user_id).delete()
                chongfu = int(len(forms_obj.cleaned_data.get('keywords_list'))) - int(len(set(forms_obj.cleaned_data.get('keywords_list'))))

                now_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                for search in eval(forms_obj.cleaned_data.get('search_list')):
                    for keyword in set(forms_obj.cleaned_data.get('keywords_list')):
                        print(search, keyword)
                        querysetlist.append(
                            models.zhugedanao_baiduxiala_chaxun(
                                user_id_id = user_id,
                                keyword = keyword,
                                search = search,
                                is_zhixing = 0,
                                createAndStart_time=now_date
                            )
                        )
                models.zhugedanao_baiduxiala_chaxun.objects.bulk_create(querysetlist)
                response.code = 200
                response.msg = "添加成功"
                response.data = {}
            else:
                print("验证不通过")
                response.code = 301
                response.msg = json.loads(forms_obj.errors.as_json())

    elif request.method == 'GET':
        # 点击返回 删除任务
        if oper_type == 'clickReturn':
            response.code = 200
            response.msg = '退出成功'
            models.zhugedanao_pingtaiwajue_yuming.objects.filter(
                tid__user_id_id=user_id
            ).delete()
            models.zhugedanao_pingtaiwajue_keyword.objects.filter(
                user_id_id=user_id
            ).delete()
            return JsonResponse(response.__dict__)

        # 生成excel
        if oper_type == 'generateExcel':
            now_date = datetime.datetime.today().strftime('%Y-%m-%d %H-%M-%S')
            wb = Workbook()
            ws = wb.active
            ws.cell(row=1, column=1, value="任务名称")
            ws.cell(row=3, column=1, value="序号")
            ws.cell(row=3, column=2, value="平台名称")
            ws.cell(row=3, column=3, value="排名数")
            ws.cell(row=3, column=4, value="比例")
            ws.cell(row=3, column=5, value="搜索引擎")
            ws.cell(row=3, column=6, value="查询时间:{}".format(now_date))
            # ft1 = Font(name='宋体', size=22)
            # a1 = ws['A1']
            # a1.font = ft1

            # 合并单元格        开始行      结束行       用哪列          占用哪列
            ws.merge_cells(start_row=1, end_row=2, start_column=1, end_column=8)
            ws.merge_cells(start_row=3, end_row=3, start_column=1, end_column=1)
            ws.merge_cells(start_row=3, end_row=3, start_column=2, end_column=2)
            ws.merge_cells(start_row=3, end_row=3, start_column=3, end_column=3)
            ws.merge_cells(start_row=3, end_row=3, start_column=4, end_column=4)
            ws.merge_cells(start_row=3, end_row=3, start_column=5, end_column=5)
            ws.merge_cells(start_row=3, end_row=3, start_column=6, end_column=8)
            ws.merge_cells(start_row=4, end_row=4, start_column=6, end_column=8)
            ws.merge_cells(start_row=5, end_row=5, start_column=6, end_column=8)

            # print('设置列宽')
            ws.column_dimensions['A'].width = 9
            ws.column_dimensions['B'].width = 30
            ws.column_dimensions['C'].width = 9
            ws.column_dimensions['D'].width = 20
            ws.column_dimensions['E'].width = 9
            ws.column_dimensions['F'].width = 10
            ws.column_dimensions['H'].width = 70

            # print('设置行高')
            # ws.row_dimensions[1].height = 28

            # print('文本居中')
            ws['A1'].alignment = Alignment(horizontal='center', vertical='center')
            ws['D2'].alignment = Alignment(horizontal='center', vertical='center')
            ws['E2'].alignment = Alignment(horizontal='center', vertical='center')
            ws['F3'].alignment = Alignment(horizontal='center', vertical='center')
            ws['F4'].alignment = Alignment(horizontal='center', vertical='center')
            ws['F5'].alignment = Alignment(horizontal='center', vertical='center')
            row = 4
            objs = models.zhugedanao_pingtaiwajue_yuming.objects.filter(tid__user_id_id=user_id)
            number_count = objs.values('tid__user_id').annotate(Sum('number'))
            print('number_count==========> ',number_count)
            number = 0
            bili = 0
            yinqing = '百度'
            for obj in objs:
                if str(obj.tid.search) == '1':
                    yinqing = '百度'
                elif str(obj.tid.search) == '4':
                    yinqing = '手机百度'
                elif str(obj.tid.search) == '3':
                    yinqing = '360'
                elif str(obj.tid.search) == '6':
                    yinqing = '手机360'
                number += 1
                if obj.number:
                    bili = int((int(obj.number) / int(number_count[0]['number__sum'])) * 100)
                ws.cell(row=row, column=1, value="{number}".format(number=number))
                ws.cell(row=row, column=2, value="{title}".format(title=obj.yuming))
                ws.cell(row=row, column=3, value="{title}".format(title=obj.number))
                ws.cell(row=row, column=4, value="{bili}".format(bili=str(bili) + '%'))
                ws.cell(row=row, column=5, value="{search}".format(search=yinqing))
                row += 1
            ws.cell(row=4, column=6, value="总排名数:{}".format(number_count[0]['number__sum']))
            ws.cell(row=5, column=6, value="平台数:1")
            randInt = random.randint(1, 100)
            nowDateTime = int(time.time())
            excel_name = str(randInt) + str(nowDateTime)
            wb.save(os.path.join(os.getcwd(), 'statics', 'zhugedanao', 'pingTaiWaJueExcel' , '{}.xlsx'.format(excel_name)))
            response.code = 200
            response.msg = '生成成功'
            response.data = {'excel_name':'http://api.zhugeyingxiao.com/' + os.path.join('statics', 'zhugedanao', 'pingTaiWaJueExcel' , '{}.xlsx'.format(excel_name))}
            return JsonResponse(response.__dict__)

    else:
        response.code = 402
        response.msg = "请求异常"

    return JsonResponse(response.__dict__)