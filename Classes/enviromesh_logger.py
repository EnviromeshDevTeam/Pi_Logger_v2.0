import time
import board
import busio
import adafruit_ccs811 as CCS811
import adafruit_bme280 as BME280
import adafruit_ads1x15.ads1115 as ADC
from adafruit_ads1x15.analog_in import Moist_Analog_In


# *Immutable i2c registry addresses (:hex)
CSS811_addr: str = "0x5a"
BME280_addr: str = "0x77"
moist_Address: str = "0x48" 
# Named Differently because its a serial module so can only be interfaced by ADC converter


class Enviromesh_logger:
    def __init__(self) -> None:
        pass
