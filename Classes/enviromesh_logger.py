import time  # used for allowing set pause times between script actions
import board  # to reference pins and locations of the microcontroller(pi)
import busio  # busio responsible for bus communication such as i2c and SPI comms

# CO2/Contaminants in air sensing
from adafruit_ccs811 import CCS811
# Temperature/Humidity/Barometric Pressure/Altitude Sensing
import adafruit_bme280.basic as BME280
# Analog to Digital Converter
import adafruit_ads1x15.ads1115 as ADC
# Analag/Serial in import symbiotic relationship with the ADC
from adafruit_ads1x15.analog_in import AnalogIn


# *Immutable i2c registry addresses (:hex)
# ! - sudo i2cdetect -y 1
# ^Grabs the hex codes of all of these (Upon checking class docs it appears these are default args anyways. Oh well its good to be extra careful)
CSS811_addr: hex = 0x5a
BME280_addr: hex = 0x77
# Named Differently because its a serial module so can only be interfaced by ADC converter
moist_addr: hex = 0x48

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
        self.adc = ADC(self.i2c_bus)

        # * Our Channel reference on the ADC because there are up to 4 analog channels to map sensors onto
        self.analog0_moist = AnalogIn(self.adc, ADC.P0)

    def getTemp(self) -> int:
        print(self.bme280._read_temperature())
        return self.bme280._read_temperature()

    def getHumidity(self) -> float:
        print(self.bme280.relative_humidity)
        return self.bme280.relative_humidity

    def getCO2(self) -> int:
        print(self.ccs811.eco2)
        return self.ccs811.eco2

    def getTVOC(self) -> int:
        print(self.ccs811.eco2)
        return self.ccs811.eco2

    # TODO: Change Return Type
    def getMoisture(self) -> tuple(int, int):
        return (self.analog0_moist.value, self.analog0_moist.voltage)
