
#### code 说明：
```
200 正常

300 已存在
301 数据类型验证失败
302 对应ID不存在
303 form 验证错误
304 含有子级数据,请先删除或转移子级数据
305 不允许删除自己
306 账户未启用

401 账号密码错误
402 请求方式异常 例如应该使用 POST 请求的使用的是 GET 请求
403 无任务
404 非法请求
405 扫码登录异常，请重新扫描

```


#### 获取链接提交任务 说明：

``` 
http请求方式: GET
http请求url http://127.0.0.1:8000/zhugedanao/set_task_access
参数   				请求方式		        是否必须            说明
公共参数
返回说明 （正常时返回的json数据 示例）
{
    "code": 200,
    "msg": "查询成功",
    "data": {
        "data_list": [
            {
                "url": "56465465156",           # url
                "o_id": 94,                     # url id 
                "tid": 15                       # 父级id
            },
        ]
    }
}
```

#### 获取返回完成链接提交 说明：

``` 
http请求方式: GET
http请求url： http://127.0.0.1:8000/zhugedanao/get_task_for?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11&urlId=94
参数   				请求方式		        是否必须            说明
urlId               GET                 是                 提交完成的url id

返回说明 （正常时返回的json数据 示例）
{
    "msg": "请求成功",
    "data": {},
    "code": 200
}
```

#### 链接提交 增加任务 说明:
``` 
http请求方式： POST
http请求url： http://127.0.0.1:8000/zhugedanao/lianjie_tijiao/add/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			请求方式		是否必须 		        说明
user_id			GET					是 		    用户id  token中获取 
name 			POST				是 			任务名称
url		        POST				是 			任务链接
o_id            GET                 否           可写为0 添加指定id

返回说明 （正常时返回的json数据 示例）
{
    "data": {},
    "code": 200,
    "msg": "添加成功"
}
```

#### 链接提交 修改任务前 获取数据 说明：
``` 
http请求方式： POST
http请求url： http://127.0.0.1:8000/zhugedanao/lianjie_tijiao/update_show_data/15?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			请求方式		是否必须 		        说明

返回说明 （正常时返回的json数据 示例）

```

#### 链接提交 修改任务 说明：
``` 
http请求方式： POST
http请求url:  http://127.0.0.1:8000/zhugedanao/lianjie_tijiao/update_task/15?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11&o_id=2
参数   			请求方式		是否必须 		        说明
o_id            GET         是                   要修改的id
name            POST        否                   要修改的任务名字
url             POST        否                   要修改的url

返回说明 （正常时返回的json数据 示例）
{
    "msg": "修改成功",
    "data": {},
    "code": 200
}
```

#### 链接提交 展示任务列表 说明：
``` 
http请求方式： GET
http请求url:  http://127.0.0.1:8000/zhugedanao/lianjie_tijiao_show?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			请求方式		是否必须 		        说明

返回说明 （正常时返回的json数据 示例）
{
    "msg": "查询成功",
    "data": {
        "ret_data": [                       
            {
                "yiwancheng_obj": 0,                        # 已完成数量
                "task_name": "任务列表1",                    # 任务名字
                "task_progress": 0,                         # 任务进度
                "task_status": "未完成",                     # 任务状态
                "create_date": "2018-08-16 11:00:24",       # 创建时间
                "is_update": 1,                             # 是否可以修改和删除 1不可以 0可以
                "id": 16,                                   # 任务id
                "count_taskList": 3                         # 详情数据数量
            },
        ],
        "data_count": 1                                     任务列表总数
    },
    "code": 200
}
```

#### 链接提交 展示任务详情数据 说明：
``` 
http请求方式： GET
http请求url： http://127.0.0.1:8000/zhugedanao/detail_lianjie_tijiao?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11&tid=15
参数   			请求方式		是否必须 		        说明
tid             GET         是                   父级id

返回说明 （正常时返回的json数据 示例）
{
    "data": {
        "data_count": 1,                        # 详情总数
        "ret_data": [
            {
                "url": "fdg",                   # 详情url
                "status_text": "等待查询",       # 详情状态
                "id": 106,                      # 详情id
                "count": 0                      # 详情提交次数
            },
        ]
    },
    "msg": "查询成功",
    "code": 200
}
```


#### 收录查询 添加任务 说明：
``` 
http请求方式： POST
http请求url： http://127.0.0.1:8000/zhugedanao/shouLuChaxun/add/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			请求方式		是否必须 		        说明
search_list       POST      是                  搜索引擎
url_list          POST      是                  需要操作的链接

返回说明 （正常时返回的json数据 示例）
{
    "code": 200,
    "msg": "添加成功",
    "data": {}
}
```

#### 收录查询 点击返回 说明：
``` 
http请求方式： GET 
http请求url： http://127.0.0.1:8000/zhugedanao/shouLuChaxun/clickReturn/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			请求方式		是否必须 		        说明
无

返回说明 （正常时返回的json数据 示例）
{
    "msg": "退出成功",
    "data": {},
    "code": 200
}
```

#### 收录查询 生成excel表格 说明：
``` 
http请求方式： GET
http请求url： http://127.0.0.1:8000/zhugedanao/shouLuChaxun/generateExcel/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			请求方式		是否必须 		        说明
无

返回说明 （正常时返回的json数据 示例）
{
    "data": {
        "excel_name": "171534405338"            # 随机生成时间戳名字(随机数 + 时间戳)
    },
    "msg": "生成成功",
    "code": 200
}
```

#### 收录查询 展示所有数据 说明：
``` 
http请求方式： GET
http情求url： http://127.0.0.1:8000/zhugedanao/shouLuChaXunShow?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			请求方式		是否必须 		        说明
difference_status  GET      否               difference_status 为0只看已收录 为1只看未收录

返回说明 （正常时返回的json数据 示例）
{
    "msg": "查询成功",
    "code": 200,
    "data": {
        "yiwancheng_obj": 68,               # 已完成百分比
        "whether_complete": false,          # 是否全部完成 
        "chongfu_num": 5,                   # 重复数
        "shoulushu": 30,                    # 已收录数量
        "count_obj": 32,                    # 数据总数
        "shoululv": 100,                    # 收录率
        query_progress: 90                  # 进度条
        "data": [
            {
                "title": "大连新华美天周年庆变美抄底1折起  消费多少送多少_整形科_求医新闻-医学健康新闻-求医网",
                "statusCode": 200,
                "kuaizhao_date": "2017-12-4",
                "website": "http://news.qiuyi.cn/html/2017/zhengxing_1204/63922.html",
                "search_engine": "百度",
                "shoulu_status": "未收录"
            }
        ]
    }
}}
```


#### 覆盖查询 展示所有数据 说明：
``` 
http请求方式： GET
http情求url： http://127.0.0.1:8000/zhugedanao/fuGaiChaxunShow?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			请求方式		是否必须 		        说明
无

返回说明 （正常时返回的json数据 示例）
{
    "data": {
        "retData": [
            {
                "rank_num": 9,
                "rank_info": "1,2,3,4,5,6,7,8,9",
                "keyword": "合众康桥",
                "id": 129,
                "otherData": "[{'keyword': '合众康桥', 'url': 'http://www.baidu.com/link?url=slwxEwjledOJxW-PRPUQp9H5Ww_4m4t4ba1vViNiezLZ6YcWWS16A54hXfjGvbBC', 'guize': '合众康桥', 'search_engine': '1', 'zhanwei': 1, 'title': '北京合众康桥,互联网整合营销服务商', 'rank': 1}, {'keyword': '合众康桥', 'url': 'http://www.baidu.com/link?url=WULtmrY8RfkBGM2Fll1B0mkglLZSh8zAOAKQsQlH16W2Wqgwo4D9GIott0vMRkdegSLEtddu9T9ivdeYHzQPoq', 'guize': '合众康桥', 'search_engine': '1', 'zhanwei': 1, 'title': '北京合众康桥 - 熊掌号', 'rank': 2}, {'keyword': '合众康桥', 'url': 'http://www.baidu.com/link?url=sfzDaK5QUWMfe2gI3XvoYEVD-CLtOXgEVZDYrTFTOLXEFJnnhg4VHWCPNvaf28ADqEp3TFfcgty4FV3IGjZVWeY_6Ivr2wkhxTB9BSwjxhO', 'guize': '合众康桥', 'search_engine': '1', 'zhanwei': 1, 'title': '合众康桥王美平这个人怎么样_百度知道', 'rank': 3}, {'keyword': '合众康桥', 'url': 'http://www.baidu.com/link?url=6ROvZ8hUPsZUbNiE_HIL5Rmc601KysPUnVo6oozV0OqeldFgySDVWwbrnWr1K4Lw42z7TsNVtJtFoDDxhzRLreibCIurZf8NY4fitlfLiQEjwVOJ140ZAcWlzPIDrLuOSCOVC-5-qzxo-Z39qhstFrWf5Fe3aFbHxPmu2fIXisIwQZshBrrW9TyfzCva9CI6ldUqbF7gX0Z59vUyeYoqmien2AYDO0BJkTjsbsJxzGK', 'guize': '合众康桥', 'search_engine': '1', 'zhanwei': 1, 'title': '北京合众康桥科技发展有限公司_百度百科', 'rank': 4}, {'keyword': '合众康桥', 'url': 'http://www.baidu.com/link?url=C7CiISWQMQOen2cGe-QSVaDoH2A7qpa3eXyf89HD3dC85ih6dHlC0muVm12lq-EBfMduYeDuMWF2O6n45m48Rq', 'guize': '合众康桥', 'search_engine': '1', 'zhanwei': 1, 'title': '合众康桥王美平_Tencent Weibo', 'rank': 5}, {'keyword': '合众康桥', 'url': 'http://www.baidu.com/link?url=bFqPjvct2HHiM1pjmTE50gaESLhx9CxKzgl_Hj1SWWAXEKTB6P2PdGuMmJBXclsxyLrR4Vi6cxwhwuFGqcnyf_', 'guize': '合众康桥', 'search_engine': '1', 'zhanwei': 1, 'title': '北京合众康桥科技发展有限公司怎么样? - 职友集(一家做公司点评的...', 'rank': 6}, {'keyword': '合众康桥', 'url': 'http://www.baidu.com/link?url=yujgxkipq_MjE_6mR6uF_6V5NrXVWK3aPvGbQGwKvTXTn-w1sMXs7yzzStAmLb4MQ4AjCDR8DyAKZ8aZ4mh8vK', 'guize': '合众康桥', 'search_engine': '1', 'zhanwei': 1, 'title': '【北京合众康桥科技发展有限公司2018招聘信息】_猎聘网', 'rank': 7}, {'keyword': '合众康桥', 'url': 'http://www.baidu.com/link?url=EecZEVbfUOIWYlsWoDHOMgAlTWvKTF9fc9EipefjEiRIF8YL3006HuVybfMwvn7CRzjTgLqkEyBDKS791vUZwK', 'guize': '合众康桥', 'search_engine': '1', 'zhanwei': 1, 'title': '【合众康桥怎么样?】-看准网', 'rank': 8}, {'keyword': '合众康桥', 'url': 'http://www.baidu.com/link?url=jb4ziul5ijXkINheL11CcpXEim12yXhwylduyb99tJVOEPKyUS5gvqAyE_bQV2m9', 'guize': '合众康桥', 'search_engine': '1', 'zhanwei': 1, 'title': '【合众康桥_合众康桥招聘】北京合众康桥科技发展有限公司..._拉勾网', 'rank': 9}]",
                "search_engine": "百度"
            },
        ],
        "query_progress": 20,
        "whether_complete": false,
        "dataCount": 6,
        "yiwancheng_obj": 100,
        "chongfu_num": 10,
        "paiminglv": 100,
        "fugailv": 90,
        "paiming_num": 6
    },
    "code": 200,
    "msg": "查询成功"
}
```

#### 覆盖查询 添加任务 说明：
``` 
http请求方式： POST
http请求url： http://127.0.0.1:8000/zhugedanao/fuGaiChaXun/add/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		        说明
searchEngineModel       POST                是                 搜索引擎
editor_content          POST                是                 关键词
fugai_tiaojian          POST                是                 搜索条件

返回说明 （正常时返回的json数据 示例）
{
    "data": {},
    "code": 200,
    "msg": "添加成功"
}
```

#### 覆盖查询 退出 说明：
``` 
http请求方式： GET
http请求url： http://127.0.0.1:8000/zhugedanao/fuGaiChaXun/clickReturn/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		        说明
无

返回说明 （正常时返回的json数据 示例）
{
    "msg": "退出成功",
    "data": {},
    "code": 200
}
```

#### 覆盖查询 生成覆盖excel 说明：
``` 
http请求方式： GET
http请求url： http://127.0.0.1:8000/zhugedanao/fuGaiChaXun/generateExcel/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		        说明
无

返回说明 （正常时返回的json数据 示例）
{
    "msg": "生成成功",
    "data": {
        "excel_name": "941534492426"
    },
    "code": 200
```

#### 重点词监控 查询列表页 说明
``` 
http请求方式： GET
http请求url： http://127.0.0.1:8000/zhugedanao/zhongDianCiShowTaskList?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		        说明
公共参数
返回说明 （正常时返回的json数据 示例）
{
    "data": {
        "data_list": [
            {
                "id": 16,                           任务id
                "task_name": "任务",                 任务名称
                "qiyong_status": true,              启用状态
                "task_jindu": 0,                    任务进度
                "task_start_time": "07:50:20",      任务开始时间
                "is_zhixing":1                      是否执行      0代表未执行 显示修改   1代表执行 显示转圈
                "search_engine": [                  搜索引擎
                    "1",
                    "3"
                ],
                "task_status": 3                    任务状态 0已查询 1未查询 3正在查询 
            }
        ]
    },
    "msg": "查询成功",
    "code": 200
}
```

#### 重点词监控 查询详情页 说明
``` 
http请求方式： GET
http请求url：  http://127.0.0.1:8000/zhugedanao/zhongDianCiDetailShowTaskList?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11&tid=16
参数   			        请求方式		        是否必须 		        说明
公共参数                
tid                     GET                 是                   任务列表id

返回说明 （正常时返回的json数据 示例）
 {
    "data": {
        "data_list": [
            {
                "id": 49,                                   详情id
                "create_time": "2018-08-21T20:09:34",       创建时间
                "search_engine": "1",                       搜索引擎
                "lianjie": "http://www.bjhzkq.com",         链接
                "keywords": "合众康桥",                      关键词
                "mohupipei": "",                            模糊匹配条件
                "tid": 16                                   父级id
            }
        ],
                "count": 4                                  总数
    },
    "msg": "查询成功",
    "code": 200
}
```

#### 重点词监控 添加任务 说明
``` 
http请求方式： POST
http请求url：  http://127.0.0.1:8000/zhugedanao/zhongDianCiOper/add/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		        说明
qiyong_status           POST                是                   启用状态
task_name               POST                是                   任务名称
task_jindu              POST                是                   任务进度
task_start_time         POST                是                   任务开始时间
search_engine           POST                是                   搜索引擎
mohupipei               POST                否                   模糊匹配条件
keywords                POST                是                   关键词 or (关键词 and 链接)
task_status             POST                是                   任务状态

返回说明 （正常时返回的json数据 示例）
{
    "data": {},
    "msg": "添加成功",
    "code": 200
}
```

#### 重点词监控 修改任务前查询 说明
``` 
http请求方式： POST
http请求url：  http://127.0.0.1:8000/zhugedanao/zhongDianCiOper/update_show/17?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		        说明

返回说明 （正常时返回的json数据 示例）
{
    "msg": "修改查询成功",
    "code": 200,
    "data": {
        "task_name": "任务",
        "task_start_time": "07:50:20"
    }
}
```

#### 重点词监控 确认修改 说明
``` 
http请求方式：  POST
http请求url： http://127.0.0.1:8000/zhugedanao/zhongDianCiOper/update/17?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11 
参数   			        请求方式		        是否必须 		        说明
task_name               POST                  否                 任务名称
task_start_time         POST                  否                 任务开始时间

返回说明 （正常时返回的json数据 示例）
{
    "msg": "修改成功",
    "code": 200,
    "data": {}
}
```

#### 重点词监控 删除任务 说明
``` 
http请求方式： POST
http请求url： http://127.0.0.1:8000/zhugedanao/zhongDianCiOper/delete/16?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		        说明
id_list                 POST                是                  要删除的任务id列表
返回说明 （正常时返回的json数据 示例）
{
    "data": {},
    "code": 200,
    "msg": "删除成功"
}
```

#### 重点词监控 清空任务详情 说明
``` 
http请求方式： POST
http请求url：  http://127.0.0.1:8000/zhugedanao/zhongDianCiOper/empty/16?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		        说明
id                      url                 是                   要清空的详情的列表id

返回说明 （正常时返回的json数据 示例）
{
    "data": {},
    "code": 200,
    "msg": "清空成功"
}
```

#### 重点词监控 生成excel表格 说明
``` 
http请求方式： POST
http请求url： http://127.0.0.1:8000/zhugedanao/zhongDianCiOper/generateExcel/17?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11     
参数   			        请求方式		        是否必须 		        说明
id                      url                 是                   任务列表id

返回说明 （正常时返回的json数据 示例）
{
    "msg": "生成成功",      
    "data": {
        "excel_name": "http://api.zhugeyingxiao.com/statics\\zhugedanao\\zhongDianCiExcel\\任务阿萨德_1534916204.xlsx"   
    },                  生成excel表格 路径 ↑ 
    "code": 200
}
```

#### 重点词监控  立即监控 说明
``` 
http请求方式： GET
http请求url： http://127.0.0.1:8000/zhugedanao/zhongDianCiChaXunLiJiJianKong?id_list=[28,2]
参数   			        请求方式		        是否必须 		        说明
id_list                 GET                 是                   要监控的id列表

返回说明 （正常时返回的json数据 示例）
{
    "msg": "监控成功",
    "data": {},
    "code": 200
}
```

#### 公共删除功能 说明
``` 
http请求方式： GET
http请求url：  http://127.0.0.1:8000/zhugedanao/gonggong_exit_delete?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		        说明
公共参数

返回说明 （正常时返回的json数据 示例）
{
    "code": 200,
    "msg": "退出成功",
    "data": {}
}
```




















