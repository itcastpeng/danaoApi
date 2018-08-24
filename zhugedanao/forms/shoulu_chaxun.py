from django import forms
import re
from zhugedanao import models
import time, json


# 添加
class AddForm(forms.Form):
    search_list = forms.CharField(
        required=True,
        error_messages={
            'required': "搜索引擎不能为空"
        }
    )
    url_list = forms.CharField(
        required=True,
        error_messages={
            'required': "提交链接不能为空"
        }
    )
    def clean_url_list(self):
        url_list = self.data.get('url_list')
        return url_list.split()


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
