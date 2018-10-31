import asyncio

from hbmqtt.client import MQTTClient, ClientException
from hbmqtt.mqtt.constants import QOS_1#, QOS_2


@asyncio.coroutine
def uptime_coro():
    try:
        C = MQTTClient()
        yield from C.connect('mqtt://orange:164e089363@mqtt.thing.zone:1898')
        yield from C.subscribe([
            ('#', QOS_1)
         ])

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
