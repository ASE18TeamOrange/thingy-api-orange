import aiohttp_cors
import views


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