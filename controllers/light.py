from aiohttp import web
from service.thingy_env_sensors import EnvironmentSensorDataService
from models.environment import EnvironmentSensorData
from models.database import Database
import asyncio
from functools import wraps
from aiohttp.web import Response, View, json_response
import jwt
from ast import literal_eval


JWT_ALG = "HS256"

# decorator for methods with required authentication token
def token_required(f):
    @wraps(f)
    def decorated(request, *args, **kwargs):
        token = None

        try:
            auth = request.headers['authorization']
        except KeyError as keyErr:
            print(keyErr)
            return json_response({'message' : 'Missing token'}, status=401)

        try:
            token = auth[7::]
            print(token)
            data = jwt.decode(token, request.app['JWT_KEY'], algorithms=JWT_ALG)
            print("DAT: ", data)
            current_user = data['login']
            print("User: ", current_user)
        except jwt.ExpiredSignatureError:
            return Response(text='Signature expired. Please log in again.')
        except jwt.InvalidTokenError:
            return Response(text='Invalid token. Please log in again.')

        return f(request, current_user, *args, **kwargs)

    return decorated


@token_required
async def log_light(request, current_user):
    request_json = await request.json()
    print(request_json)
    
    try:
        login = request_json['login']
    except Exception as e:
        print(e)
        print("Login needed")

    if login != current_user:
        return Response(text="You have no power here!", status=403)

    redis = Database()
    llogin = login.lower()

    if redis.key_exists_in_hash('users:', llogin):
        db_entry = redis.get_hash('users:', llogin)
        user_dict = literal_eval(db_entry.decode('utf-8'))
        uuid = user_dict['id']
        print(uuid)
    
    user_thingy_raw = redis.get_hash("user:%s" % uuid, "thingy")
    print("raw: ", user_thingy_raw)
    user_thingy = user_thingy_raw.decode('utf-8')
    print(user_thingy)

    name = 'light'
    esd_service = EnvironmentSensorDataService()
    esd_service.run_pressure_service(user_thingy, current_user, name)

    return web.Response(status=204)

@token_required
async def delete_light_log(request, current_user):
    request_json = await request.json()
    print(request_json)
    
    try:
        login = request_json['login']
    except Exception as e:
        print(e)
        print("Login needed")

    if login != current_user:
        return Response(text="You have no power here!", status=403)

    name = 'light'
    esd = EnvironmentSensorData()
    esd.delete(current_user, name)

    return web.Response(status=204)