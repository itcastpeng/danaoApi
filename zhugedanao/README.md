
#### code 说明：
```
200 正常

300 角色名已存在
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
http请求url： http://127.0.0.1:8000/zhugedanao/shouLuChauxn/add/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
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
http请求url： http://127.0.0.1:8000/zhugedanao/shouLuChauxn/clickReturn/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
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
无

返回说明 （正常时返回的json数据 示例）
{
    "data": {
        "retData": [
            {   
                "status_code": null,                # 链接返回的 状态码
                "search": "百度",                    # 搜索引擎
                "is_shoulu": "未收录",               # 是否收录
                "url": "sdfsadfsdaf",               # 链接
                "kuaizhao_time": null,              # 链接返回的 快照时间
                "title": null                       # 链接标题
            },
        ],
        "dataCount": 1,                             # 数据总数
        "yiWanCheng": 0,                            # 已完成数量
        "shouLuLv": 0,                              # 收录率
        "shouluNum": 0                              # 收录数量
    },
    "msg": "查询成功",
    "code": 200
}
```















