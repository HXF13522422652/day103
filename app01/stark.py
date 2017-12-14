#!/usr/bin/env python
# coding:utf-8
#My_Name:Mrs_HAN 韩晓飞
from app01 import models
from stark.service import v1
from django.utils.safestring import mark_safe
class UserInfig(v1.StarkConfig):
    def checkbox(self,obj=None,is_header=False):
        if is_header:
            return '选择'
        return mark_safe("<input type='checkbox' name='pk' value='%s'/>" %(obj.id))
    def edit(self,obj=None,is_header=False):
        if is_header:
            return '编辑'
        return '<a href="/edit/%s">编辑</a>'%(obj.id)
    list_display = [checkbox,'id','name',edit]


v1.site.register(models.UserInfo,UserInfig)

# class AdminConfig(v1.StarkConfig):
#     list_display = []
# v1.site.register(models.A,)

class RoleConfig(v1.StarkConfig):
    list_display = []
v1.site.register(models.Role,RoleConfig)
class UserTypeConfig(v1.StarkConfig):
    list_display = ['id','title']
v1.site.register(models.UserType,UserTypeConfig)