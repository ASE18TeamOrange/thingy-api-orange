import aiohttp_cors
import views
from controllers import user, temperature, humidity, pressure, gas, light

def setup_routes(app):
    # Configure default CORS settings
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })

    # Routes

    ################################################
    # Environment
    # Temperature
    temp_resource = cors.add(app.router.add_resource("/temperature/", name='temperature'))
    cors.add(temp_resource.add_route("GET", views.TempsView))

    last_temp_resource = cors.add(app.router.add_resource("/temperature/last", name='last_temperature'))
    cors.add(last_temp_resource.add_route("GET", views.LastTempView))

    user_temperature_log = cors.add(app.router.add_resource("/log_temperatures/", name='temperatures'))
    cors.add(user_temperature_log.add_route("GET", temperature.log_temperatures))
    # cors.add(user_temperature_log.add_route("DELETE", controllers.temperature.delete_temperature_log))

    # Pressure
    press_resource = cors.add(app.router.add_resource("/pressure/", name='pressure'))
    cors.add(press_resource.add_route("GET", views.PressView))

    last_press_resource = cors.add(app.router.add_resource("/pressure/last", name='last_pressure'))
    cors.add(last_press_resource.add_route("GET", views.LastPressView))

    user_pressure_log = cors.add(app.router.add_resource("/log_pressures/", name='pressures'))
    cors.add(user_pressure_log.add_route("GET", pressure.log_pressures))
    # cors.add(user_pressure_log.add_route("DELETE", controllers.pressure.delete_pressure_log))

    # Humidity
    humid_resource = cors.add(app.router.add_resource("/humidity/", name='humidity'))
    cors.add(humid_resource.add_route("GET", views.HumidView))

    last_humid_resource = cors.add(app.router.add_resource("/humidity/last", name='last_humidity'))
    cors.add(last_humid_resource.add_route("GET", views.LastHumidView))

    user_humidity_log = cors.add(app.router.add_resource("/log_humidity/", name='humidities'))
    cors.add(user_humidity_log.add_route("GET", humidity.log_humidities))
    # cors.add(user_humidity_log.add_route("DELETE", controllers.humidity.delete_humidity_log))

    # Gas
    gas_resource = cors.add(app.router.add_resource("/gas/", name='gas'))
    cors.add(gas_resource.add_route("GET", views.GasView))

    last_gas_resource = cors.add(app.router.add_resource("/gas/last", name='last_gas'))
    cors.add(last_gas_resource.add_route("GET", views.LastGasView))

    user_gas_log = cors.add(app.router.add_resource("/log_gas/", name='log_gas'))
    cors.add(user_gas_log.add_route("GET", gas.log_gases))
    # cors.add(user_gas_log.add_route("DELETE", controllers.gas.delete_gas_log))

    # Light
    light_resource = cors.add(app.router.add_resource("/light/", name='light'))
    cors.add(light_resource.add_route("GET", views.LightView))

    last_light_resource = cors.add(app.router.add_resource("/light/last", name='last_light'))
    cors.add(last_light_resource.add_route("GET", views.LastLightView))

    user_light_log = cors.add(app.router.add_resource("/log_light/", name='log_light'))
    cors.add(user_light_log.add_route("GET", light.log_light))
    # cors.add(user_light_log.add_route("DELETE", controllers.light.delete_light_log))
    ################################################

    ################################################
    # User
    add_user_resource = cors.add(app.router.add_resource("/user/", name='add_user'))
    cors.add(add_user_resource.add_route("POST", user.create_user))
    delete_user_resource = cors.add(app.router.add_resource("/user/", name='delete_user'))
    cors.add(delete_user_resource.add_route("DELETE", user.delete_user))

    # TODO: Add more resources and routes
