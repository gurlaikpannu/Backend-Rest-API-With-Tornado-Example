import asyncio

import tornado.web

from handlers.users import Users

SERVER_PORT = 8888

def make_app():
	return tornado.web.Application([
		(r"/users/([\d]+)", Users),
	])

async def main():
	print("Starting APP")

	app = make_app()
	app.listen(SERVER_PORT)
	await asyncio.Event().wait()

if __name__ == "__main__":
	asyncio.run(main())
