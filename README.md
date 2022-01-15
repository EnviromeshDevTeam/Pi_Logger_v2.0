# Pi_Logger_v2.0

<img src="./images/2021-01-12_Enviromesh_Full_Colour.svg" style="width: 100%; max-height= 300px"  >

Revamped Pi Logger: Built Around Test-Driven Development, Rasp-Pi with Arduino Sensors, AWS IOT Core, AWS Lambda to store to our AWS RDS SQL

<img src="./images/AWS_enviromesh-stack.png">

Using Raspberry Pi communication bus I2C to communicate with our sensors (BME280, CCS811, ADC-Analogue_Soil_Moisture_Sensor) to gather the data.

Requires: Custom Configuration with AWS IOT Core, Will add an env.example soon for example config plus mini AWS IoT Guide

For Pi OS:

(Download latest needed packages)
sudo pip3 install -r requirements.txt 

(Pings for sensors occupying the I2C bus and returns their hex address if detected)
sudo i2cdetect -y 1

Enviromesh Artwork/Logos designed by: Super snake - https://www.behance.net/Supersnaketate


