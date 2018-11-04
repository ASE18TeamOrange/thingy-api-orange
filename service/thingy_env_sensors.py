import mqtt.client
import asyncio
from models.environment import EnvironmentSensorData
from models.database import Database


class EnvironmentSensorDataService:
    __database = None
    __esd = None

    def __init__(self):
        self.__database = Database()
        self.__esd = EnvironmentSensorData()

    def run_temperature_service(self, name):
        key = self.__esd.temperatures(name)
        if key is not None:
            asyncio.get_event_loop().run_until_complete(mqtt.client.temp_coro(self.__database, key))

    def run_pressure_service(self, name):
        key = self.__esd.pressures(name)
        if key is not None:
            asyncio.get_event_loop().run_until_complete(mqtt.client.pressure_coro(self.__database, key))

    def run_humidity_service(self, name):
        key = self.__esd.humidities(name)
        if key is not None:
            asyncio.get_event_loop().run_until_complete(mqtt.client.humidity_coro(self.__database, key))