from requests.models import Response
from Classes.enviromesh_logger import Enviromesh_logger
from Classes.mqttclient import MQTTCLIENT
import requests #!Remember to remove if ever change stack
import time  # used for allowing set pause times between script actions
from dotenv import load_dotenv, find_dotenv
import sys
import os
sys.path.append("..")

# TODO: Implement AWS IOT RULE to trigger An AWS Lambda
# TODO Post an env.example to the git repo


load_dotenv(find_dotenv())
    
if __name__ == '__main__':
    print("Initiating IoT Core Contact Topic")
    Env_logger = Enviromesh_logger()
    mqtt_Client = MQTTCLIENT()
    print(f"Publishing message for {str(mqtt_Client)}")
    mqtt_Client.client.connect()
    while True:
        # public params/headers to send for mqtt_client publish method
        # ? @param topic - link publishing/subscriptions to equivalent topics
        # ? @param QoS - 0 or 1 (High Priority or Low)
        # ? @param payload - JSON Object of message
        mqtt_Client.client.publish(
            topic=str(mqtt_Client),
            payload=Env_logger.getPayload(1),
            QoS=0 #Changed to 0, Was working at 1 will test next iteration
        )
        time.sleep(30)  # Reset loop after 30 seconds This means our data is close to live with a lag of 30 seconds
