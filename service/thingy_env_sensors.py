import mqtt.client
import asyncio
from models.environment import EnvironmentSensorData
from models.database import Database
from mqtt.client import MqttClient


class EnvironmentSensorDataService:
    __database = None
    __esd = None
    __mqtt_client = None

    def __init__(self):
        self.__database = Database()
        self.__esd = EnvironmentSensorData()
        self.__mqtt_client = MqttClient()

    def run_temperature_service(self, thingy, user, name):
        key = self.__esd.temperatures(user, name)
        if key is not None:
            asyncio.ensure_future(self.__mqtt_client.temp_coro(self.__database, thingy, key))

    def run_pressure_service(self, thingy, user, name):
        key = self.__esd.pressures(user, name)
        if key is not None:
            asyncio.ensure_future(self.__mqtt_client.pressure_coro(self.__database, thingy, key))

    def run_humidity_service(self, thingy, user, name):
        key = self.__esd.humidities(user, name)
        if key is not None:
            asyncio.ensure_future(self.__mqtt_client.humidity_coro(self.__database, thingy, key))

    def run_gas_service(self, thingy, user, name):
        key = self.__esd.gases(user, name)
        if key is not None:
            asyncio.ensure_future(self.__mqtt_client.gas_coro(self.__database, thingy, key))
    
    def run_light_service(self, thingy, user, name):
        key = self.__esd.lights(user, name)
        if key is not None:
            asyncio.ensure_future(self.__mqtt_client.light_coro(self.__database, thingy, key))
