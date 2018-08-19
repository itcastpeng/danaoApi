from django import forms
import re
from zhugedanao import models
import time


# 添加
class AddForm(forms.Form):
    oper_user_id = forms.IntegerField(
        required=True,
        error_messages={
            'required': '操作人不能为空'
        }
    )

    name = forms.CharField(
        required=True,
        error_messages={
            'required': "任务名称不能为空"
        }
    )
    url = forms.CharField(
        required=True,
        error_messages={
            'required': "提交链接不能为空"
        }
    )

    def clean_url(self):
        url_list = []
        url = self.data.get('url')
        for i in url.strip().split():
            if i.strip():
                url_list.append(i.strip())
        if len(url_list) == 0:
            self.add_error('url', '提交链接不能为空')
        else:
            url_list_data = []
            for url_re in url_list:
                pattern = re.compile(
                    r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # 匹配模式
                url = re.findall(pattern, url_re)
                if url:
                    url_list_data.append(url[0])
                    return url_list_data
                else:
                    self.add_error('url', '请输入正确链接')


# 更新
class UpdateForm(forms.Form):
    o_id = forms.IntegerField(
        required=True,
        error_messages={
            'required': '角色id不能为空'
        }
    )

    name = forms.CharField(
        required=True,
        error_messages={
            'required': "任务名称不能为空"
        }
    )
    url = forms.CharField(
        required=True,
        error_messages={
            'required': "提交链接不能为空"
        }
    )

    def clean_url(self):
        url = self.data.get('url')
        if not url.strip():
            self.add_error('url', '提交链接不能为空')
        else:
            return url

# 任务详情更新 先删除后创建
class UpdateTaskForm(forms.Form):
    o_id = forms.IntegerField(
        required=True,
        error_messages={
            'required': '角色id不能为空'
        }
    )

    name = forms.CharField(
        required=True,
        error_messages={
            'required': "任务名称不能为空"
        }
    )
    url = forms.CharField(
        required=True,
        error_messages={
            'required': "提交链接不能为空"
        }
    )

    def clean_url(self):
        url_list = []
        url = self.data.get('url')
        for i in url.strip().split():
            if i.strip():
                url_list.append(i.strip())
        if len(url_list) == 0:
            self.add_error('url', '提交链接不能为空')
        else:
            return url_list


# 判断是否是数字
class SelectForm(forms.Form):
    current_page = forms.IntegerField(
        required=False,
        error_messages={
            'required': "页码数据类型错误"
        }
    )

    length = forms.IntegerField(
        required=False,
        error_messages={
            'required': "页显示数量类型错误"
        }
    )

    def clean_current_page(self):
        if 'current_page' not in self.data:
            current_page = 1
        else:
            current_page = int(self.data['current_page'])
        return current_page

    def clean_length(self):
        if 'length' not in self.data:
            length = 10
        else:
            length = int(self.data['length'])
        return length
