from django.conf.urls import url


from zhugedanao.views_dir.wechat import wechat
from zhugedanao.views_dir import oper_log
from zhugedanao.views_dir import tongji_data
from zhugedanao.views_dir import lianjie_tijiao, shoulu_chauxn, fugai_chaxun, zhongdianci_jiankong
from zhugedanao.views_dir.Access_tijiaolianjie_task import access_task
from zhugedanao.views_dir.Access_shouluChaxun import shouluchauxn
from zhugedanao.views_dir.Access_fugaiChaxun import fugaichaxun
from zhugedanao.views_dir.Access_zhongDianCiJianKong import zhongdianci
from zhugedanao.views_dir.Access_gonggong import exit_delete
urlpatterns = [

    # url(r'^w_login',login.w_login),
    url(r'^wechat$', wechat.index),                                                              # 微信
    url(r'^wechat_login$', wechat.wechat_login),                                                 # 判断是否登录
    url(r'^generate_qrcode$', wechat.generate_qrcode),                                           # 获取用于登录的微信二维码
    url(r'^oper_log$', oper_log.oper_log),                                                       # 记录使用日志
    url(r'^tongji_data$', tongji_data.tongji_data),                                              # 微信公众号获取统计数据

    # 链接提交
    url(r'^lianjie_tijiao/(?P<oper_type>\w+)/(?P<o_id>\d+)', lianjie_tijiao.lianjie_tijiao_oper),# 操作
    url(r'^lianjie_tijiao_show', lianjie_tijiao.lianjie_tijiao),                                 # 查看任务
    url(r'^detail_lianjie_tijiao/', lianjie_tijiao.lianjie_tijiao_detail),                       # 查看详情
    url(r'^linksToSubmitShouLu', access_task.linksToSubmitShouLu),                               # 收录查看任务
    url(r'^decideIsTask', access_task.decideIsTask),                                             # 判断是否还有任务
    url(r'^tiJiaoLianJieDecideIsTask', access_task.tiJiaoLianJieDecideIsTask),                   # 判断收录是否还有任务
    url(r'^linksShouLuReturnData', access_task.linksShouLuReturnData),                           # 收录返回任务改状态
    url(r'^set_task_access', access_task.set_task_access),                                       # 获取提交链接数据
    url(r'^get_task_for', access_task.get_task_for),                                             # 接收返回的数据并改值
    # url(r'^panduan_shijian', access_task.panduan_shijian),                                     # celery定时判断时间改值30分钟

    # 收录功能
    url(r'^shouLuChaxun/(?P<oper_type>\w+)/(?P<o_id>\d+)', shoulu_chauxn.shouLuChaxun),          # 操作
    url(r'^shouLuChaXunShow', shoulu_chauxn.shouLuChaXunShow),                                   # 查看数据
    url(r'^shouLuChaXunDecideIsTask', shouluchauxn.shouLuChaXunDecideIsTask),                    # 判断是否还有任务
    url(r'^shouluHuoQuRenWu', shouluchauxn.shouluHuoQuRenWu),                                    # 收录获取任务
    url(r'^shouluTiJiaoRenWu', shouluchauxn.shouluTiJiaoRenWu),                                  # 收录返回数据

    # 覆盖功能
    url(r'^fuGaiChaXun/(?P<oper_type>\w+)/(?P<o_id>\d+)', fugai_chaxun.fuGaiChaXun),             # 操作
    url(r'^fuGaiChaxunShow', fugai_chaxun.fuGaiChaxunShow),                                      # 查看数据
    url(r'^fuGaiChaXunDecideIsTask', fugaichaxun.fuGaiChaXunDecideIsTask),                       # 判断是否有任务
    url(r'^fuGaiHuoQuRenWu', fugaichaxun.fuGaiHuoQuRenWu),                                       # 获取任务
    url(r'^fuGaiTiJiaoRenWu', fugaichaxun.fuGaiTiJiaoRenWu),                                     # 返回参数

    # 重点词监控
    url(r'^zhongDianCiOper/(?P<oper_type>\w+)/(?P<o_id>\d+)', zhongdianci_jiankong.zhongDianCiOper),     # 操作
    url(r'^zhongDianCiShowTaskList', zhongdianci_jiankong.zhongDianCiShowTaskList),                      # 查看任务列表
    url(r'^zhongDianCiDetailShowTaskList', zhongdianci_jiankong.zhongDianCiDetailShowTaskList),          # 查看列表详情
    url(r'^zhongDianCiChaXunDecideIsTask', zhongdianci.zhongDianCiChaXunDecideIsTask),                   # 判断是否有任务
    url(r'^HuoQuRenWuzhongDianCi', zhongdianci.HuoQuRenWuzhongDianCi),                                   # 获取任务
    url(r'^TiJiaoRenWuzhongDianCi', zhongdianci.TiJiaoRenWuzhongDianCi),                                 # 返回任务

    # 公共功能
    url(r'^gonggong_exit_delete', exit_delete.gonggong_exit_delete),                                 # 公共删除

]
