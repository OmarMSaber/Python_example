from tornado import web,ioloop
from handlers.page1 import page1Handler,WSHandler,WSHandler1
from handlers.page2 import page2Handler


class MainHandler(web.RequestHandler):
    def get(self):
        self.render("templates/homepage.html")


app = web.Application([
	(r"/", MainHandler),
	(r"/page1", page1Handler),
	(r"/page2", page2Handler),
	(r"/ws",WSHandler),
	(r"/ws1",WSHandler1),
	#(r"/signin",SignInHandler)
	],
	static_path='static',debug=True,cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__")

app.listen(8080)
ioloop.IOLoop.current().start()