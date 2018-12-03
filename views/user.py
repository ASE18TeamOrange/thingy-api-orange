from aiohttp.web import Response, View, json_response
from aiohttp_cors import CorsViewMixin

from models.user import User
from uuid import uuid4
import asyncio


@asyncio.coroutine
async def post(request):
    """ Register user """
    
    request_json = await request.json()
    print(request_json)

    try:
        login = request_json['login']
    except Exception as e:
        print(e)
        print("Login needed")
    try:
        password = request_json['password']
    except Exception as e:
        print(e)

    print(login, " ", password)
    try:
        result = await User.create(login, password)

        if result is None:
            return Response(text="Username already exists")
        
        return Response(text="User created", status=201)
    except Exception as ex:
        print("Exception occurred while trying to create user: ", ex)
        return Response(text="User creation failed", status=500)
    

@asyncio.coroutine
async def delete(request):
    """ Register user """
    
    request_json = await request.json()
    print(request_json)

    try:
        login = request_json['login']
    except Exception as e:
        print(e)
        print("Login needed")

    result = await User.delete(login)

    if result is None:
        return Response(text="No user with this login")
    
    return Response(text="User deleted", status=200)