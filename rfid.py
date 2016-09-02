#! /usr/bin/python
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.8)
print("Port in use is " + ser.name)
line = ser.readline()
print (line.hex())
