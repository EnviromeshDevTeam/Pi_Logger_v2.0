from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

# TODO: TEST IF DOTENV WORKS

# ! Uses a library that searches each parent until root and until a .env is found
# ! User will have to custom fillout the env.example template with their own AWS Thing credentials
# TODO Post an env.example to the git repo

#! I have no idea if this is the right format (Also will this run?) If not assign to method to activate
_tempCred = os.getenv("DEVICE1CREDENTIALS").split(",")


class MQTTCLIENT(AWSIoTMQTTClient):
    def __init__(self) -> None:
        # random string, helps maintain same key connections
        self.clientID = os.getenv("DEVICE1KEY")
        # TODO: Everything below might need to be put in function that activates AFTER object creation
        self.configureEndpoint(os.getenv("DEVICE1ENDPOINT"),  # Specify AWS endpoint and Port Num
                               int(os.getenv("DEVICE1ENDPORT")))
        # Specify location of certificates
        self.configureCredentials(
            _tempCred[0],
            _tempCred[1],
            _tempCred[2]
            # os.getenv("Device1Credentials"["PUBKEY"]),
        )
        self.configureOfflinePublishQueueing = int(os.getenv(
            "DEVICE1Q"))  # Infinite offline publishing queue

        self.configureDrainingFrequency = int(os.getenv(
            "DEVICE1DFREQ"))  # Draining: 2hz - Frequency

        # Connect Disconnect Timeout after Specified seconds
        self.configureConnectDisconnectTimeout = int(
            os.getenv("DEVICE1TIMEOUT"))

        self.configureMQTTOperationTimeout = int(os.getenv(
            "DEVICE1OPTIMEOUT"))  # Operation timeout after 5
