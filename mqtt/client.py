import asyncio
from models.database import Database
from hbmqtt.client import MQTTClient, ClientException
from hbmqtt.mqtt.constants import QOS_0, QOS_1, QOS_2
from datetime import datetime
import logging


class MqttClient:
    # Connection parameters
    MQTT_BROKER_ADDR = 'mqtt://orange:164e089363@mqtt.thing.zone:1898'

    # Thingy services and characteristics
    THNGY_NAME = '_AFPEye74mPxrzSvFPWlYA'  # TODO: find a way to update this variable with the current thingy id

    # Thingy configuration service
    THNGY_CONFIG_UUID = 'ef680100-9b35-4933-9b10-52ffa9740042'
    THNGY_CONFIG_NAME_UUID = 'ef680101-9b35-4933-9b10-52ffa9740042'

    # Thingy environment service
    THNGY_ENV_UUID = 'ef680200-9b35-4933-9b10-52ffa9740042'
    THNGY_ENV_TMP_UUID = 'ef680201-9b35-4933-9b10-52ffa9740042'
    THNGY_ENV_PRESS_UUID = 'ef680202-9b35-4933-9b10-52ffa9740042'
    THNGY_ENV_HUMID_UUID = 'ef680203-9b35-4933-9b10-52ffa9740042'
    THNGY_ENV_GAS_UUID = 'ef680204-9b35-4933-9b10-52ffa9740042'
    THNGY_ENV_LIGHT_UUID = 'ef680205-9b35-4933-9b10-52ffa9740042'

    # Thingy user interface service
    THNGY_USR_INTERF_UUID = 'ef680300-9b35-4933-9b10-52ffa9740042'
    THNGY_USR_INTERF_LED_UUID = 'ef680301-9b35-4933-9b10-52ffa9740042'
    THNGY_USR_INTERF_BUTTON_UUID = 'ef680302-9b35-4933-9b10-52ffa9740042'

    @asyncio.coroutine
    def temp_coro(self, database, key):
        try:
            C = MQTTClient()
            yield from C.connect(self.MQTT_BROKER_ADDR)
            yield from C.subscribe([('%s/%s/%s' % (self.THNGY_NAME, self.THNGY_ENV_UUID, self.THNGY_ENV_TMP_UUID), QOS_1)])

            # yield from C.subscribe([('#', QOS_1)])

            for i in range(1, 5):
                message = yield from C.deliver_message()
                packet = message.publish_packet
                integer = packet.payload.data[0]
                decimal = packet.payload.data[1]
                temperature = integer + (decimal / 100)
                date = str(datetime.now())

                print("%d:  %s => %s" % (i, packet.variable_header.topic_name, str(temperature)))

                data = {
                    'temperature': temperature,
                    'date': date
                }
                print(data)
                print("key: ", key)
                database.enqueue(key, data)

            yield from C.unsubscribe([('%s/%s/%s' % (self.THNGY_NAME, self.THNGY_ENV_UUID, self.THNGY_ENV_TMP_UUID))])
            yield from C.disconnect()

        except ClientException as ce:
            print(ce)

        readings = database.get_list('temperature_series', 0, database.get_list_length('temperature_series'))
        for read in readings:
            print("IM BAKK ", read)

    @asyncio.coroutine
    def pressure_coro(self, database, key):
        try:
            C = MQTTClient()
            yield from C.connect(self.MQTT_BROKER_ADDR)
            yield from C.subscribe([('%s/%s/%s' % (self.THNGY_NAME, self.THNGY_ENV_UUID, self.THNGY_ENV_PRESS_UUID), QOS_1)])

            # yield from C.subscribe([('#', QOS_1)])

            for i in range(1, 5):
                message = yield from C.deliver_message()
                packet = message.publish_packet
                # TODO: check the parsing of pressure data - it seems like wrong values (~180 instead of ~1000)

                integer = packet.payload.data[0]
                decimal = packet.payload.data[4]
                pressure = integer + (decimal / 100.0)
                date = str(datetime.now())

                print("%d:  %s => %s" % (i, packet.variable_header.topic_name, str(pressure)))

                data = {
                    'pressure': pressure,
                    'date': date
                }
                print(data)
                database.enqueue(key, data)

            yield from C.unsubscribe([('%s/%s/%s' % (self.THNGY_NAME, self.THNGY_ENV_UUID, self.THNGY_ENV_PRESS_UUID))])
            yield from C.disconnect()
        except ClientException as ce:
            print(ce)
        
        readings = database.get_list('pressure_series', 0, database.get_list_length('pressure_series'))
        for read in readings:
            print("IM BAKK ", read)

    @asyncio.coroutine
    def humidity_coro(self, database, key):
        try:
            C = MQTTClient()
            yield from C.connect(self.MQTT_BROKER_ADDR)
            yield from C.subscribe([('%s/%s/%s' % (self.THNGY_NAME, self.THNGY_ENV_UUID, self.THNGY_ENV_HUMID_UUID), QOS_1)])

            # yield from C.subscribe([('#', QOS_1)])

            for i in range(1, 10):
                message = yield from C.deliver_message()
                packet = message.publish_packet
                humidity = packet.payload.data[0]
                date = str(datetime.now())

                print("%d:  %s => %s" % (i, packet.variable_header.topic_name, str(humidity)))

                data = {
                    'humidity': humidity,
                    'date': date
                }
                print(data)
                database.enqueue(key, data)

            yield from C.unsubscribe([('%s/%s/%s' % (self.THNGY_NAME, self.THNGY_ENV_UUID, self.THNGY_ENV_HUMID_UUID))])
            yield from C.disconnect()
        except ClientException as ce:
            print("Error while running coroutine: ", ce)
        
        readings = database.get_list('humidity_series', 0, database.get_list_length('humidity_series'))
        for read in readings:
            print("IM BAKK ", read)

    @asyncio.coroutine
    def gas_coro(self, database, key):
        try:
            C = MQTTClient()
            yield from C.connect(self.MQTT_BROKER_ADDR)
            yield from C.subscribe([('%s/%s/%s' % (self.THNGY_NAME, self.THNGY_ENV_UUID, self.THNGY_ENV_GAS_UUID), QOS_1)])

            # yield from C.subscribe([('#', QOS_1)])

            for i in range(1, 10):
                message = yield from C.deliver_message()
                packet = message.publish_packet
                gas = {
                'eco2': packet.payload.data[0],
                'tvoc': packet.payload.data[2]
                }
                date = str(datetime.now())

                print("%d:  %s => %s" % (i, packet.variable_header.topic_name, str(gas)))

                data = {
                    'gas': gas,
                    'date': date
                }
                print(data)
                database.enqueue(key, data)

            yield from C.unsubscribe([('%s/%s/%s' % (self.THNGY_NAME, self.THNGY_ENV_UUID, self.THNGY_ENV_GAS_UUID))])
            yield from C.disconnect()
        except ClientException as ce:
            print("Error while running coroutine: ", ce)
        
        readings = database.get_list('gas_series', 0, database.get_list_length('gas_series'))
        for read in readings:
            print("IM BAKK ", read)

    @asyncio.coroutine
    def light_coro(self, database, key):
        try:
            C = MQTTClient()
            yield from C.connect(self.MQTT_BROKER_ADDR)
            yield from C.subscribe([('%s/%s/%s' % (self.THNGY_NAME, self.THNGY_ENV_UUID, self.THNGY_ENV_LIGHT_UUID), QOS_1)])

            # yield from C.subscribe([('#', QOS_1)])

            for i in range(1, 10):
                message = yield from C.deliver_message()
                packet = message.publish_packet
                color = {
                'red':  packet.payload.data[0],
                'green': packet.payload.data[2],
                'blue': packet.payload.data[4],
                'clear': packet.payload.data[6]
                }
                date = str(datetime.now())

                print("%d:  %s => %s" % (i, packet.variable_header.topic_name, str(color)))

                data = {
                    'color': color,
                    'date': date
                }
                print(data)
                database.enqueue(key, data)

            yield from C.unsubscribe([('%s/%s/%s' % (self.THNGY_NAME, self.THNGY_ENV_UUID, self.THNGY_ENV_LIGHT_UUID))])
            yield from C.disconnect()
        except ClientException as ce:
            print("Error while running coroutine: ", ce)
        
        readings = database.get_list('light_series', 0, database.get_list_length('light_series'))
        for read in readings:
            print("IM BAKK ", read)

    @asyncio.coroutine
    def button_coro(self):
        try:
            C = MQTTClient()
            yield from C.connect(self.MQTT_BROKER_ADDR)
            yield from C.subscribe([('%s/%s/%s' % (self.THNGY_NAME, self.THNGY_USR_INTERF_UUID, self.THNGY_USR_INTERF_BUTTON_UUID), QOS_1)])

            for i in range(10):
                message = yield from C.deliver_message()
                packet = message.publish_packet
                if packet.payload.data:
                    print("Button pressed")
                else:
                    print("Button not pressed")

            yield from C.unsubscribe([('%s/%s/%s' % (self.THNGY_NAME, self.THNGY_USR_INTERF_UUID, self.THNGY_USR_INTERF_BUTTON_UUID))])
            yield from C.disconnect()
        except ClientException as ce:
            print(ce)


    @asyncio.coroutine
    def get_thingy_name(self):
        try:
            C = MQTTClient()
            yield from C.connect(self.MQTT_BROKER_ADDR)
            yield from C.subscribe([('%s/%s/%s' % (self.THNGY_NAME, self.THNGY_CONFIG_UUID, self.THNGY_CONFIG_NAME_UUID), QOS_1)])
            message = yield from C.publish('%s/%s/%s/read' % (self.THNGY_NAME, self.THNGY_CONFIG_UUID, self.THNGY_CONFIG_NAME_UUID), b'read', qos=QOS_1)
            response = yield from C.deliver_message()
            packet = response.publish_packet

            print("%s => %s" % (packet.variable_header.topic_name, response.data.decode("ascii")))
            yield from C.unsubscribe([('%s/%s/%s' % (self.THNGY_NAME, self.THNGY_CONFIG_UUID, self.THNGY_CONFIG_NAME_UUID))])
            yield from C.disconnect()
        except ClientException as ce:
            pass


    @asyncio.coroutine
    def get_led_vals_coro(self):
        try:
            C = MQTTClient()
            yield from C.connect(self.MQTT_BROKER_ADDR)
            yield from C.subscribe([('%s/%s/%s' % (self.THNGY_NAME, self.THNGY_USR_INTERF_UUID, self.THNGY_USR_INTERF_LED_UUID), QOS_1)])
            message = yield from C.publish('%s/%s/%s/read' % (self.THNGY_NAME, self.THNGY_USR_INTERF_UUID, self.THNGY_USR_INTERF_LED_UUID), b'read', qos=QOS_1)
            response = yield from C.deliver_message()
            print(list(response.data))
            yield from C.unsubscribe([('%s/%s/%s' % (self.THNGY_NAME, self.THNGY_USR_INTERF_UUID, self.THNGY_USR_INTERF_LED_UUID))])
            yield from C.disconnect()
        except ClientException as ce:
            pass




    #if __name__ == '__main__':
        # Logging
        # formatter = "[%(asctime)s] %(name)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
        # logging.basicConfig(level=logging.DEBUG, format=formatter)

        # Testing of different services
        # asyncio.get_event_loop().run_until_complete(get_thingy_name())
        # asyncio.get_event_loop().run_until_complete(get_led_vals_coro())
        # asyncio.get_event_loop().run_until_complete(temp_coro())
        # asyncio.get_event_loop().run_until_complete(button_coro())
        # asyncio.get_event_loop().run_until_complete(pressure_coro())
        # asyncio.get_event_loop().run_until_complete(humidity_coro())
