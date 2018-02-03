#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/3 0:40
# @Author  : CycloneBoy
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.urls import path
from . import views

urlpatterns = [
    path(r'^$',views.index,name='index'),
]
