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

    def __get_key(self, user_id, measure):
        print("%s:%s" % (user_id, measure))
        return "%s:%s" % (user_id, measure)

    #todo we need to have a strategy: overwrite or not if key present??. Currently it will overwrite
    def temperatures(self, user, name):
        key = self.__get_key(user, name)
        print("keyy: ",key)
        return key


    def pressures(self, user, name):
        key = self.__get_key(user, name)
        print("keyy: ",key)
        return key


    def humidities(self, user, name):
        key = self.__get_key(user, name)
        print("keyy: ",key)
        return key

    def gases(self, user, name):
        key = self.__get_key(user, name)
        print("keyy: ",key)
        return key
    
    def lights(self, user, name):
        key = self.__get_key(user, name)
        print("keyy: ",key)
        return key


    def exists(self, key):
        return self.__database.exists(key)

    def delete(self, user, name):
        key = self.__get_key(user, name)
        if self.exists(key):
            self.__database.delete(key)
            return True
        return False
