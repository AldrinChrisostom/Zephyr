import serial
import time
import re

tx = 5
rx = 5


try:
    ser = serial.Serial("COM8", 9600)
except:
    print("Serial Port Error")

def readSerial():

    data = []

    for i in range(tx):
        arduinoData_string = ser.readline().decode()
        formattedString = arduinoData_string.split(",")
        formattedString[-1] = formattedString[-1].replace("$\r\n","")

        if(re.search("\*\d\*",formattedString[0])): 
            data.append(formattedString[1:]) 
        else:
            print("Data Error")
            data.append([0] * (rx - 1))
        
    return (data)


if(ser):
    print(readSerial())
