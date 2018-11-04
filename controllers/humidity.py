from aiohttp import web
from service.thingy_env_sensors import EnvironmentSensorDataService


async def collect_humidities(request):
    data = await request.json()

    if 'name' not in data:
        return web.json_response({'error': '"name" is a required field'})
    name = data['name']
    if not isinstance(name, str) or not len(name):
        return web.json_response({'error': '"name" must be a string with at least one character'})

    humidity_service = EnvironmentSensorDataService()
    humidity_service.run_humidity_service()

    return web.Response(status=204)