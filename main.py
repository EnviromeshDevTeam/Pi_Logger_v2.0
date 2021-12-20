from Classes.enviromesh_logger import *
from Classes.mqttclient import MQTTCLIENT


# TODO: Loop readings with 15 second time.sleep
# TODO: Implement AWS IOT CORE Publish DATA
# * ^When publishing add timestamp as well

# TODO: Implement AWS IOT RULE to trigger An AWS Lambda
# TODO: AWS Lambda will take the data as an object and interact with our AWS RDS_SQL

Env_logger = Enviromesh_logger()
mqtt_Client = MQTTCLIENT()


if __name__ == '__main__':
    print("Initiating IoT Core Contact Topic")
    print(f"Publishing message for {mqtt_Client.clientID}")
    mqtt_Client.connect()
    while True:
        # public params/headers to send for mqtt_client publish method
        # ? @param topic - link publishing/subscriptions to equivalent topics
        # ? @param QoS - 0 or 1 (High Priority or Low)
        # ? @param payload - JSON Object of message
        mqtt_Client.publish(
            topic=f"{mqtt_Client.clientID}/PublishedData",
            payload={
                'temp': f'{Env_logger.getTemp()}',
                'humidity': f'{Env_logger.getHumidity()}',
                'co2': f'{Env_logger.getCO2()}',
                'tvoc': f'{Env_logger.getTVOC()}',
                'soil_moisture': f'{Env_logger.getMoisture()}',
                'timestamp': f'{Env_logger.getDT2Second()}'
            },
            QoS=1
        )
        time.sleep(15)  # Reset loop after 15 seconds
