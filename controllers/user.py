from aiohttp import web
from models.user import User


async def create_user(request):
    data = await request.json()

    if 'name' not in data:
        return web.json_response({'error': '"name" is a required field'})
    name = data['name']
    if not isinstance(name, str) or not len(name):
        return web.json_response({'error': '"name" must be a string with at least one character'})

    if 'pwd' not in data:
        return web.json_response({'error': '"pwd" is a required field'})
    pwd = data['pwd']

    user = User()

    if user.create(name=name, pwd=pwd):
        return web.Response(status=204)
    return web.Response(status=400)


async def delete_user(request):
    data = await request.json()

    if 'name' not in data:
        return web.json_response({'error': '"name" is a required field'})
    name = data['name']
    if not isinstance(name, str) or not len(name):
        return web.json_response({'error': '"name" must be a string with at least one character'})

    if 'pwd' not in data:
        return web.json_response({'error': '"pwd" is a required field'})
    pwd = data['pwd']

    user = User()

    if user.delete(name=name, pwd=pwd):
        return web.Response(status=204)
    return web.Response(status=400)

#todo temporary, enable session for user
#async def authenticate_user(request):