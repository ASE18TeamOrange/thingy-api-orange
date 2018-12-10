import asyncio
from models.database import Database
import jwt
from ast import literal_eval


JWT_ALG = "HS256"

class SessionHandler:
    __database = None

    def __init__(self, app, loop=asyncio.get_event_loop()):
        self.__app = app
        self.__database = Database()
        self.loop = loop
        self.loop.create_task(self.check_expired_sessions())

    @asyncio.coroutine
    async def check_expired_sessions(self):
        while True:
            await asyncio.sleep(1)
            sessions_raw = (self.__database.get_hash_all('sessions:'))
            sessions = convert(sessions_raw)

            for key in sessions.keys():
                val = sessions[key]
                new_val = literal_eval(val)
                sessions[key] = new_val

            for item in sessions.items():

                try:
                    key = item[0]
                    token = item[1]['token']
                    data = jwt.decode(token, self.__app['JWT_KEY'], algorithms=JWT_ALG)

                except jwt.ExpiredSignatureError:
                    print('Expired signature detected. Deleting.')
                    self.__database.delete_hash('sessions:', key)
                except jwt.InvalidTokenError:
                    print('Expired signature detected. Deleting.')
                    self.__database.delete_hash('sessions:', key)


def convert(data):
    if isinstance(data, bytes):  return data.decode()
    if isinstance(data, dict):   return dict(map(convert, data.items()))
    if isinstance(data, tuple):  return tuple(map(convert, data))
    if isinstance(data, list):   return list(map(convert, data))
    return data