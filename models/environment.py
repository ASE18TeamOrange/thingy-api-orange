from models.database import Database

class EnvironmentSensorData:

    __temp = "temp"
    __pressure = "pressure"
    __humidity = "humidity"

    def __get_key(self, name, measure):
        return name + '#' + measure

    async def temperatures(self, name):
        redis = Database()
        key = self.__get_key(name, self.__temp)
        if not self.exists(key):
            redis.insert(key)
            return key
        return None

    async def pressures(self, name):
        redis = Database()
        key = self.__get_key(name, self.__pressure)
        if not self.exists(key):
            redis.insert(key)
            return key
        return None

    async def humidities(self, name):
        redis = Database()
        key = self.__get_key(name, self.__humidity)
        if not self.exists(key):
            redis.insert(key)
            return key
        return None

    async def exists(self, key):
        redis = Database()
        user = redis.get(key)
        if user is not None:
            return True
        return False
