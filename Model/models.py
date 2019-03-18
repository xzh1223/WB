# -*- coding: utf-8 -*-

# Create your models here.
# models.py
import django.utils.timezone as timezone

from django.db import models


# 用户表
class User(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=18)
    mobile = models.CharField(max_length=11, null=True)
    email = models.EmailField(null=True)
    code = models.CharField(null=True, max_length=6)
    create_time = models.DateTimeField('创建时间', default=timezone.now)


# 我的博客表
class MyBlog(models.Model):
    # user_id = models.IntegerField(null=False)
    title = models.TextField(null=True)
    description = models.TextField(null=True)
    content = models.TextField(null=True)
    create_time = models.TextField(null=True)
    # status = models.IntegerField(null=False, default=0)
    url = models.TextField(null=True)


# 我的聚焦
class Focus(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    time = models.IntegerField(null=True, default=0)
    create_time = models.DateTimeField('创建时间', default=timezone.now)
    user_id = models.IntegerField(null=False)
    status = models.IntegerField(default=0)
