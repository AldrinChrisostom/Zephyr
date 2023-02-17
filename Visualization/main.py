import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import numpy as np


def animate(dataList):

    try:
        arduinoData = np.array([[46, 45, 54, 45, 39, 40], [46, 45, random.randrange(90, 103), 45, 39, 40], [
                               43, 42, 43, 45, 39, 40], [46, 45, 54, 45, 39, 40], [46, 45, 54, 45, 39, 40], [46, 45, 54, 45, 39, 40]])
        dataList = arduinoData
    except:
        pass

    x_range = np.arange(6)
    y_range = np.arange(6)

    x, y = np.meshgrid(x_range, y_range)
    ax.clear()

    ax.plot_surface(x, y, dataList, rstride=1, cstride=1,
                    linewidth=2, antialiased=False, shade=True)

    ax.set_zlim([0, 130])
    ax.set_title("Arduino Data")


dataList = []


fig = plt.figure()
ax = fig.add_subplot(projection='3d')


time.sleep(2)


ani = animation.FuncAnimation(
    fig, animate, frames=100, fargs=(dataList), interval=100)

print("Hello")
plt.show()
