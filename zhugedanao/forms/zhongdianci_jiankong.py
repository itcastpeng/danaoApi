from django import forms
import re
from zhugedanao import models
import time, json

# 添加
class AddForm(forms.Form):
    task_name = forms.CharField(
        required=True,
        error_messages={
            'required': "任务名称不能为空"
        }
    )
    search_engine = forms.CharField(
        required=True,
        error_messages={
            'required': "搜索引擎不能为空"
        }
    )
    keywords = forms.CharField(
        required=True,
        error_messages={
            'required': "关键词不能为空"
        }
    )
    # task_status = forms.IntegerField(
    #     required=True,
    #     error_messages={
    #         'required': "任务状态不能为空"
    #     }
    # )

    def clean_search_engine(self):
        search_engine = self.data.get('search_engine')
        json_search = json.loads(search_engine)
        return json_search

    def clean_keywords(self):
        keywords = self.data.get('keywords')
        if len(keywords.split()) == 0:
            self.add_error('keywords', '关键词不能为空!')
        if len(keywords.split()) > 500:
            self.add_error('keywords', '关键词超过五百条!')
        else:
            return keywords







        # self.add_error('search_engine', '搜索引擎不能为空')























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
