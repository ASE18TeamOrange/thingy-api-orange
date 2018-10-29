import paho.mqtt.client as mqtt


def get_connection():
        broker_address = "192.168.1.184"
        client = mqtt.Client("P1")  # create new instance
        client.connect(broker_address)  # connect to broker
        return client
