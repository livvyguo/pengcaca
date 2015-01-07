#!/usr/bin/env python
# coding=utf8
__author__ = 'livvy'
import os.path

import tornado.options
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import options, define

define("port", default=9999, help="run on the given port", type=int)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    from urls import routes as handlers
    app = tornado.web.Application(
        handlers=handlers,
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "statics"),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
