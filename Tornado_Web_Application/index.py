import tornado.web
import tornado.ioloop
import json

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World")

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class resourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self, studentName, courseID):
        self.write(f"Welcome {studentName}!!! the course you're viewing is {courseID}")

class queryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if (num.isdigit()):
            r = "odd" if int(num) % 2 else "even"
            self.write(f"The integer {num} is {r}")
        else:
            self.write(f"{num} is not a valid integer.")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/Animal", listRequestHandler),
        (r"/IsEven", queryParamRequestHandler),
        (r"/students/([a-z]+)/([0-9]+)", resourceParamRequestHandler)

    ])



    port = 8882
    app.listen(port)

    print (f"Application is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()