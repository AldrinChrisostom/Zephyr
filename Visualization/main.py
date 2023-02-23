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


    # Read Data from Serial
    arduinoDataString = ser.readline().decode()
    # Make it into an array seperated by ; and remove the last item
    formattedString = arduinoDataString.split(";")[0:-1]

    formattedArray = []

    # For each array convert the elements into list and type from string to int
    for i in range(len(formattedString)):
        arrayElement = formattedString[i].split(',')
        arrayElement = [int(i) for i in arrayElement]

        formattedArray.append(arrayElement)
    
    # Fix this later

    # if(len(formattedString) != tx):
    #     raise Exception("Incorrect Data") 
   

    return (formattedArray)


def animate(dataList):

    dataFromArduino = []

    try:
        dataFromArduino = readSerial()
    except:
        dataFromArduino = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

    dataList = np.array(dataFromArduino)
    print(dataList)


    x_range = np.arange(len(dataList))
    y_range = np.arange(len(dataList))

    x, y = np.meshgrid(x_range, y_range)
    ax.clear()

    ax.plot_surface(x, y, dataList)

    ax.set_zlim([0, 500])
    ax.set_title("Arduino Data")




fig = plt.figure()
ax = fig.add_subplot(projection='3d')


time.sleep(2)

dataList = []

ani = animation.FuncAnimation(fig, animate, frames=100, fargs=(dataList), interval=100)
plt.show()


