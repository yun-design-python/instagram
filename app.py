import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options

from handlers.main import IndexHandler, ExplorHandler, PostHandler
from handlers.users import RegisterHandler, LoginHandler

define("port", default="8888", help="Listening port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/index", IndexHandler),
            (r"/explor", ExplorHandler),
            (r"/post/(?P<post_id>[0-9]+)", PostHandler),
            (r"/register", RegisterHandler),
            (r"/login", LoginHandler),

        ]
        settings = dict(
            debug=True,
            template_path="templates"
        )

        super().__init__(handlers, **settings)
if __name__ == "__main__":
    tornado.options.parse_command_line()#命令行
    application = Application()  #实例化
    application.listen(options.port) #链接端口
    tornado.ioloop.IOLoop.current().start()#开启tornado服务
































