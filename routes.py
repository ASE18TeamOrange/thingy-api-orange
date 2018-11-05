import aiohttp_cors
import views
import controllers.user
import controllers.temperature


def setup_routes(app):
    # Configure default CORS settings
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })

    temp_resource = cors.add(app.router.add_resource("/temperature/", name='temperature'))
    cors.add(temp_resource.add_route("GET", views.TempsView))

    # TODO: Add more resources and routes
    # cors.add(temp_resource.add_route("DELETE", remove_all_todos))
    # cors.add(temp_resource.add_route("POST", create_todo))
    last_temp_resource = cors.add(app.router.add_resource("/temperature/last", name='last_temperature'))
    cors.add(last_temp_resource.add_route("GET", views.LastTempView))

    add_user_resource = cors.add(app.router.add_resource("/user/", name='add_user'))
    cors.add(add_user_resource.add_route("POST", controllers.user.create_user))
    delete_user_resource = cors.add(app.router.add_resource("/user/", name='delete_user'))
    cors.add(delete_user_resource.add_route("DELETE", controllers.user.delete_user))

    get_user_temperatures = cors.add(app.router.add_resource("/log_temperatures/", name='log_temperatures'))
    cors.add(get_user_temperatures.add_route("GET", controllers.temperature.log_temperatures))
    delete_user_temperatures = cors.add(app.router.add_resource("/log_temperatures/", name='delete_temperatures'))
    cors.add(delete_user_temperatures.add_route("DELETE", controllers.temperature.delete_temperature_log))


