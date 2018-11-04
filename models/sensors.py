from ast import literal_eval
import json
from models.database import Database
class Temperature():
# Store temperature readings

    # database connection handle
    redis = Database()

    @classmethod
    async def all_readings(cls):
        """Get a list of all recorded temps"""

        readings = cls.redis.getList('temperature_series', 0, cls.redis.getListLength('temperature_series'))
        readings_json = []
        for item in readings:
            item_json = literal_eval(item.decode('utf8'))
            readings_json.append(item_json)

        return readings_json

    @classmethod
    async def last_reading(cls):
        """Get the most recent temp recording"""

        # Get last reading from list
        readings = cls.redis.getList('temperature_series', 0, cls.redis.getListLength('temperature_series'))
        most_recent_reading = readings[-1]
        reading_json = literal_eval(most_recent_reading.decode('utf8'))

        return reading_json
