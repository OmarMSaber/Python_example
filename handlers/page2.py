from tornado import web,websocket


class page2Handler(web.RequestHandler):
	def get(self):
		self.render("../templates/page2.html")


