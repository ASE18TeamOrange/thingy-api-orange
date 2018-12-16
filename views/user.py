from aiohttp.web import Response, View, json_response
from aiohttp_cors import CorsViewMixin

from models.user import User
from uuid import uuid4
import asyncio
from functools import wraps
import jwt
import json

JWT_ALG = "HS256"

# decorator for methods with required authentication token
def token_required(f):
    @wraps(f)
    def decorated(request, *args, **kwargs):
        token = None
        try:
            auth = request.headers['authorization']
        except KeyError as keyErr:
            return json_response({'message': 'Missing token'}, status=401)

        try:
            token = auth#[7::]
            print(token)
            data = jwt.decode(token, request.app['JWT_KEY'], algorithms=JWT_ALG)
            print("DAT: ", data)
            current_user = data['login']
        except jwt.ExpiredSignatureError:
            return json_response({'message': 'Signature expired. Please log in again.'}, status=401)
        except jwt.InvalidTokenError:
            return json_response({'message': 'Invalid token. Please log in again.'}, status=401)

        return f(request, current_user, *args, **kwargs)

    return decorated


@asyncio.coroutine
async def post(request):
    """ Register user with specified login and password """
    
    request_json = await request.json()

    try:
        login = request_json['login']
    except Exception as e:
        print(e)
        print("Login needed")
    try:
        password = request_json['password']
    except Exception as e:
        print(e)

    try:
        result = await User.create(login, password)

        if result is None:
            return json_response({'message': 'User already exists'}, status=401)
        
        return json_response({'message': 'User created!'}, status=200)
    except Exception as ex:
        print("Exception occurred while trying to create user: ", ex)
        return json_response({'message': 'User creation failed!'}, status=500)
    

@token_required
@asyncio.coroutine
async def delete(request, current_user):
    """ Delete user with specific login """
    request_json = await request.json()

    try:
        login = request_json['login']
        print(login)
    except Exception as e:
        print(e)
        print("Login needed")

    if login != current_user:
        print(str(login) + ' - ' + str(current_user))
        return json_response({'message': 'You have no power here!'}, status=403)

    result = await User.delete(login)

    if result is None:
        return json_response({'message': 'no user with this login!'}, status=400)
    
    return json_response({'message': 'user deleted'}, status=200)


@asyncio.coroutine
async def login(request):
    request_json = await request.json()

    try:
        login = request_json['login']
    except Exception as e:
        print(e)
        print("Login needed")
    
    try:
        password = request_json['password']
    except Exception as e:
        print(e)
        print("Password needed")

    result = await User.login(login, password, request.app['JWT_KEY'])

    if result is None:
        return json_response({'message': 'Login failed. Login or password incorrect!'}, status=401)
    
    return result
    

@token_required
@asyncio.coroutine
async def show_profile(request, current_user):
    print('show_profile')
    try:
        login = request.match_info.get('login')
    except Exception as e:
        print(e)
        print("Login not found")
    
    if login != current_user:
        return json_response({'message': 'You have no power here!'}, status=403)

    result = await User.get_profile(login)

    if result is None:
        return json_response({'message': 'Profile not found'}, status=401)

    list_of_sensors = result['sensors']
    sensors = ','.join(list_of_sensors)
    return json_response(
        {'login': result['login'], 'id': result['id'], 'thingy': result['thingy'], 'sensors': '[' + sensors + ']'}
    , status=200)


@token_required
@asyncio.coroutine
async def logout(request, current_user):
    request_json = await request.json()
    print(request_json)

    try:
        login = request_json['login']
    except Exception as e:
        print(e)
        print("Login not found")

    if login != current_user:
        return json_response({'message': 'You have no power here!'}, status=403)

    result = await User.logout(login)
    
    if result is None:
        return json_response({'message': 'User already logged out!'}, status=401)

    return json_response({'message': 'Logout successful!'}, status=200)


@token_required
@asyncio.coroutine
async def connect_thingy(request, current_user):
    print('connect_thingy')
    request_json = await request.json()
    print(request_json)

    try:
        login = request_json['login']
    except Exception as e:
        print(e)
        print("Login not found")

    try:
        thingy_id = request_json['thingy_id']
    except Exception as e:
        print(e)
        print("Thingy id not found")

    if login != current_user:
        return json_response({'message': 'You have no power here!'}, status=403)

    result = await User.connect_thingy(login, thingy_id)
    
    if result is None:
        return json_response({'message': 'User not found!'}, status=401)

    return json_response({'message': 'Successfully connected!'}, status=200)
