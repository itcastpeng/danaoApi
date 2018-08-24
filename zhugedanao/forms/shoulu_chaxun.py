from django import forms
import re
from zhugedanao import models
import time


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
        url_data_list = []
        url_list = self.data.get('url_list')
        for i in url_list.strip().split():
            if i.strip():
                url_data_list.append(i.strip())
        if len(url_data_list) == 0:
            self.add_error('url', '链接不能为空')
        # if len(url_data_list) > 500:
        #     self.add_error('url', '链接大于五百条!')
        else:
            url_list_data = []
            for url_re in url_data_list:
                pattern = re.compile(
                    r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # 匹配模式
                url = re.findall(pattern, url_re)
                if url:
                    url_list_data.append(url[0])
                else:
                    self.add_error('url_list', '请输入正确链接')
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
