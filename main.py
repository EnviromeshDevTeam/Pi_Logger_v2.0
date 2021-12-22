from Classes.enviromesh_logger import Enviromesh_logger
from Classes.mqttclient import MQTTCLIENT
import time
import sys
sys.path.append("..")

# TODO: Implement AWS IOT RULE to trigger An AWS Lambda
# TODO: AWS Lambda will take the data as an object and interact with our AWS RDS_SQL


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
            payload=Env_logger.getPayload(),
            QoS=0 #Changed to 0, Was working at 1 will test next iteration
        )
        time.sleep(15)  # Reset loop after 15 seconds
