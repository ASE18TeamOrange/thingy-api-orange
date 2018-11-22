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

    def run_temperature_service(self, name):
        key = self.__esd.temperatures(name)
        if key is not None:
            asyncio.ensure_future(self.__mqtt_client.temp_coro(self.__database, key))

    def run_pressure_service(self, name):
        key = self.__esd.pressures(name)
        if key is not None:
            asyncio.ensure_future(self.__mqtt_client.pressure_coro(self.__database, key))

    def run_humidity_service(self, name):
        key = self.__esd.humidities(name)
        if key is not None:
            asyncio.ensure_future(self.__mqtt_client.humidity_coro(self.__database, key))

    def run_gas_service(self, name):
        key = self.__esd.gases(name)
        if key is not None:
            asyncio.ensure_future(self.__mqtt_client.gas_coro(self.__database, key))
