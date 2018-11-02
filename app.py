from aiohttp import web
from routes import *
from models import *


def app_factory(args=()):
    # database.create_tables()
    app = web.Application()
    setup_routes(app)
    web.run_app(app)

# Run the server
try:
    app_factory()
except KeyboardInterrupt:
    pass
