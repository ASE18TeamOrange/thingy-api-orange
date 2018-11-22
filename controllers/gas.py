from aiohttp import web
from service.thingy_env_sensors import EnvironmentSensorDataService
from models.environment import EnvironmentSensorData


async def log_gases(request):
    # data = await request.json()

    # if 'name' not in data:
    #     return web.json_response({'error': '"name" is a required field'})
    # name = data['name']
    # if not isinstance(name, str) or not len(name):
    #     return web.json_response({'error': '"name" must be a string with at least one character'})

    name = 'gas_series'
    pressure_service = EnvironmentSensorDataService()
    pressure_service.run_gas_service(name)

    return web.Response(status=204)

def delete_gas_log(request):
    #todo test with json data post
    #data = await request.json()

    #if 'name' not in data:
    #    return web.json_response({'error': '"name" is a required field'})
    #name = data['name']
    #if not isinstance(name, str) or not len(name):
    #    return web.json_response({'error': '"name" must be a string with at least one character'})

    #temp
    name = 'gas_series'
    temperature_log = EnvironmentSensorData()
    temperature_log.delete(name)

    return web.Response(status=204)