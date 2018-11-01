import asyncio

from hbmqtt.client import MQTTClient, ClientException
from hbmqtt.mqtt.constants import QOS_1#, QOS_2


# Connection parameters
MQTT_BROKER_ADDR = 'mqtt://orange:164e089363@mqtt.thing.zone:1898'

# Thingy services and characteristics
THNGY_NAME = 'fQolqRNUGA2e8mECtW_24w'

# Thingy configuration service
THNGY_CONFIG_SERVICE = 'ef680100-9b35-4933-9b10-52ffa9740042'

# Thingy environment service
THNGY_ENV_SERVICE = 'ef680200-9b35-4933-9b10-52ffa9740042'
THNGY_ENV_TMP_SERVICE = 'ef680201-9b35-4933-9b10-52ffa9740042'

@asyncio.coroutine
def uptime_coro():
    try:
        C = MQTTClient()
        yield from C.connect(MQTT_BROKER_ADDR)
        yield from C.subscribe([('%s/%s/%s' % (THNGY_NAME, THNGY_ENV_SERVICE, THNGY_ENV_TMP_SERVICE), QOS_1)])
        # yield from C.subscribe([('#', QOS_1)])

        for i in range(1, 100):
            message = yield from C.deliver_message()
            packet = message.publish_packet

            integer = packet.payload.data[0]
            decimal = packet.payload.data[1]
            temperature = integer + (decimal / 100)

            print("%d:  %s => %s" % (i, packet.variable_header.topic_name, str(temperature)))
        
    except ClientException as ce:
        print(ce)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(uptime_coro())
