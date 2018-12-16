from aiohttp import web
from routes import *
from models import *
from controllers.auth import SessionHandler


def app_factory(args=()):
    # database.create_tables()
    app = web.Application()
    app['JWT_KEY'] = "65479d4dee2b90587ec0cff62dfb8f042a2adabc6e7ded6f"
    sessionHandler = SessionHandler(app)
    setup_routes(app)
    web.run_app(app, host='localhost', port='8081')

# Run the server
try:
    app_factory()
except KeyboardInterrupt:
    pass
