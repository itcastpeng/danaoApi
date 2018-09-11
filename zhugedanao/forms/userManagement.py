from django import forms
import re
from zhugedanao import models
import time, json


# 添加
class AddForm(forms.Form):
    role_name = forms.CharField(
        required=True,
        error_messages={
            'required': "角色名不能为空"
        }
    )
    quanxian = forms.CharField(
        required=False,
        error_messages={
            'required': ""
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


# 更新
class UpdateForm(forms.Form):
    roleName = forms.CharField(
        required=True,
        error_messages={
            'required': '角色名称不能为空'
        }
    )
    o_id = forms.IntegerField(
        required=True,
        error_messages={
            'required': '角色id不能为空'
        }
    )

    permissionList = forms.CharField(
        required=True,
        error_messages={
            'required': "选择权限不能为空"
        }
    )

    # 判断名称是否存在
    def clean_roleName(self):
        o_id = self.data['o_id']
        name = self.data['roleName']
        objs = models.zhugedanao_role.objects.filter(
            name=name,
        ).exclude(id=o_id)
        if objs:
            self.add_error('roleName', '角色名称已存在')
        else:
            return name

    def clean_permissionList(self):
        permissionList = self.data.get('permissionList')
        return json.loads(permissionList)