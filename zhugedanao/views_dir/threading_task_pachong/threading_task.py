import sqlite3, os, sys, json, re, time
from time import sleep
import threading
from django.db.models import Q
from zhugedanao.views_dir.threading_task_pachong import zhongzhuanqi
from zhugedanao import models

# 运行程序 - 收录查询
def shoulu_func(user_id, len_url):
    print('进入-------')
    q = Q()
    while True:
        now_time = int(time.time())
        time_stamp = now_time + 20
        q.add(Q(is_zhixing=0) & Q(user_id_id=user_id), Q.AND)
        q.add(Q(time_stamp__isnull=True) | Q(time_stamp__lte=time_stamp), Q.AND)
        objs = models.zhugedanao_shoulu_chaxun.objects.filter(q)
        for obj_data in objs:
            tid = obj_data.id
            search = obj_data.search
            lianjie = obj_data.url

            if threading.active_count() <= 6:
                obj_data.time_stamp = time_stamp
                obj_data.save()

                threadObj = threading.Thread(target=zhongzhuanqi.shouluChaxun, args=(lianjie, user_id, search))
                threadObj.start()
            else:
                sleep(0.5)
                continue
        zhixing_objs = objs.filter(is_zhixing=1)
        zhixing_obj_count = zhixing_objs.count()
        if zhixing_obj_count == len_url:
            break

# 运行程序 - 覆盖查询
def fugai_func(huoqu_fugai_time_stamp, set_keyword_data):
    while True:
        now_time = int(time.time())
        time_stamp = now_time + 30
        sql = """select * from fugai_Linshi_List where is_zhixing = '0' and time_stamp='{huoqu_fugai_time_stamp}' and (shijianchuo < '{time_stamp}' or  shijianchuo is NULL) limit 1;""".format(
            huoqu_fugai_time_stamp=huoqu_fugai_time_stamp,
            time_stamp=now_time)
        objs_data = database_create_data.operDB(sql, 'select')
        for obj_data in objs_data['data']:
            tid = obj_data[0]
            search = obj_data[2]
            mohu_pipei = obj_data[3]
            keyword = obj_data[10]
            if threading.active_count() <= 6:
                # 更改数据库时间戳 二十秒可执行下一次
                sql = """update fugai_Linshi_List set shijianchuo ='{time_stamp}' where id = '{id}';""".format(
                    time_stamp=time_stamp, id=tid)
                database_create_data.operDB(sql, 'update')
                # 启动线程
                fugai_thread4 = threading.Thread(target=zhongzhuanqi.fugaiChaxun,
                        args=(tid, search, keyword, mohu_pipei, huoqu_fugai_time_stamp))
                fugai_thread4.start()
            else:
                sleep(0.5)
                continue
        count_sql = """select count(id) from fugai_Linshi_List where is_zhixing = '1' and time_stamp='{huoqu_fugai_time_stamp}';""".format(
            huoqu_fugai_time_stamp=huoqu_fugai_time_stamp
        )
        count_objs = database_create_data.operDB(count_sql, 'select')
        if count_objs['data'][0][0] == set_keyword_data:
            break

