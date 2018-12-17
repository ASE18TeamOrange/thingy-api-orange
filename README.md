# thingy-api-orange

Restful api for time series data

To run on local:

python -m aiohttp.web -P 8081 app:app_factory

or 

web.run_app(app, host='localhost', port='8081')


Requisites:
redis_readme