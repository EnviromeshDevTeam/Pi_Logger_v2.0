# Analag/Serial in import symbiotic relationship with the ADC
from adafruit_ads1x15.analog_in import AnalogIn
# Analog to Digital Converter
import adafruit_ads1x15.ads1115 as ADC
# Temperature/Humidity/Barometric Pressure/Altitude Sensing
import adafruit_bme280.basic as BME280
# CO2/Contaminants in air sensing
from adafruit_ccs811 import CCS811
import busio  # busio responsible for bus communication such as i2c and SPI comms
import board  # to reference pins and locations of the microcontroller(pi)
import datetime as dt
import time  # used for allowing set pause times between script actions
import sys
sys.path.append("..")


# *Immutable i2c registry addresses (:hex)
# ! - sudo i2cdetect -y 1
# ^Grabs the hex codes of all of these (Upon checking class docs it appears these are default args anyways. Oh well its good to be extra careful)
CSS811_addr: hex = 0x5A
BME280_addr: hex = 0x77
# Named Differently because its a serial module so can only be interfaced by ADC converter
moist_addr: hex = 0x48

# specify channel of adc to read values from
adc_channel: int = 0
# ADC GAIN - Edit to enable more precise ADC measurement
adc_GAIN: int = 1

'''
[summary]
Enviromesh_logger class in charge of logging all our different environment variables
'''


class Enviromesh_logger:

    def __init__(self) -> None:

        # * Our Method of communication protocol to communicate data to the Pi
        # ? @param board.SCL - Reference to Serial CLock of the board to keep i2c data grounded to a constant refresh or clock rate
        # ? @param board.SDA - Reference to the board's Serial DAta line for receiving data

        self.i2c_bus = busio.I2C(board.SCL, board.SDA)

        # * The Temperature/Humidity Sensor, Can also do Barometric pressure
        # * Temp measured in degrees celsius
        # * Humidity measured as a percentage of the air, ranging from 0-100
        self.bme280 = BME280.Adafruit_BME280_I2C(
            self.i2c_bus, address=BME280_addr)

        # * CO2/Contimants sensor mapping to bus and confirming its hardcoded registry address
        self.ccs811 = CCS811(self.i2c_bus, address=CSS811_addr)

        # * Our Analogue Digital converter parsing in the i2c bus to use
        # * This is used because our soil moisture sensor only does analog outputs
        # * Need to convert it to digital data
        self.adc = ADC.ADS1115(self.i2c_bus)

        # * Our Channel reference on the ADC because there are up to 4 analog channels to map sensors onto
        self.analog0_moist = AnalogIn(self.adc, ADC.P0)

    def getTemp(self) -> int:
        print(f"TEMP: {round(self.bme280.temperature)}")
        return round(self.bme280.temperature)

    def getHumidity(self) -> int:
        print(f"Humidity: {round(self.bme280.humidity)}")
        return round(self.bme280.humidity)

    def getCO2(self) -> int:
        #The ccs811 chip will send an 0 or 1 boolean if ready, we wait for this signal before retrieving value
        while not self.ccs811.data_ready:
            pass
        print(f"CO2: {self.ccs811.eco2}")
        return self.ccs811.eco2

    def getTVOC(self) -> int:
        #The ccs811 chip will send an 0 or 1 boolean if ready, we wait for this signal before retrieving value
        while not self.ccs811.data_ready:
            pass
        print(f"TVOC: {self.ccs811.tvoc}")
        return self.ccs811.tvoc

    def getMoisture(self)->int:
        _moistValue, _moistV = self.analog0_moist.value, self.analog0_moist.voltage
        print(f"Moisture: {_moistValue} with a voltage of {_moistV}")
        return _moistValue

    def getDT2Second(self)->str:
        """[summary]
        Get Current Datetime rounded to whole second
        Returns:
            str: formatted YEAR:MONTH:DAY:HOUR:MINUTE:SECOND #We Will design backend to easily parse this format
        """        
        return dt.datetime.utcnow().strftime('%Y%m%d%H%M%S')
    
    def getPayload(self)->str:
        return f"'temp':'{self.getTemp()}','humidity':'{self.getHumidity()}','CO2':'{self.getCO2()}','TVOC':'{self.getTVOC()}','Soil_Moisture':'{self.getMoisture()}','Timestamp':'{self.getDT2Second()}'"
