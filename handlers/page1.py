from tornado import web,websocket
import json
clients = []
clients1 = []



class page1Handler(web.RequestHandler):
	def get(self):
		self.render("../templates/page1.html")
		print("hiii")
	def post(self):
		usr=self.get_argument("username")
		print(usr)
		self.render("../templates/page1.html",user1=usr)


class WSHandler(websocket.WebSocketHandler):
	def open(self):
		clients.append(self)


	def on_message(self,message):
		#var obj=JSON.parse(message)
		string1=json.loads(message)
		for c in clients:
			#c.write_message(string1['id']+":"+string1['messag'])
			c.write_message(string1)



class WSHandler1(websocket.WebSocketHandler):
	def open(self):
		clients1.append(self)


	def on_message(self,message):
		#var obj=JSON.parse(message)
		for c1 in clients1:
			#c.write_message(string1['id']+":"+string1['messag'])
			c1.write_message(message)


#class SignInHandler(web.RequestHandler):
#    def get(self):
#        self.render("../templates/page2.html")

