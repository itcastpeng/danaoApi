from django import forms
import re
from zhugedanao import models
import time, json


# 添加
class AddForm(forms.Form):
    search_list = forms.CharField(
        required=False,
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
    page_number = forms.IntegerField(
        required=False,
        error_messages={
            'required': "页码数据类型错误"
        }
    )
    def clean_url_list(self):
        url_list = []
        url = self.data.get('url_list')
        url_num = 0
        for i in url.split('\n'):
            url_num += 1
            if i.strip():
                url_list.append(i.strip())
            else:
                self.add_error('url_list', '第{}行不能为空!'.format(url_num))
        if len(url_list) == 0:
            self.add_error('url_list', '提交链接不能为空')
        # if len(url_list) > 20:                          # 测试
        if len(url_list) > 1000:  # 线上
            self.add_error('url_list', '提交链接大于1000条!')
        else:
            url_list_data = []
            num = 0
            for url_re in url_list:
                num += 1
                pattern = re.compile(
                    r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # 匹配模式
                url = re.findall(pattern, url_re)
                if url:
                    url_list_data.append(url[0])
                else:
                    self.add_error('url_list', '第{}行请输入正确链接'.format(num))
            return url_list_data


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
