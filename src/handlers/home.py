#!/usr/bin/env python
# coding=utf8
__author__ = 'livvy'


import tornado.options
import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.render("index.html")


routes = [
    (r"/", IndexHandler)
]