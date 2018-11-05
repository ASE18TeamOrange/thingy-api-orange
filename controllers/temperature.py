from aiohttp import web
from service.thingy_env_sensors import EnvironmentSensorDataService
from models.environment import EnvironmentSensorData


def log_temperatures(request):
    #todo test with json data post
    #data = await request.json()

    #if 'name' not in data:
    #    return web.json_response({'error': '"name" is a required field'})
    #name = data['name']
    #if not isinstance(name, str) or not len(name):
    #    return web.json_response({'error': '"name" must be a string with at least one character'})

    #temp
    name = 'temperature_series'
    temperature_service = EnvironmentSensorDataService()
    temperature_service.run_temperature_service(name)

    return web.Response(status=204)


def delete_temperature_log(request):
    #todo test with json data post
    #data = await request.json()

    #if 'name' not in data:
    #    return web.json_response({'error': '"name" is a required field'})
    #name = data['name']
    #if not isinstance(name, str) or not len(name):
    #    return web.json_response({'error': '"name" must be a string with at least one character'})

    #temp
    name = 'temperature_series'
    temperature_log = EnvironmentSensorData()
    temperature_log.delete(name)

    return web.Response(status=204)