import tornado.ioloop
import tornado.web
import yasb
import os

class PagesHandler(tornado.web.RequestHandler):
    def get(self, name):
        page = yasb.load_page_from_yaml(os.path.join("pages", name + '.yaml'))
        self.write(yasb.render_page(page))

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        name = "index"
        page = yasb.load_page_from_yaml(os.path.join("pages", name + '.yaml'))
        self.write(yasb.render_page(page))

if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/~cforstal/cdt-30020-sp17\/?$", MainHandler),
        (r"/([^\/]+)\.html", PagesHandler),
        (r"/~cforstal/cdt-30020-sp17/(.+)\.html", PagesHandler),
        (r"/~cforstal/cdt-30020-sp17/static/(.*)", tornado.web.StaticFileHandler, {'path':'static'}),
    ], 
    debug=True)

    # run the app
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    