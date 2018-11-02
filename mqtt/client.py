import asyncio
from models.database import Database
from hbmqtt.client import MQTTClient, ClientException
from hbmqtt.mqtt.constants import QOS_1#, QOS_2
from datetime import datetime

@asyncio.coroutine
def uptime_coro():
    try:
        C = MQTTClient()
        yield from C.connect('mqtt://orange:164e089363@mqtt.thing.zone:1898')
        yield from C.subscribe([
            ('wCTz0UmwOe5gKM17m5d_Fg/ef680200-9b35-4933-9b10-52ffa9740042/ef680201-9b35-4933-9b10-52ffa9740042', QOS_1)
         ])

        redis = Database()

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

            redis.enqueue('temperature_series', data)
    except ClientException as ce:
        print(ce)
    hund = redis.getList('temperature_series', 0, 3)
    print(hund)
    redis.delete('temperature_series')

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(uptime_coro())
