import aiohttp_cors
from views import sensors, user
from controllers import temperature, humidity, pressure, gas, light

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
    cors.add(temp_resource.add_route("GET", sensors.TempsView))

    last_temp_resource = cors.add(app.router.add_resource("/temperature/last", name='last_temperature'))
    cors.add(last_temp_resource.add_route("GET", sensors.LastTempView))

    user_temperature_log = cors.add(app.router.add_resource("/log_temperature/", name='log_temperature'))
    cors.add(user_temperature_log.add_route("GET", temperature.log_temperatures))
    cors.add(user_temperature_log.add_route("DELETE", temperature.delete_temperature_log))

    # Pressure
    press_resource = cors.add(app.router.add_resource("/pressure/", name='pressure'))
    cors.add(press_resource.add_route("GET", sensors.PressView))

    last_press_resource = cors.add(app.router.add_resource("/pressure/last", name='last_pressure'))
    cors.add(last_press_resource.add_route("GET", sensors.LastPressView))

    user_pressure_log = cors.add(app.router.add_resource("/log_pressure/", name='log_pressure'))
    cors.add(user_pressure_log.add_route("GET", pressure.log_pressures))
    cors.add(user_pressure_log.add_route("DELETE", pressure.delete_pressure_log))

    # Humidity
    humid_resource = cors.add(app.router.add_resource("/humidity/", name='humidity'))
    cors.add(humid_resource.add_route("GET", sensors.HumidView))

    last_humid_resource = cors.add(app.router.add_resource("/humidity/last", name='last_humidity'))
    cors.add(last_humid_resource.add_route("GET", sensors.LastHumidView))

    user_humidity_log = cors.add(app.router.add_resource("/log_humidity/", name='log_humidity'))
    cors.add(user_humidity_log.add_route("GET", humidity.log_humidities))
    cors.add(user_humidity_log.add_route("DELETE", humidity.delete_humidity_log))

    # Gas
    gas_resource = cors.add(app.router.add_resource("/gas/", name='gas'))
    cors.add(gas_resource.add_route("GET", sensors.GasView))

    last_gas_resource = cors.add(app.router.add_resource("/gas/last", name='last_gas'))
    cors.add(last_gas_resource.add_route("GET", sensors.LastGasView))

    user_gas_log = cors.add(app.router.add_resource("/log_gas/", name='log_gas'))
    cors.add(user_gas_log.add_route("GET", gas.log_gases))
    cors.add(user_gas_log.add_route("DELETE", gas.delete_gas_log))

    # Light
    light_resource = cors.add(app.router.add_resource("/light/", name='light'))
    cors.add(light_resource.add_route("GET", sensors.LightView))

    last_light_resource = cors.add(app.router.add_resource("/light/last", name='last_light'))
    cors.add(last_light_resource.add_route("GET", sensors.LastLightView))

    user_light_log = cors.add(app.router.add_resource("/log_light/", name='log_light'))
    cors.add(user_light_log.add_route("GET", light.log_light))
    cors.add(user_light_log.add_route("DELETE", light.delete_light_log))
    ################################################

    ################################################
    # User
    user_register = cors.add(app.router.add_resource("/user/", name='user'))
    cors.add(user_register.add_route("POST", user.post))
    cors.add(user_register.add_route("DELETE", user.delete))

    user_login = cors.add(app.router.add_resource("/login/", name="login"))
    cors.add(user_login.add_route("POST", user.login))

    user_logout = cors.add(app.router.add_resource("/logout/", name="logout"))
    cors.add(user_logout.add_route("POST", user.logout))

    user_profile = cors.add(app.router.add_resource("/user/{login}", name="user_profile"))
    cors.add(user_profile.add_route("GET", user.show_profile))