from ast import literal_eval
import json
from models.database import Database


class Temperature:
# Store temperature readings

    # database connection handle
    redis = Database()

    @classmethod
    async def all_readings(cls):
        """Get a list of all recorded temps"""

        readings = cls.redis.get_list('temperature_series', 0, cls.redis.get_list_length('temperature_series'))
        readings_json = []
        for item in readings:
            item_json = literal_eval(item.decode('utf8'))
            readings_json.append(item_json)

        return readings_json

    @classmethod
    async def last_reading(cls):
        """Get the most recent temp recording"""

        # Get last reading from list
        readings = cls.redis.get_list('temperature_series', 0, cls.redis.get_list_length('temperature_series'))
        most_recent_reading = readings[-1]
        reading_json = literal_eval(most_recent_reading.decode('utf8'))

        return reading_json


class Pressure:
# Store pressure readings

    # database connection handle
    redis = Database()

    @classmethod
    async def all_readings(cls):
        """Get a list of all recorded pressures"""

        readings = cls.redis.get_list('pressure_series', 0, cls.redis.get_list_length('pressure_series'))
        readings_json = []
        for item in readings:
            item_json = literal_eval(item.decode('utf8'))
            readings_json.append(item_json)

        return readings_json

    @classmethod
    async def last_reading(cls):
        """Get the most recent pressure recording"""

        # Get last reading from list
        readings = cls.redis.get_list('pressure_series', 0, cls.redis.get_list_length('pressure_series'))
        most_recent_reading = readings[-1]
        reading_json = literal_eval(most_recent_reading.decode('utf8'))

        return reading_json


class Humidity:
# Store humidity readings

    # database connection handle
    redis = Database()

    @classmethod
    async def all_readings(cls):
        """Get a list of all recorded humidities"""

        readings = cls.redis.get_list('humidity_series', 0, cls.redis.get_list_length('humidity_series'))
        readings_json = []
        for item in readings:
            item_json = literal_eval(item.decode('utf8'))
            readings_json.append(item_json)

        return readings_json

    @classmethod
    async def last_reading(cls):
        """Get the most recent humidity recording"""

        # Get last reading from list
        readings = cls.redis.get_list('humidity_series', 0, cls.redis.get_list_length('humidity_series'))
        most_recent_reading = readings[-1]
        reading_json = literal_eval(most_recent_reading.decode('utf8'))

        return reading_json


class Gas:
# Store gas readings

    # database connection handle
    redis = Database()

    @classmethod
    async def all_readings(cls):
        """Get a list of all recorded gases"""

        readings = cls.redis.get_list('gas_series', 0, cls.redis.get_list_length('gas_series'))
        readings_json = []
        for item in readings:
            item_json = literal_eval(item.decode('utf8'))
            readings_json.append(item_json)

        return readings_json

    @classmethod
    async def last_reading(cls):
        """Get the most recent gas recording"""

        # Get last reading from list
        readings = cls.redis.get_list('gas_series', 0, cls.redis.get_list_length('gas_series'))
        most_recent_reading = readings[-1]
        reading_json = literal_eval(most_recent_reading.decode('utf8'))

        return reading_json


class Light:
# Store light readings

    # database connection handle
    redis = Database()

    @classmethod
    async def all_readings(cls):
        """Get a list of all recorded light"""

        readings = cls.redis.get_list('light_series', 0, cls.redis.get_list_length('light_series'))
        readings_json = []
        for item in readings:
            item_json = literal_eval(item.decode('utf8'))
            readings_json.append(item_json)

        return readings_json

    @classmethod
    async def last_reading(cls):
        """Get the most recent light recording"""

        # Get last reading from list
        readings = cls.redis.get_list('light_series', 0, cls.redis.get_list_length('light_series'))
        most_recent_reading = readings[-1]
        reading_json = literal_eval(most_recent_reading.decode('utf8'))

        return reading_json