from aiohttp.web import Response, View, json_response
from aiohttp_cors import CorsViewMixin

from models.sensors import Temperature


class TempView(View, CorsViewMixin):
    """
    Temperature view
    """

    async def get(self):
      """ Return JSON with the current temperature reading """
      return json_response(await Temperature.all_readings())

    # TODO: Define and implement rest of functions for view