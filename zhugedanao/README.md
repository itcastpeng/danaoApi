
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
http请求url http://127.0.0.1:8000/zhugedanao/access_task?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11
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
user_id			GET					是 			操作人id
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
    "data": {},
    "code": 200,
    "msg": "添加成功"
}
```











#### 展示任务列表

GET数据示例:

```
参数   			    请求方式	        是否必须 		        说明
current_page		GET			否			页码
length				GET			否			条数	
order				GET			否			排序条件
```


展示任务详情数据  
detail_lianjie_tijiao
参数   				请求方式		是否必须     说明
current_page	    GET			否			页码
length				GET			否			条数	
order				GET			否			排序条件
tid			        GET			是 			父级id



























