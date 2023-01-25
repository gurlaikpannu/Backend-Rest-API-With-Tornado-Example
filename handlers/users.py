import tornado.web

import models.users as usersModel


class Users(tornado.web.RequestHandler):
	def get(self, userId):
		self.write(f"Hello, world -> , ID: {userId}")

		# db = Connect(dbParams)
		# user = usersModel.getUser(userId)
