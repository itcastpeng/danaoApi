
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


#### 平台挖掘 查询 说明
``` 
http请求方式 GET
http请求url:  http://127.0.0.1:8000/zhugedanao/pingTaiWaJueShow?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		        说明
公共参数

返回说明 （正常时返回的json数据 示例）
{
    "data": {
        "exet_data": {
            "data": [
                {
                    "number": 3,
                    "yuming": "w.huanqiu.com"                   
                    "yinqing": "百度"
                },          
            ],
            "objs_count": 26
        }
    },
    "code": 200,
    "msg": "查询成功"
}
```

#### 平台挖掘 添加 说明
``` 
http请求方式 POST
http请求url： http://127.0.0.1:8000/zhugedanao/pingTaiWaJue/add/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		        说明
keywords                POST                 是                  要查询的关键词
search                  POST                 否                  默认为百度
page_number             POST                 否                  页码 默认为1

返回说明 （正常时返回的json数据 示例）
{
    "data": {},
    "code": 200,
    "msg": "添加成功"
}
```

#### 平台挖掘 退出 删除任务 说明
``` 
http请求方式 GET
http请求url： http://127.0.0.1:8000/zhugedanao/pingTaiWaJue/clickReturn/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		        说明
公共参数

返回说明 （正常时返回的json数据 示例）
{
    "data": {},
    "msg": "退出成功",
    "code": 200
}
```

#### 平台挖掘 生成excel表格 说明
``` 
http请求方式 GET
http请求url： http://127.0.0.1:8000/zhugedanao/pingTaiWaJue/generateExcel/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		        说明
公共参数

返回说明 （正常时返回的json数据 示例）
{
    "data": {
        "excel_name": "http://api.zhugeyingxiao.com/statics\\zhugedanao\\pingTaiWaJueExcel\\381535354045.xlsx"  下载地址
    },
    "msg": "生成成功",
    "code": 200
}
```

#### 平台挖掘 计算处理 说明
``` 
http请求方式 GET
http请求url：  http://127.0.0.1:8000/zhugedanao/pingTaiWaJue/finalResult/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		        说明
公共参数

返回说明 （正常时返回的json数据 示例）
{
    "data": {},
    "msg": "计算结果完成",
    "code": 200
}
```


#### 百度下拉 查询 说明
``` 
http请求方式 GET
http请求url:  http://127.0.0.1:8000/zhugedanao/baiDuXiaLaShow?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		        说明
公共参数

返回说明 （正常时返回的json数据 示例）
{
    "msg": "查询成功",
    "data": {
        "yiwancheng_obj": 1,                        已完成数量
        "obj_count": 1,                             下拉词总数
        "retData": [
            {
                "otherData": [                      下拉词
                    "北京合众康桥"
                ],
                "search": 1,                        搜索引擎
                "keyword": "合众康桥"                 关键词
            },
            {
                "otherData": "",
                "search": 4,
                "keyword": "合众康桥"
            }
        ],
        "whether_complete": false,                  是否完成
        "query_progress": 50,                       进度条
        "keyword_count": 2                          关键词总数
    },
    "code": 200                                     状态码
}
```

#### 百度下拉 添加 说明
``` 
http请求方式 POST
http请求url:  http://127.0.0.1:8000/zhugedanao/baiDuXiaLa/add/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		         说明
editor_content          POST                是                   关键词
searchEngineModel       POST                是                   搜索引擎

返回说明 （正常时返回的json数据 示例）
{
    "code": 200,
    "data": {},
    "msg": "添加成功"
}
```

#### 关键词排名 添加 说明
``` 
http请求 POST
http请求url：  http://127.0.0.1:8000/zhugedanao/guanJianCiMaiMingOper/add/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		         说明
search_engine           POST                是                   搜索引擎
keywords                POST                是                   关键词

返回说明 （正常时返回的json数据 示例）
{
    "msg": "添加成功",
    "code": 200,
    "data": {}
}
```

#### 关键词排名 查询 说明
``` 
http请求 GET
http请求url：   http://127.0.0.1:8000/zhugedanao/guanJianCiMaiMingShow?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		         说明
无

返回说明 （正常时返回的json数据 示例）
{
    "data": {
        "other_data": {
            "whether_complete": true,                                               是否完成
            "chongfu_num": 0,                                                       重复数
            "yiwancheng_obj": 4,                                                    已完成数量
            "data_list": [                                                          
                {
                    "paiming": 1,                                                   排名  
                    "lianjie": "http://focus.smxe.cn/20171204/148l",                链接
                    "keyword": "天津美莱双眼皮埋线好不好 美莱暖冬计划启动中",              关键词
                    "search": "1"                                                   搜索引擎
                },
                {
                    "paiming": "-",
                    "lianjie": "http://news.360xh.com/201712/04/37408.html",
                    "keyword": "昆明宝岛妇产医院有去过的吗？奋勇争先，情系健康",
                    "search": "1"
                },
                {
                    "paiming": "-",
                    "lianjie": "http://focus.smxe.cn/20171204/148l",
                    "keyword": "天津美莱双眼皮埋线好不好 美莱暖冬计划启动中",
                    "search": "4"
                },
                {
                    "paiming": "-",
                    "lianjie": "http://news.360xh.com/201712/04/37408.html",
                    "keyword": "昆明宝岛妇产医院有去过的吗？奋勇争先，情系健康",
                    "search": "4"
                }
            ],
            "query_progress": 100,                                                  进度
            "obj_count": 4                                                          数据总数
        }
    },
    "msg": "查询成功",
    "code": 200
}
```

#### 关键词排名 退出 说明
``` 
http请求 GET
http请求url： http://127.0.0.1:8000/zhugedanao/guanJianCiMaiMingOper/clickReturn/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		         说明
无

返回说明 （正常时返回的json数据 示例）
{
    "msg": "退出成功",
    "code": 200,
    "data": {}
}
```

#### 关键词排名 生成excel 说明
``` 
http请求 GET
http请求 url：       http://127.0.0.1:8000/zhugedanao/guanJianCiMaiMingOper/generateExcel/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		         说明
无

返回说明 （正常时返回的json数据 示例）
{
    "msg": "生成成功",                          
    "data": {                                       生成的路径名↓
        "excel_name": "http://api.zhugeyingxiao.com/statics\\zhugedanao\\zhongDianCiExcel\\161536205504.xlsx"
    },
    "code": 200
}
```


#### 权限添加 说明
``` 
http请求  POST    
http请求url：  http://127.0.0.1:8000/zhugedanao/permissions_oper/add/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		         说明
title                   POST                是                   权限名称
pid_id                  POST                否                   父级权限id
user_id                 POST                是                   操作人id

返回说明 （正常时返回的json数据 示例）
{
    "code": 200,
    "msg": "添加成功",
    "data": {}
}                
```

#### 权限删除 说明
``` 
http请求 POST
http请求url：  http://127.0.0.1:8000/zhugedanao/permissions_oper/delete/3?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		         说明
id                      url                 是                   要删除的id

返回说明 （正常时返回的json数据 示例）
{
    "msg": "删除成功",
    "code": 200,
    "data": {}
}
``` 

#### 权限修改 说明
``` 
http请求 POST 
http请求url：     http://127.0.0.1:8000/zhugedanao/permissions_oper/update/2?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		         说明
title                   POST                是                   权限标题
pid_id                  POST                是                   权限id

返回说明 （正常时返回的json数据 示例）
{
    "msg": "修改成功",
    "code": 200,
    "data": {}
}
```

 #### 权限查询 说明
``` 
http请求  GET
http请求url：  http://127.0.0.1:8000/zhugedanao/permissionsShow?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		         说明
无

返回说明 （正常时返回的json数据 示例）
{
    "data": {
        "data_count": 3,
        "ret_data": [
            {
                "id": 4,
                "pid_title": "百度",
                "oper_user__username": "",
                "pid_id": 1,
                "title": "百度",
                "create_date": "2018-09-10 10:43:01"
            },
            {
                "id": 2,
                "pid_title": "360",
                "oper_user__username": "",
                "pid_id": 2,
                "title": "360",
                "create_date": "2018-09-10 10:37:21"
            },
            {
                "id": 1,
                "pid_title": "",
                "oper_user__username": "",
                "pid_id": null,
                "title": "百度",
                "create_date": "2018-09-10 10:21:42"
            }
        ]
    },
    "msg": "查询成功",
    "code": 200
}
```

#### 权限树状图 说明
``` 
http请求  GET
http请求url： http://127.0.0.1:8000/zhugedanao/permissions_oper/get_tree_data/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		         说明
无

返回说明 （正常时返回的json数据 示例）
{
    "data": {
        "ret_data": "[{\"id\": 1, \"expand\": true, \"title\": \"\\u767e\\u5ea6\", \"checked\": false, \"children\": [{\"id\": 5, \"expand\": true, \"title\": \"\\u767e\\u5ea6\", \"checked\": false}, {\"id\": 6, \"expand\": true, \"title\": \"\\u767e\\u5ea6\", \"checked\": false}]}, {\"id\": 7, \"expand\": true, \"title\": \"\\u91cd\\u70b9\\u8bcd\\u76d1\\u63a7\", \"checked\": false}]"
    },
    "code": 200,
    "msg": "获取tree数据成功"
}
```


#### 角色管理添加 说明
``` 
http请求 POST 
http请求url：  http://127.0.0.1:8000/zhugedanao/roleManagementOper/add/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		         说明
role_name               POST                是                   角色名称
quanxian_list           POST                否                   角色权限 数组id

返回说明 （正常时返回的json数据 示例）
{
    "code": 200,
    "msg": "添加成功",
    "data": {}
}
```

#### 角色查询树状图 说明
``` 
http请求 GET
http请求url：  http://127.0.0.1:8000/zhugedanao/roleManagementOper/get_rules/36?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		         说明
o_id                    URL                 是                   要查询树状图的id

返回说明 （正常时返回的json数据 示例）
{
    "code": 200,
    "msg": "查询成功",
    "data": {
        "rules_list": [
            "百度",
            "360"
        ]
    }
}
```

#### 角色管理修改 说明
``` 
http请求： POST 
http请求url：  http://127.0.0.1:8000/zhugedanao/roleManagementOper/afterUpdate/35?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		         说明
o_id                    URL                 是                   要修改的角色id
roleName                POST                是                   要修改的名字
permissionList          POST                否                   要修改的权限

返回说明 （正常时返回的json数据 示例）
{
    "data": {},
    "code": 200,
    "msg": "修改成功"
}
```

#### 角色管理删除 说明
``` 
http请求：POST 
http请求url：  http://127.0.0.1:8000/zhugedanao/roleManagementOper/delete/35?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		         说明
o_id                    URL                 是                   要删除的角色ID

返回说明 （正常时返回的json数据 示例）
{
    "data": {},
    "code": 200,
    "msg": "删除成功"
}
```

#### 角色管理查询 说明
``` 
http请求： GET
http请求url：  http://127.0.0.1:8000/zhugedanao/roleManagementShow?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		         说明
无

返回说明 （正常时返回的json数据 示例）
{
    "data": {
        "roleCount": 1,                                 # 查询个数
        "retData": [    
            {
                "permissionsData": [
                    {
                        "checked": true,                # 是否选中
                        "id": 1,                        # 权限ID
                        "expand": true,                 # 是否展开
                        "title": "百度",                 # 权限名称 
                        "children": [                   # 子级
                            {
                                "checked": false,       # 是否选中
                                "id": 5,                # 子级权限ID
                                "expand": true,         # 是否展开
                                "title": "百度"         # 子级权限名称 
                            }
                        ]
                    }
                ],
                "id": 37,                               # 角色ID
                "name": "管理员",                        # 角色名称 
                "createDate": "2018-09-11T10:23:50"     # 创建时间
            }
        ]
    },
    "code": 200,                                       
    "msg": "查询成功"                                   
}   
```


#### 用户管理修改前查询 说明
``` 
http请求: POST 
http请求url:   http://127.0.0.1:8000/zhugedanao/userManagementOper/beforeUpdate/o_id?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		         说明
o_id                    URL                 是                   要查询的用户ID

返回说明 （正常时返回的json数据 示例）
{
    "msg": "查询成功",
    "code": 200,
    "data": {
        "otherData": {                  
            "role": "无角色",                  # 对应角色 
            "user_level": [                   # 用户等级
                "普通用户"
            ]
        }
    }
}
```

#### 用户管理修改 说明
``` 
http请求： POST
http请求url：  http://127.0.0.1:8000/zhugedanao/userManagementOper/afterUpdate/16?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		         说明
user_level              POST                是                   用户等级ID
role                    POST                是                   角色ID

返回说明 （正常时返回的json数据 示例）
{
    "code": 200,
    "data": {},
    "msg": "修改成功"
}
```

#### 用户管理查询 说明
``` 
http请求： GET
http请求url： http://127.0.0.1:8000/zhugedanao/userManagementShow?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
参数   			        请求方式		        是否必须 		         说明
无

返回说明 （正常时返回的json数据 示例）
{
    "msg": "查询成功",
    "code": 200,
    "data": {
        "data_list": [
            {
                "create_date": "2018-09-07T20:11:16",
                "level": "普通用户",
                "role": "",
                "username": "做自己"
            },
            {
                "create_date": "2018-09-05T17:25:12",
                "level": "普通用户",
                "role": "",
                "username": "吴中生有"
            },
            {
                "create_date": "2018-09-05T17:08:02",
                "level": "普通用户",
                "role": "",
                "username": "雷华标"
            },
            {
                "create_date": "2018-09-04T11:19:34",
                "level": "普通用户",
                "role": "",
                "username": "真诚（陈）"
            },
            {
                "create_date": "2018-08-30T08:51:54",
                "level": "普通用户",
                "role": "",
                "username": "邱华兵"
            },
            {
                "create_date": "2018-08-28T16:23:22",
                "level": "普通用户",
                "role": "",
                "username": " 小四月 。"
            },
            {
                "create_date": "2018-08-23T11:06:34",
                "level": "普通用户",
                "role": "",
                "username": "宁波同仁植发"
            },
            {
                "create_date": "2018-08-23T10:39:36",
                "level": "普通用户",
                "role": "",
                "username": "二庆"
            },
            {
                "create_date": "2018-08-23T10:34:18",
                "level": "普通用户",
                "role": "",
                "username": "Sven"
            },
            {
                "create_date": "2018-08-23T10:33:55",
                "level": "普通用户",
                "role": "",
                "username": "眼迷离"
            }
        ],
        "obj_count": 98                                                               总数
    }
}
```


#### 统计
``` 
http请求： GET
http请求url：  http://127.0.0.1:8000/zhugedanao/statisticalDetails?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11&JudgeFunc=userStatistics&watchDay=watchSevenDays
参数   			        请求方式		        是否必须 		         说明
watchDay                GET                 否                   # 不传参 默认今天
                                                                 watchYesterday  # 明天      
                                                                 watchSevenDays  # 七天
                                                                 watchThirtyDays # 一个月
                                                                 watchAllDays    # 汇总
                                                                  
JudgeFunc               GET                 是                   userStatistics      # 用户统计
                                                                 newUserStatistics   # 新增用户 
                                                                 activeUsersNum      # 活跃用户
                                                                 loginNum            # 登录用户
                                                                  
detailsLogData          GET                 否                   用户统计 和 新增用户 详情查询 ID
detailsUserData         GET                 否                   活跃用户 和 登录用户 详情查询 ID
用户统计返回说明 （正常时返回的json数据示例）
{
    "data": {
        "otherData": [
            {
                "create_time": "2018-09-07 20-11-16",
                "city": "通州",
                "set_avator": "http://thirdwx.qlogo.cn/mmopen/PiajxSqBRaEKVmDsdSa1GOBN4XVnegvVRTeHqwVJMnOomZOlUzPTicAXyYNibKsLFRaW7nVSQUic75070xpmZOeMkw/132",
                "sex": "男",
                "o_id": 10,
                "username": "做自己",
                "country": "中国",
                "province": "北京"
            }
        ],
        "objsCount": 98
    },
    "msg": "查询成功",
    "code": 200
}

新增用户返回说明 （正常时返回的json数据示例）
{
    "data": {
        "otherData": [
            {
                "create_time": "2018-09-07 20-11-16",
                "city": "通州",
                "set_avator": "http://thirdwx.qlogo.cn/mmopen/PiajxSqBRaEKVmDsdSa1GOBN4XVnegvVRTeHqwVJMnOomZOlUzPTicAXyYNibKsLFRaW7nVSQUic75070xpmZOeMkw/132",
                "sex": "男",
                "o_id": 10,
                "username": "做自己",
                "country": "中国",
                "province": "北京"
            }
        ],
        "objsCount": 1
    },
    "msg": "查询成功",
    "code": 200
}

活跃用户返回说明 （正常时返回的json数据示例）
{
    "data": {
        "otherData": [
            {
                "city": "通州",
                "create_date": "2018-09-07T20:11:16",
                "sex": 1,
                "user": "做自己",
                "country": "中国",
                "set_avator": "http://thirdwx.qlogo.cn/mmopen/PiajxSqBRaEKVmDsdSa1GOBN4XVnegvVRTeHqwVJMnOomZOlUzPTicAXyYNibKsLFRaW7nVSQUic75070xpmZOeMkw/132"
            }           
        ],
        "objsCount": 11
    },
    "msg": "查询成功",
    "code": 200
}

登录用户返回说明 （正常时返回的json数据示例）
{
    "code": 200,
    "msg": "查询成功",
    "data": {
        "objsCount": 5,
        "otherData": [
            {
                "user": "张聪",
                "city": "丰台",
                "set_avator": "http://thirdwx.qlogo.cn/mmopen/oFswpUmYn53kTv5QdmmONicVJqp3okrhHospu6icoLF7Slc5XyZWR96STN9RiakoBQn1uoFJIWEicJgJ1QjR5iaGOgWNQ5BSVqFe5/132",
                "country": "中国",
                "sex": "男",
                "create_date": "2018-06-16T20:13:59"
            }            
        ]
    }
}

用户统计 和 新增用户 详情查询（正常时返回的json数据示例）
{
    "code": 200,
    "data": {
        "username": "张聪",
        "objCount": 1,
        "onlineTime": [
            {
                "stopTime": "2018-09-14 14:39:07",
                "day": 1,
                "minutes": 4,
                "hour": 0,
                "startTime": "2018-09-13 14:34:48",
                "seconds": 19
            },
            {
                "stopTime": "2018-09-12 14:39:07",
                "day": 0,
                "minutes": 4,
                "hour": 0,
                "startTime": "2018-09-12 14:34:48",
                "seconds": 19
            }
        ]
    },
    "msg": "查询成功"
}

活跃用户 和 登录用户 详情查询（正常时返回的json数据示例）
{
    "code": 200,
    "data": {
        "objCount": 8,
        "dataList": [
            "登录",
            "关键词首页覆盖查询",
            "查询覆盖",
            "收录查询",
            "查询按钮",
            "重点词监控",
            "添加任务按钮",
            "返回按钮"
        ]
    },
    "msg": "查询成功"
}
```

#### 统计在线时长
``` 
http请求： GET
http请求url： http://127.0.0.1:8000/zhugedanao/statisticsUserOnlineTime?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11&pid=1
参数   			        请求方式		        是否必须 		         说明
startTime               GET                 否                   第一次请求发送该请求 值为 startTime
pid                     GET                 否                   第一次发送请求返回值为pid 依次请求带pid

依次请求  返回说明 （正常时返回的json数据 示例）
{
    "msg": "更新时间叠加",
    "data": {},
    "code": 200
}

第一次请求 返回说明 （正常时返回的json数据 示例）
{
    "code": 200,
    "data": {
        "pid": 3
    },
    "msg": "创建初始时间"
}
```










