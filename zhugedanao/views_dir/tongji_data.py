from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Count, Sum
from publicFunc.Response import ResponseObj
from publicFunc.account import is_token
from zhugedanao import models
from publicFunc.condition_com import conditionCom
from django.db.models import Q

import datetime, base64, sys, io

response = ResponseObj()
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
# 统计数据
def tongji_data(request):
    nowDate = datetime.datetime.now().strftime("%Y-%m-%d")
    print(request.GET)
    start_date = request.GET.get('create_date__gte', nowDate)
    stop_date = request.GET.get('create_date__lt', '')
    # 获取参数
    field_dict = {
        'id': '',
        'name': '__contains',
        'create_date__gte': start_date,
        'create_date__lt': stop_date,
    }
    print('field_dict -->', field_dict)
    q = conditionCom(request, field_dict)
    print('q -->', q)

    userCount = models.zhugedanao_userprofile.objects.count()       # 所有用户
    userNewCount = models.zhugedanao_userprofile.objects.filter(q).count()    # 新用户

    todayHuoyueCount = len(models.zhugedanao_oper_log.objects.filter(q).values('user_id').annotate(Count('id')))   # 今日活跃

    data2 = []
    gongneng_objs = models.zhugedanao_gongneng.objects.filter(pid__isnull=True)

    for gongneng_obj in gongneng_objs:
        oper_log_q = Q(gongneng_id=gongneng_obj.id) | Q(gongneng__pid=gongneng_obj.id)
        if stop_date:
            gongneng_count = models.zhugedanao_oper_log.objects.filter(q).filter(oper_log_q).count()
        else:
            gongneng_count = models.zhugedanao_oper_log.objects.filter(oper_log_q).count()
        data2.append({
            "title": gongneng_obj.name,
            "value": gongneng_count
        })
    
    response.code = 200
    response.data = {
        "data1": [
            {
                "title": "用户总数",
                "value": userCount
            },
            {
                "title": "新增用户数",
                "value": userNewCount
            },
            {
                "title": "活跃用户数",
                "value": todayHuoyueCount
            },
        ],
        "data2": data2
    }

    return JsonResponse(response.__dict__)


# 判断时间
def determineTheTime(watch_Yesterday=None):
    now_date = datetime.datetime.now()
    stop_date = datetime.datetime.now().strftime('%Y-%m-%d 23:59:59')
    start_date = now_date.strftime('%Y-%m-%d 00:00:00')
    if watch_Yesterday == 'watchYesterday':
        start_date = (now_date - datetime.timedelta(days=1)).strftime('%Y-%m-%d 00:00:00')
    elif watch_Yesterday == 'watchSevenDays':
        start_date = (now_date - datetime.timedelta(days=6)).strftime('%Y-%m-%d 00:00:00')
    elif watch_Yesterday == 'watchThirtyDays':
        start_date = (now_date - datetime.timedelta(days=30)).strftime('%Y-%m-%d 00:00:00')
    elif watch_Yesterday == 'watchAllDays':
        start_date = '1995-01-01 00:00:00'
    return start_date, stop_date

# 分页
def pagingPage(objs, current_page, length):
    length = int(length)
    current_page = int(current_page)
    start_line = (current_page - 1) * length
    stop_line = start_line + length
    print('start_line,stop_line----------> ',start_line,stop_line)
    objs = objs[start_line: stop_line]
    return objs

# 用户统计详情
def userStatisticalDetail(request):
    objs = models.zhugedanao_userprofile.objects.filter(status=1)
    obj_count = objs.count()
    current_page = request.GET.get('current_page')
    length = request.GET.get('length')
    if length:
        objs = pagingPage(objs, current_page, length)
    otherData = []
    for obj in objs:
        sex = '男'
        if int(obj.sex) == 2:
            sex = '女'
        decode_username = base64.b64decode(obj.username)
        username = str(decode_username, 'utf-8')
        otherData.append({
            'o_id':obj.id,                  # 用户id
            'username':username,            # 用户名
            'create_time':obj.create_date.strftime('%Y-%m-%d %H-%M-%S'),  # 创建时间
            'country':obj.country,          # 国家
            'province':obj.province,        # 省份
            'city':obj.city,                # 城市
            'sex':sex,                      # 性别
            'set_avator':obj.set_avator     # 头像
        })
    overData = {
        'otherData':otherData,
        'obj_count':obj_count
    }
    response.code = 200
    response.msg = '查询成功'
    response.data = {'overData':overData}
    return JsonResponse(response.__dict__)

# 今日增加用户详情
def todayAddUserNumberDetail(request):
    watch_Yesterday = request.GET.get('watchDay')
    print('watch_Yesterday=====> ',watch_Yesterday)
    start_date, stop_date = determineTheTime(watch_Yesterday)
    q = Q()
    print('start_date====> ', start_date, 'stop_date----> ', stop_date)
    q.add(Q(create_date__gte=start_date) & Q(create_date__lte=stop_date), Q.AND)
    objs = models.zhugedanao_userprofile.objects.filter(q)
    obj_count = objs.count()
    current_page = request.GET.get('current_page')
    length = request.GET.get('length')
    if length:
        objs = pagingPage(objs, current_page, length)
    otherData = []
    for obj in objs:
        decode_username = base64.b64decode(obj.username)
        username = str(decode_username, 'utf-8')
        sex = '男'
        if int(obj.sex) == 2:
            sex = '女'
        otherData.append({
            'username':username,            # 用户名
            'country':obj.country,          # 国家
            'province':obj.province,        # 省份
            'city':obj.city,                # 城市
            'sex':sex,                      # 性别
            'set_avator':obj.set_avator,    # 头像
            'create_time':obj.create_date.strftime('%Y-%m-%d %H-%M-%S')   # 创建时间
        })

    overData = {
        'otherData':otherData,
        'obj_count':obj_count
    }
    response.code = 200
    response.msg = '查询成功'
    response.data = {'overData':overData}
    return JsonResponse(response.__dict__)

# 今日活跃用户详情
def todayActiveUsersNumberDetail(request):
    watch_Yesterday = request.GET.get('watchDay')
    start_date, stop_date = determineTheTime(watch_Yesterday)
    q = Q()
    print('start_date====> ',start_date, 'stop_date----> ', stop_date)
    q.add(Q(create_date__gte=start_date) & Q(create_date__lte=stop_date), Q.AND)
    log_objs = models.zhugedanao_oper_log.objects.filter(q)
    objs = log_objs.select_related(
        'user_id'
    ).values(
        'user_id',
    ).distinct()
    objs_count = objs.count()
    current_page = request.GET.get('current_page')
    length = request.GET.get('length')
    print('current_page==========> ',current_page, length)
    if length:
        objs = pagingPage(objs, current_page, length)
    otherData = []
    for obj in objs:
        user_obj = models.zhugedanao_userprofile.objects.filter(id=obj.get('user_id'))
        userObj = user_obj[0]
        sex = '男'
        if int(userObj.sex) == 2:
            sex = '女'
        user_id = obj.get('user_id')
        dataList = []
        objs_gongneng = log_objs.filter(
            user_id=user_id
        ).values(
            'gongneng__name'
        ).distinct()
        for gongneng in objs_gongneng:
            dataList.append(
                gongneng.get('gongneng__name')
            )
        obj_count = objs_gongneng.count()
        decode_username = base64.b64decode(userObj.username)
        username = str(decode_username, 'utf-8')
        otherData.append({
            'objs_count': obj_count,
            'user_id':user_id,
            'create_time':userObj.create_date.strftime('%Y-%m-%d %H-%M-%S'), # 创建时间
            'country':userObj.country,
            'province': userObj.province,       # 省份
            'city': userObj.city,               # 城市
            'sex': sex,                         # 性别
            'set_avator': userObj.set_avator,   # 头像
            'username':username,                # 用户名
            'dataList':dataList,                # 功能


        })
    response.code = 200
    response.msg = '查询成功'
    response.data = {
        'otherData':otherData,
        'objs_count':objs_count
    }
    return JsonResponse(response.__dict__)

# 登录详情
def loginNmberDeatil(request):
    watch_Yesterday = request.GET.get('watchDay')
    start_date, stop_date = determineTheTime(watch_Yesterday)
    q = Q()
    q.add(Q(create_date__gte=start_date) & Q(create_date__lte=stop_date) &(Q(gongneng=1)), Q.AND)
    objs = models.zhugedanao_oper_log.objects.filter(q).values('user_id', 'create_date').distinct().order_by('-create_date')
    obj_count = objs.count()
    otherData = []
    current_page = request.GET.get('current_page')
    length = request.GET.get('length')
    if length:
        objs = pagingPage(objs, current_page, length)
    for obj in objs:
        user_objs = models.zhugedanao_userprofile.objects.filter(id=obj.get('user_id'))
        userObj = user_objs[0]
        sex = '男'
        if int(userObj.sex) == 2:
            sex = '女'
        decode_username = base64.b64decode(userObj.username)
        username = str(decode_username, 'utf-8')
        otherData.append({
            'username':username,
            'create_time':userObj.create_date.strftime('%Y-%m-%d %H-%M-%S'),
            'set_avator':userObj.set_avator,        # 头像
            'country': userObj.country,                 # 国家
            'province': userObj.province,               # 省份
            'city': userObj.city,                       # 城市
            'sex': sex,                                 # 性别
        })
    dataList = {
        'otherData':otherData,
        'obj_count':obj_count
    }
    response.code = 200
    response.msg = '查询成功'
    response.data = {'dataList':dataList}
    return JsonResponse(response.__dict__)








