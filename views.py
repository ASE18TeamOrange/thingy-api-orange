from aiohttp.web import Response, View, json_response
from aiohttp_cors import CorsViewMixin

from models.readings import Temperature, Pressure, Humidity, Gas, Light


class TempsView(View, CorsViewMixin):
    """
    Temperature view
    """

    async def get(self):
      """ Return JSON with all temperature readings """
      return json_response(await Temperature.all_readings())

    # TODO: Define and implement rest of functions for view

class LastTempView(View, CorsViewMixin):
    """
    Last temperature view (most recent reading)
    """

    async def get(self):
      """ Return JSON with the current temperature reading """
      return json_response(await Temperature.last_reading())


class PressView(View, CorsViewMixin):
    """
    Pressure view
    """

    async def get(self):
      """ Return JSON with all pressure readings """
      return json_response(await Pressure.all_readings())

class LastPressView(View, CorsViewMixin):
    """
    Last pressure view (most recent reading)
    """

    async def get(self):
      """ Return JSON with the current pressure reading """
      return json_response(await Pressure.last_reading())


class HumidView(View, CorsViewMixin):
    """
    Humidity view
    """

    async def get(self):
      """ Return JSON with all humidity readings """
      return json_response(await Humidity.all_readings())

class LastHumidView(View, CorsViewMixin):
    """
    Last humidity view (most recent reading)
    """

    async def get(self):
      """ Return JSON with the current humidity reading """
      return json_response(await Humidity.last_reading())


class GasView(View, CorsViewMixin):
    """
    Gas view
    """

    async def get(self):
      """ Return JSON with all gas readings """
      return json_response(await Gas.all_readings())

class LastGasView(View, CorsViewMixin):
    """
    Last gas view (most recent reading)
    """

    async def get(self):
      """ Return JSON with the current gas reading """
      return json_response(await Gas.last_reading())


class LightView(View, CorsViewMixin):
    """
    Light view
    """

    async def get(self):
      """ Return JSON with all light readings """
      return json_response(await Light.all_readings())

class LastLightView(View, CorsViewMixin):
    """
    Last light view (most recent reading)
    """

    async def get(self):
      """ Return JSON with the current light reading """
      return json_response(await Light.last_reading())