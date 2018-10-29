from aiohttp import web
from routes import *
from models import *


def app_factory(args=()):
    database.create_tables()
    app = web.Application()
    setup_routes(app)
    return app

