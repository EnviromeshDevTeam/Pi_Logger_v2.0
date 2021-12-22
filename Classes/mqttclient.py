from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

# TODO: TEST IF DOTENV WORKS

# * Uses a library that searches each parent until root and until a .env is found
# ! User will have to custom fillout the env.example template with their own AWS Thing credentials
# TODO Post an env.example to the git repo


#TODO: See if we can get this class to fully inherit from MQTTLib or AWSIoTMQTTClient
class MQTTCLIENT():
    def __init__(self) -> None:
        # random string, helps maintain same key connections
        self.client: AWSIoTMQTTClient = AWSIoTMQTTClient(os.getenv("DEVICE1KEY"))
        # TODO: Everything below might need to be put in function that activates AFTER object creation
        self.mqttStartUp()
    
    #string magic method when object or class name is called directly
    def __str__(self) -> str:
        if self.client != None:
            return os.getenv("DEVICE1KEY")
        else:
            return None

    def mqttStartUp(self)->None:
        """[summary]
        Function Called and activated inside init calls on methods to interact with the instantiated client object
        """        
        #Had some problems inheriting the SDK MQTT Client so we are just making a standalone assigning method
        self.client.configureEndpoint(os.getenv("DEVICE1ENDPOINT"),  # Specify AWS endpoint and Port Num
                               int(os.getenv("DEVICE1ENDPORT")))
        # Specify location of certificates
        self.client.configureCredentials(
            os.getenv("DEVICE1CERT1"),
            os.getenv("DEVICE1CERT2"),
            os.getenv("DEVICE1CERT3")
            # os.getenv("Device1Credentials"["PUBKEY"]),
        )
        self.client.configureOfflinePublishQueueing = int(os.getenv(
            "DEVICE1Q"))  # Infinite offline publishing queue

        self.client.configureDrainingFrequency = int(os.getenv(
            "DEVICE1DFREQ"))  # Draining: 2hz - Frequency

        # Connect Disconnect Timeout after Specified seconds
        self.client.configureConnectDisconnectTimeout = int(
            os.getenv("DEVICE1TIMEOUT"))


        self.client.configureMQTTOperationTimeout = int(os.getenv(
            "DEVICE1OPTIMEOUT"))  # Operation timeout after 5