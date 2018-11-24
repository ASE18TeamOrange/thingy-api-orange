from models.database import Database


class EnvironmentSensorData:

    __temp = "temperature_series"
    __pressure = "pressure_series"
    __humidity = "humidity_series"
    __gas = "gas_series"
    __light = "light_series"

    __database = None

    def __init__(self):
        self.__database = Database()

    def __get_key(self, name, measure):
        return name + '#' + measure

    #todo we need to have a strategy: overwrite or not if key present??. Currently it will overwrite
    def temperatures(self, name):
        key = 'temperature_series'
        # key = self.__get_key(name, self.__temp)
        # if not self.exists(key):
        #     self.__database.insert(key, [])
        print("keyy: ",key)
        return key


    def pressures(self, name):
        key = 'pressure_series'
        # key = self.__get_key(name, self.__pressure)
        # if not self.exists(key):
        #     self.__database.insert(key, [])
        print("keyy: ",key)
        return key


    def humidities(self, name):
        key = 'humidity_series'
        # key = self.__get_key(name, self.__humidity)
        # if not self.exists(key):
        #     self.__database.insert(key, [])
        return key

    def gases(self, name):
        key = 'gas_series'
        # key = self.__get_key(name, self.__gas)
        # if not self.exists(key):
        #     self.__database.insert(key, [])
        return key
    
    def lights(self, name):
        key = 'light_series'
        # key = self.__get_key(name, self.__gas)
        # if not self.exists(key):
        #     self.__database.insert(key, [])
        return key


    def exists(self, key):
        return self.__database.exists(key)

    def delete(self, key):
        if self.exists(key):
            self.__database.delete(key)
            return True
        return False
