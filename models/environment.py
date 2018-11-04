from models.database import Database

class EnvironmentSensorData:

    __temp = "temp"
    __pressure = "pressure"
    __humidity = "humidity"

    __database = None

    def __init__(self):
        self.__database = Database()

    def __get_key(self, name, measure):
        return name + '#' + measure

    #todo we need to have a strategy: overwrite or not if key present??. Currently it will overwrite
    def temperatures(self, name):
        key = 'temperature_series' #self.__get_key(name, self.__temp)
        #if not self.exists(key):
        #    self.__database.insert(key)
        return key


    def pressures(self, name):
        key = self.__get_key(name, self.__pressure)
        if not self.exists(key):
            self.__database.insert(key)
        return key


    def humidities(self, name):
        key = self.__get_key(name, self.__humidity)
        if not self.exists(key):
            self.__database.insert(key)
        return key


    def exists(self, key):
        series = self.__database.get(key)
        if series is not None:
            return True
        return False

    def delete(self, key):
        if self.exists(key):
            self.__database.delete(key)
            return True
        return False
