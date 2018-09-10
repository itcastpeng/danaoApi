from django.db import models


# Create your models here.


# 权限表
class zhugedanao_quanxian(models.Model):
    path = models.CharField(verbose_name="访问路径", max_length=64)
    icon = models.CharField(verbose_name="图标", max_length=64)
    title = models.CharField(verbose_name="功能名称", max_length=64)
    pid = models.ForeignKey('self', verbose_name="父级id", null=True, blank=True)
    # order_num = models.SmallIntegerField(verbose_name="按照该字段的大小排序")
    create_date = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    component = models.CharField(verbose_name="vue 文件路径", max_length=64, null=True, blank=True)
    oper_user = models.ForeignKey(to='zhugedanao_userprofile', verbose_name='用户', null=True, blank=True)

    class Meta:
        verbose_name_plural = "角色表"
        app_label = "zhugedanao"


# 角色表
class zhugedanao_role(models.Model):
    name = models.CharField(verbose_name="角色名称", max_length=32)
    create_date = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    quanxian = models.ManyToManyField('zhugedanao_quanxian', verbose_name="对应权限")

    class Meta:
        verbose_name_plural = "角色表"
        app_label = "zhugedanao"

    def __str__(self):
        return "%s" % self.name


# 用户级别表
class zhugedanao_level(models.Model):
    name = models.CharField(verbose_name="级别名称", max_length=128)


# 用户信息表
class zhugedanao_userprofile(models.Model):
    status_choices = (
        (1, "启用"),
        (2, "未启用"),
    )
    status = models.SmallIntegerField(choices=status_choices, verbose_name="状态", default=1)
    password = models.CharField(verbose_name="密码", max_length=64, null=True, blank=True)
    username = models.CharField(verbose_name="姓名", max_length=64, null=True, blank=True)

    level_name = models.ForeignKey('zhugedanao_level', verbose_name="用户级别", default=1)
    role = models.ForeignKey("zhugedanao_role", verbose_name="角色", null=True, blank=True)
    create_date = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    last_login_date = models.DateTimeField(verbose_name="最后登录时间", null=True, blank=True)
    token = models.CharField(verbose_name="token值", max_length=32, null=True, blank=True)
    set_avator = models.CharField(verbose_name="头像图片地址", max_length=256, default='statics/imgs/setAvator.jpg')
    openid = models.CharField(verbose_name="微信公众号id", max_length=32)
    timestamp = models.CharField(verbose_name="时间戳", max_length=32, null=True, blank=True)

    sex_choices = (
        (1, '男'),
        (2, '女'),
    )
    sex = models.SmallIntegerField(choices=sex_choices, verbose_name="性别", null=True, blank=True)
    country = models.CharField(verbose_name="国家", max_length=32, null=True, blank=True)
    province = models.CharField(verbose_name="省份", max_length=32, null=True, blank=True)
    city = models.CharField(verbose_name="城市", max_length=32, null=True, blank=True)
    subscribe_time = models.CharField(verbose_name="最后关注时间", max_length=32, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        app_label = "zhugedanao"


# 功能表
class zhugedanao_gongneng(models.Model):
    name = models.CharField(verbose_name="功能名称", max_length=128)
    pid = models.ForeignKey('self', verbose_name="功能父ID，为空表示主功能", null=True, blank=True)
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        app_label = "zhugedanao"


# 功能访问日志表
class zhugedanao_oper_log(models.Model):
    user = models.ForeignKey('zhugedanao_userprofile', verbose_name="用户")
    gongneng = models.ForeignKey('zhugedanao_gongneng', verbose_name='使用功能')
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        app_label = "zhugedanao"


# 百度知道链接提交任务表
class zhugedanao_lianjie_task_list(models.Model):
    task_name = models.CharField(verbose_name="任务名称", max_length=128)
    task_status = models.BooleanField(verbose_name='该任务是否完成', default=False)
    task_progress = models.IntegerField(verbose_name='任务进度', default=0)
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    count_taskList = models.IntegerField(verbose_name='任务总数', default=0)
    is_update = models.BooleanField(verbose_name='是否可以修改', default=0)
    user_id = models.ForeignKey(to='zhugedanao_userprofile', verbose_name='用户', null=True, blank=True)
    shoulu_num = models.IntegerField(verbose_name='任务收录条数', null=True, blank=True, default=0)

    class Meta:
        app_label = "zhugedanao"


# 百度知道链接提交
class zhugedanao_lianjie_tijiao(models.Model):
    # user = models.ForeignKey('zhugedanao_userprofile', verbose_name="用户", null=True, blank=True)
    tid = models.ForeignKey(to='zhugedanao_lianjie_task_list', verbose_name='链接提交百度任务表', null=True, blank=True)
    url = models.TextField(verbose_name="提交链接")
    count = models.SmallIntegerField(verbose_name="提交次数", default=0)
    status_choices = (
        (1, "等待查询"),
        (2, "已收录"),
        (3, "未收录"),
    )
    beforeSubmitStatus = models.SmallIntegerField(verbose_name="提交前收录状态", choices=status_choices, default=1)
    status = models.SmallIntegerField(verbose_name="收录状态", choices=status_choices, default=1)
    # get_task_date = models.DateTimeField(verbose_name='获取任务时间', null=True, blank=True)
    is_zhixing = models.BooleanField(verbose_name='是否执行', default=False)
    time_stamp = models.IntegerField(verbose_name='取任务间隔时间', null=True, blank=True)
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True, null=True, blank=True)
    submit_date = models.DateTimeField(verbose_name='提交时间', null=True, blank=True)
    shoulutime_stamp = models.IntegerField(verbose_name='收录取任务间隔时间', null=True, blank=True)
    # access_task_stamp = models.IntegerField(verbose_name='提交链接获取任务间隔时间', null=True, blank=True)

    class Meta:
        app_label = "zhugedanao"


# 百度知道链接提交日志
class zhugedanao_lianjie_tijiao_log(models.Model):
    zhugedanao_lianjie_tijiao = models.ForeignKey('zhugedanao_lianjie_tijiao', verbose_name="提交的链接信息")
    ip = models.CharField(verbose_name="提交的ip", max_length=128)
    address = models.CharField(verbose_name="提交机器的ip", max_length=128)
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)


# 收录查询表
class zhugedanao_shoulu_chaxun(models.Model):
    is_shoulu = models.IntegerField(verbose_name='是否收录', default=0)
    url = models.CharField(verbose_name='链接', max_length=128)
    time_stamp = models.IntegerField(verbose_name='任务间隔时间', default=0)
    title = models.CharField(verbose_name='网页标题', max_length=64, null=True, blank=True)
    search = models.IntegerField(verbose_name='搜索引擎', default=0)
    kuaizhao_time = models.CharField(verbose_name='快照时间', max_length=64, null=True, blank=True)
    status_code = models.IntegerField(verbose_name='状态码', null=True, blank=True)
    is_zhixing = models.BooleanField(verbose_name='是否已经执行', default=0)
    createAndStart_time = models.DateTimeField(verbose_name='创建和开始时间', auto_now_add=True)
    user_id = models.ForeignKey(to='zhugedanao_userprofile', verbose_name='用户', null=True, blank=True)


# 覆盖查询
class zhugedanao_fugai_chaxun(models.Model):
    keyword = models.CharField(verbose_name='关键词', max_length=64)
    search_engine = models.CharField(verbose_name='搜索引擎', max_length=64, default=0)
    sousuo_guize = models.CharField(verbose_name='搜索规则', max_length=64)
    createAndStart_time = models.DateTimeField(verbose_name='创建和开始时间', auto_now_add=True)
    is_zhixing = models.BooleanField(verbose_name='是否执行', default=False)
    time_stamp = models.IntegerField(verbose_name='任务间隔时间', default=0)
    paiming_detail = models.CharField(verbose_name='总体排名', max_length=64, null=True, blank=True)
    # zhanwei = models.BooleanField(verbose_name='占位', default=False)
    json_detail_data = models.TextField(verbose_name='详情数据 json格式', null=True, blank=True)
    user_id = models.ForeignKey(to='zhugedanao_userprofile', verbose_name='用户', null=True, blank=True)


# 重点词监控 - 总
class zhugedanao_zhongdianci_jiankong_taskList(models.Model):
    qiyong_status = models.BooleanField(verbose_name='是否启用', default=False)
    task_name = models.CharField(verbose_name='任务名称', max_length=128)
    task_jindu = models.IntegerField(verbose_name='任务进度', default=0, null=True, blank=True)
    status_choices = (
        (1, "已查询"),
        (2, "未查询"),
        (3, "正在查询"),
    )
    task_status = models.SmallIntegerField(verbose_name='任务状态', choices=status_choices, default=2)
    search_engine = models.CharField(verbose_name='搜索引擎', max_length=64, default=0)
    mohupipei = models.CharField(verbose_name='模糊匹配', max_length=64)
    is_zhixing = models.BooleanField(verbose_name='是否执行', default=False)
    next_datetime = models.DateTimeField(verbose_name='下一次执行时间', null=True, blank=True)
    task_start_time = models.CharField(verbose_name='任务开始时间', max_length=64, null=True, blank=True)
    user_id = models.ForeignKey(to='zhugedanao_userprofile', verbose_name='用户', null=True, blank=True)


# 重点词监控 列表详情
class zhugedanao_zhongdianci_jiankong_taskDetail(models.Model):
    tid = models.ForeignKey(to='zhugedanao_zhongdianci_jiankong_taskList', verbose_name='任务列表', null=True, blank=True)
    search_engine = models.CharField(verbose_name='搜索引擎', max_length=64, default=0)
    lianjie = models.CharField(verbose_name='链接', max_length=128, null=True, blank=True)
    keyword = models.CharField(verbose_name='关键词', max_length=64, null=True, blank=True)
    mohupipei = models.CharField(verbose_name='模糊匹配', max_length=64)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    task_start_time = models.DateTimeField(verbose_name='任务开始时间', null=True, blank=True)
    is_perform = models.BooleanField(verbose_name='是否执行', default=False)
    time_stamp = models.IntegerField(verbose_name='时间戳', null=True, blank=True)


# 重点词监控 详情数据
class zhugedanao_zhongdianci_jiankong_taskDetailData(models.Model):
    tid = models.ForeignKey(to='zhugedanao_zhongdianci_jiankong_taskDetail', verbose_name='任务列表', null=True, blank=True)
    paiming = models.CharField(verbose_name='排名', max_length=64, default=0)
    is_shoulu = models.BooleanField(verbose_name='收录', default=0)
    create_time = models.DateField(verbose_name='创建时间', null=True, blank=True)


# 平台挖掘  关键词表
class zhugedanao_pingtaiwajue_keyword(models.Model):
    create_time = models.DateTimeField(verbose_name='创建时间', null=True, blank=True)
    search = models.IntegerField(verbose_name='搜索引擎', default=0)
    keyword = models.CharField(verbose_name='关键词', max_length=128, null=True, blank=True)
    user_id = models.ForeignKey(to='zhugedanao_userprofile', verbose_name='用户', null=True, blank=True)
    is_perform = models.BooleanField(verbose_name='是否执行', default=False)
    time_stamp = models.IntegerField(verbose_name='时间戳', null=True, blank=True)
    page_number = models.IntegerField(verbose_name='页码', default=1)


# 平台挖掘  域名表
class zhugedanao_pingtaiwajue_yuming(models.Model):
    create_time = models.DateTimeField(verbose_name='创建时间', null=True, blank=True)
    tid = models.ForeignKey(to='zhugedanao_pingtaiwajue_keyword', verbose_name='关键词列表', null=True, blank=True)
    yuming = models.CharField(verbose_name='域名', max_length=128, null=True, blank=True)
    number = models.IntegerField(verbose_name='域名数量', default=0)


# 百度下拉
class zhugedanao_baiduxiala_chaxun(models.Model):
    keyword = models.CharField(verbose_name='关键词', max_length=128, null=True, blank=True)
    search = models.IntegerField(verbose_name='搜索引擎', default=0)
    xialaci = models.CharField(verbose_name='下拉词', max_length=256, null=True, blank=True)
    is_zhixing = models.BooleanField(verbose_name='是否已经执行', default=0)
    time_stamp = models.IntegerField(verbose_name='任务间隔时间', default=0)
    user_id = models.ForeignKey(to='zhugedanao_userprofile', verbose_name='用户', null=True, blank=True)
    createAndStart_time = models.DateTimeField(verbose_name='创建和开始时间', auto_now_add=True)


# 关键词排名查询
class zhugedanao_guanjianci_paiming_chaxun(models.Model):
    search_engine = models.CharField(verbose_name='搜索引擎', max_length=64, default=0)
    is_perform = models.BooleanField(verbose_name='是否执行', default=False)
    time_stamp = models.IntegerField(verbose_name='时间戳', null=True, blank=True)
    keyword = models.CharField(verbose_name='关键词', max_length=64, null=True, blank=True)
    lianjie = models.CharField(verbose_name='链接', max_length=128, null=True, blank=True)
    user_id = models.ForeignKey(to='zhugedanao_userprofile', verbose_name='用户', null=True, blank=True)
    paiming = models.IntegerField(verbose_name='链接排名', default=0)
