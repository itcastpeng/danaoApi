from django.conf.urls import url


from zhugedanao.views_dir.wechat import wechat
from zhugedanao.views_dir import oper_log
from zhugedanao.views_dir import tongji_data
from zhugedanao.views_dir import lianjie_tijiao, shoulu_chauxn, fugai_chaxun
from zhugedanao.views_dir.Access_tijiaolianjie_task import access_task
urlpatterns = [

    # url(r'^w_login',login.w_login),
    url(r'^wechat$', wechat.index),                                                              # 微信
    url(r'^wechat_login$', wechat.wechat_login),                                                 # 判断是否登录
    url(r'^generate_qrcode$', wechat.generate_qrcode),                                           # 获取用于登录的微信二维码
    url(r'^oper_log$', oper_log.oper_log),                                                       # 记录使用日志
    url(r'^tongji_data$', tongji_data.tongji_data),                                              # 微信公众号获取统计数据

    url(r'^lianjie_tijiao_show', lianjie_tijiao.lianjie_tijiao),                                      # 提交链接 - 查看任务
    url(r'^detail_lianjie_tijiao/', lianjie_tijiao.lianjie_tijiao_detail),                       # 提交链接 - 查看详情
    url(r'^lianjie_tijiao/(?P<oper_type>\w+)/(?P<o_id>\d+)', lianjie_tijiao.lianjie_tijiao_oper),# 提交链接 - 操作
    url(r'^decideIsTask', access_task.decideIsTask),                                             # 提交链接 - 判断是否还有任务
    url(r'^set_task_access', access_task.set_task_access),                                       # 提交链接 - 获取提交链接数据
    url(r'^get_task_for', access_task.get_task_for),                                             # 提交链接 - 接收返回的数据并改值
    url(r'^panduan_shijian', access_task.panduan_shijian),                                             # 提交链接 - 接收返回的数据并改值

    url(r'^shouLuChaxun/(?P<oper_type>\w+)/(?P<o_id>\d+)', shoulu_chauxn.shouLuChaxun),          # 收录查询 - 操作
    url(r'^shouLuChaXunShow', shoulu_chauxn.shouLuChaXunShow),                                   # 收录查询 - 查看数据
    url(r'^shouluHuoQuRenWu', access_task.shouluHuoQuRenWu),                                     # 收录查询 - 查看数据


    url(r'^fuGaiChaXun/(?P<oper_type>\w+)/(?P<o_id>\d+)', fugai_chaxun.fuGaiChaXun),             # 覆盖查询 - 操作
    url(r'^fuGaiChaxunShow', fugai_chaxun.fuGaiChaxunShow),                                      # 覆盖查询 - 查看数据


]
