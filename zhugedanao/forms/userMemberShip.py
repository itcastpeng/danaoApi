from django import forms
import re
from zhugedanao import models
import time, json


# 添加
class AddForm(forms.Form):
    membershipGrade = forms.IntegerField(
        required=True,
        error_messages={
            'required': "会员等级不能为空"
        }
    )
    theOpeningTime = forms.CharField(
        required=True,
        error_messages={
            'required': "时长不能为空"
        }
    )
    price = forms.IntegerField(
        required=True,
        error_messages={
            'required': "钱数不能为空"
        }
    )
    shouLuChaXunNum = forms.IntegerField(
        required=False,
        error_messages={
            'required': "收录数量类型错误"
        }
    )
    fuGaiChaXunNum = forms.IntegerField(
        required=False,
        error_messages={
            'required': "覆盖数量类型错误"
        }
    )
    zhongDianCiNum = forms.IntegerField(
        required=False,
        error_messages={
            'required': "重点词数量类型错误"
        }
    )
    pingTaiWaJueNum = forms.IntegerField(
        required=False,
        error_messages={
            'required': "平台挖掘数量类型错误"
        }
    )
    baiDuXiaLaNum = forms.IntegerField(
        required=False,
        error_messages={
            'required': "百度下拉数量类型错误"
        }
    )


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
