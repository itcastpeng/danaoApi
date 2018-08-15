
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

添加任务
lianjie_tijiao/add/id
参数   			请求方式		是否必须 		        说明
user_id			GET					是 			操作人id
name 			POST				是 			任务名称
url		        POST				是 			任务链接
