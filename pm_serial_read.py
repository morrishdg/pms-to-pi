#!/usr/bin/env python
import time
import serial

import paho.mqtt.client as mqtt

#Connect to mqtt
client = mqtt.Client()
client.connect("localhost",1883)

#Trying to make a one place serial setup but not working

"""
def c():
    ser = serial.Serial(
        port='/dev/ttyS0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=1,
        bytesize=8,
        timeout=1
        )
    return ser
c()
"""
#Start Serial Link
ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=1,
    bytesize=8,
    timeout=1
    )

print(ser.name)

while 1:
    x1=ser.read(24)
#    print(x1)
    if x1[0]!= "B" and x1[1]!= "M":
        print(x1[0]," ",x1[1]," invalid byte")
        ser.close()
#        c()
        ser = serial.Serial(
            port='/dev/ttyS0',
            baudrate = 9600,
            parity=serial.PARITY_NONE,
            stopbits=1,
            bytesize=8,
            timeout=1
            )
        x1=ser.read(24)
    else:
#        print(x1)
        pm1a = (ord(x1[4])*256) + ord(x1[5])
        pm25a = (ord(x1[6])*256) + ord(x1[7])
        pm10a = (ord(x1[8])*256) + ord(x1[9])
        pm1b = (ord(x1[10])*256) + ord(x1[11])
        pm25b = (ord(x1[12])*256) + ord(x1[13])
        pm10b = (ord(x1[14])*256) + ord(x1[15])

        dat=("PM1:" + str(pm1a) + "PM2.5:" + str(pm25a) + "PM10:" + str(pm10a))
        print(dat)
        #print(pm10a.toint)
        #print("serial read pm2.5 type" + type(pm25a))
        
        
        client.publish("pm25", pm25a)