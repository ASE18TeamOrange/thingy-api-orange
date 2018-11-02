import asyncio

from hbmqtt.client import MQTTClient, ClientException
from hbmqtt.mqtt.constants import QOS_1#, QOS_2


# Connection parameters
MQTT_BROKER_ADDR = 'mqtt://orange:164e089363@mqtt.thing.zone:1898'

# Thingy services and characteristics
THNGY_NAME = '4N0NsTlEBB0NBInNwPPq6w' # TODO: find a way to update this variable with the current thingy id

# Thingy configuration service
THNGY_CONFIG_UUID = 'ef680100-9b35-4933-9b10-52ffa9740042'
THNGY_CONFIG_NAME_UUID = 'ef680100-9b35-4933-9b10-52ffa9740042'

# Thingy environment service
THNGY_ENV_UUID = 'ef680200-9b35-4933-9b10-52ffa9740042'
THNGY_ENV_TMP_UUID = 'ef680201-9b35-4933-9b10-52ffa9740042'
THNGY_ENV_PRESS_UUID = 'ef680202-9b35-4933-9b10-52ffa9740042'
THNGY_ENV_HUMID_UUID = 'ef680203-9b35-4933-9b10-52ffa9740042'

# Thingy user interface service
THNGY_USR_INTERF_UUID = 'ef680300-9b35-4933-9b10-52ffa9740042'
THNGY_USR_INTERF_LED_UUID = 'ef680301-9b35-4933-9b10-52ffa9740042'
THNGY_USR_INTERF_BUTTON_UUID = 'ef680302-9b35-4933-9b10-52ffa9740042'

@asyncio.coroutine
def temp_coro():
    try:
        C = MQTTClient()
        yield from C.connect(MQTT_BROKER_ADDR)
        yield from C.subscribe([('%s/%s/%s' % (THNGY_NAME, THNGY_ENV_UUID, THNGY_ENV_TMP_UUID), QOS_1)])
        
        # yield from C.subscribe([('#', QOS_1)])

        for i in range(1, 10):
            message = yield from C.deliver_message()
            packet = message.publish_packet
            integer = packet.payload.data[0]
            decimal = packet.payload.data[1]
            temperature = integer + (decimal / 100)

            print("%d:  %s => %s" % (i, packet.variable_header.topic_name, str(temperature)))
        
        yield from C.unsubscribe([('%s/%s/%s' % (THNGY_NAME, THNGY_ENV_UUID, THNGY_ENV_TMP_UUID))])
        yield from C.disconnect()
    except ClientException as ce:
        print(ce)


@asyncio.coroutine
def pressure_coro():
    try:
        C = MQTTClient()
        yield from C.connect(MQTT_BROKER_ADDR)
        yield from C.subscribe([('%s/%s/%s' % (THNGY_NAME, THNGY_ENV_UUID, THNGY_ENV_PRESS_UUID), QOS_1)])
        
        # yield from C.subscribe([('#', QOS_1)])

        for i in range(1, 10):
            message = yield from C.deliver_message()
            packet = message.publish_packet
            # TODO: check the parsing of pressure data - it seems like wrong values (~180 instead of ~1000)
            integer = packet.payload.data[0]
            decimal = packet.payload.data[4]
            temperature = integer + (decimal / 100)

            print("%d:  %s => %s" % (i, packet.variable_header.topic_name, str(temperature)))
        
        yield from C.unsubscribe([('%s/%s/%s' % (THNGY_NAME, THNGY_ENV_UUID, THNGY_ENV_PRESS_UUID))])
        yield from C.disconnect()
    except ClientException as ce:
        print(ce)


@asyncio.coroutine
def humidity_coro():
    try:
        C = MQTTClient()
        yield from C.connect(MQTT_BROKER_ADDR)
        yield from C.subscribe([('%s/%s/%s' % (THNGY_NAME, THNGY_ENV_UUID, THNGY_ENV_HUMID_UUID), QOS_1)])
        
        # yield from C.subscribe([('#', QOS_1)])

        for i in range(1, 10):
            message = yield from C.deliver_message()
            packet = message.publish_packet
            humidity = packet.payload.data[0]

            print("%d:  %s => %s" % (i, packet.variable_header.topic_name, str(humidity)))
        
        yield from C.unsubscribe([('%s/%s/%s' % (THNGY_NAME, THNGY_ENV_UUID, THNGY_ENV_HUMID_UUID))])
        yield from C.disconnect()
    except ClientException as ce:
        print(ce)


if __name__ == '__main__':
    # Testing of different services
    # asyncio.get_event_loop().run_until_complete(temp_coro())
    # asyncio.get_event_loop().run_until_complete(pressure_coro())
    # asyncio.get_event_loop().run_until_complete(humidity_coro())
