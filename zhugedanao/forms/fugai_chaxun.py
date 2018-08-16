from django import forms

from zhugedanao import models
import time


# 添加
class AddForm(forms.Form):

    search_list = forms.CharField(
        required=True,
        error_messages={
            'required': "任务名称不能为空"
        }
    )
    keywords_list = forms.CharField(
        required=True,
        error_messages={
            'required': "提交链接不能为空"
        }
    )
    conditions_list = forms.CharField(
        required=True,
        error_messages={
            'required': "提交链接不能为空"
        }
    )

    def clean_search_list(self):
        search_list = []
        for i in self.data.get('search_list').strip().split(','):
            search_list.append(i.strip())
        if len(search_list) == 0:
            self.add_error('keyword', '关键词不能为空')
        else:
            return search_list

    def clean_keywords_list(self):
        keywords_data_list = []
        for i in self.data.get('keywords_list').strip().split():
            if i.strip():
                keywords_data_list.append(i.strip())
        if len(keywords_data_list) == 0:
            self.add_error('keyword', '关键词不能为空')
        else:
            return keywords_data_list

    def clean_conditions_list(self):
        conditions_list = []
        for i in self.data.get('conditions_list').split('|'):
            if i:
                conditions_list.append(i.strip())
        if len(conditions_list) == 0:
            self.add_error('keyword', '关键词不能为空')
        else:
            return conditions_list


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