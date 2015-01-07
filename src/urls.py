#!/usr/bin/env python
# coding=utf8
__author__ = 'livvy'

from handlers import home
# 全局路由
# 将每个handler文件中的路由汇聚于此
routes = []
routes.extend(home.routes)