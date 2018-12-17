from ast import literal_eval
import json
from models.database import Database


class Temperature:
# Store temperature readings

    # database connection handle
    redis = Database()

    @classmethod
    async def all_readings(cls, user):
        """Get a list of all recorded temps"""

        readings = cls.redis.get_set("%s:%s" % (user, 'temperature'), 0, -1)
        readings_json = []
        for item in readings:
            item_json = literal_eval(item.decode('utf8'))
            readings_json.append(item_json)

        return readings_json

    @classmethod
    async def last_reading(cls, user):
        """Get the most recent temp recording"""

        # Get last reading from list
        readings = cls.redis.get_set("%s:%s" % (user, 'temperature'), 0, -1)

        if len(readings) > 0:
            most_recent_reading = readings[-1]
            reading_json = literal_eval(most_recent_reading.decode('utf8'))
            return reading_json
        
        return None


class Pressure:
# Store pressure readings

    # database connection handle
    redis = Database()

    @classmethod
    async def all_readings(cls, user):
        """Get a list of all recorded pressures"""

        readings = cls.redis.get_set("%s:%s" % (user, 'pressure'), 0, -1)
        readings_json = []
        for item in readings:
            item_json = literal_eval(item.decode('utf8'))
            readings_json.append(item_json)

        return readings_json

    @classmethod
    async def last_reading(cls, user):
        """Get the most recent pressure recording"""

        # Get last reading from list
        readings = cls.redis.get_set("%s:%s" % (user, 'pressure'), 0, -1)
        
        if len(readings) > 0:
            most_recent_reading = readings[-1]
            reading_json = literal_eval(most_recent_reading.decode('utf8'))
            return reading_json
        
        return None


class Humidity:
# Store humidity readings

    # database connection handle
    redis = Database()

    @classmethod
    async def all_readings(cls, user):
        """Get a list of all recorded humidities"""

        readings = cls.redis.get_set("%s:%s" % (user, 'humidity'), 0, -1)
        readings_json = []
        for item in readings:
            item_json = literal_eval(item.decode('utf8'))
            readings_json.append(item_json)

        return readings_json

    @classmethod
    async def last_reading(cls, user):
        """Get the most recent humidity recording"""

        # Get last reading from list
        readings = cls.redis.get_set("%s:%s" % (user, 'humidity'), 0, -1)
        
        if len(readings) > 0:
            most_recent_reading = readings[-1]
            reading_json = literal_eval(most_recent_reading.decode('utf8'))
            return reading_json
        
        return None


class Gas:
# Store gas readings

    # database connection handle
    redis = Database()

    @classmethod
    async def all_readings(cls, user):
        """Get a list of all recorded gases"""

        readings = cls.redis.get_set("%s:%s" % (user, 'gas'), 0, -1)
        readings_json = []
        for item in readings:
            item_json = literal_eval(item.decode('utf8'))
            readings_json.append(item_json)

        return readings_json

    @classmethod
    async def last_reading(cls, user):
        """Get the most recent gas recording"""

        # Get last reading from list
        readings = cls.redis.get_set("%s:%s" % (user, 'gas'), 0, -1)
        
        if len(readings) > 0:
            most_recent_reading = readings[-1]
            reading_json = literal_eval(most_recent_reading.decode('utf8'))
            return reading_json
        
        return None


class Light:
# Store light readings

    # database connection handle
    redis = Database()

    @classmethod
    async def all_readings(cls, user):
        """Get a list of all recorded light"""

        readings = cls.redis.get_set("%s:%s" % (user, 'light'), 0, -1)
        readings_json = []
        for item in readings:
            item_json = literal_eval(item.decode('utf8'))
            readings_json.append(item_json)

        return readings_json

    @classmethod
    async def last_reading(cls, user):
        """Get the most recent light recording"""

        # Get last reading from list
        readings = cls.redis.get_set("%s:%s" % (user, 'light'), 0, -1)
        
        if len(readings) > 0:
            most_recent_reading = readings[-1]
            reading_json = literal_eval(most_recent_reading.decode('utf8'))
            return reading_json
        
        return None
