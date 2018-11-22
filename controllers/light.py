from aiohttp import web
from service.thingy_env_sensors import EnvironmentSensorDataService
from models.environment import EnvironmentSensorData


async def log_light(request):
    # data = await request.json()

    # if 'name' not in data:
    #     return web.json_response({'error': '"name" is a required field'})
    # name = data['name']
    # if not isinstance(name, str) or not len(name):
    #     return web.json_response({'error': '"name" must be a string with at least one character'})

    name = 'light_series'
    esd_service = EnvironmentSensorDataService()
    esd_service.run_light_service(name)

    return web.Response(status=204)

def delete_light_log(request):
    #todo test with json data post
    #data = await request.json()

    #if 'name' not in data:
    #    return web.json_response({'error': '"name" is a required field'})
    #name = data['name']
    #if not isinstance(name, str) or not len(name):
    #    return web.json_response({'error': '"name" must be a string with at least one character'})

    #temp
    name = 'light_series'
    esd = EnvironmentSensorData()
    esd.delete(name)

    return web.Response(status=204)