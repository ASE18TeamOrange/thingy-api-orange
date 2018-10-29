import aiohttp_cors


def setup_routes(app):
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })
    todos_resource = cors.add(app.router.add_resource("/temperature/", name='temperature'))
    cors.add(todos_resource.add_route("GET", get_all_todos))
    cors.add(todos_resource.add_route("DELETE", remove_all_todos))
    cors.add(todos_resource.add_route("POST", create_todo))
