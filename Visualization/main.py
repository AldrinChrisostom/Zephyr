import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
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
    try:
        data = []

        for i in range(tx):
            arduinoDataString = ser.readline().decode()
            formattedString = arduinoDataString.split(",")
            formattedString[-1] = formattedString[-1].replace("$\r\n","")

            formattedValues = [int(x) for x in formattedString[1:]]

            if(re.search("\*\d\*",formattedString[0])): 
                data.append(formattedValues) 
            else:
                print("Data Error")
                data.append([0] * (rx ))
            
        return (data)
    except:
        return ([])

def animate(dataList):


    dataList = np.array(readSerial())
    print(dataList)


    x_range = np.arange(len(dataList))
    y_range = np.arange(len(dataList))

    x, y = np.meshgrid(x_range, y_range)
    ax.clear()

    ax.plot_surface(x, y, dataList)

    ax.set_zlim([0, 130])
    ax.set_title("Arduino Data")




fig = plt.figure()
ax = fig.add_subplot(projection='3d')


time.sleep(2)

dataList = []

ani = animation.FuncAnimation(
    fig, animate, frames=100, fargs=(dataList), interval=100)

plt.show()


