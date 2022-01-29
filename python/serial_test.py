import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import serial

# Create figure for plotting
fig, ax = plt.subplots(1, 1)
xs = []
ys = []
iarr = []


def animate(i, xs, ys):
    # Aquire and parse data from serial port
    y = np.random.rand()
    x = np.random.rand()
    iarr.append(i)

    xs.append(x)
    ys.append(y)

    xs = xs[-5:]
    ys = ys[-5:]

    ax.clear()
    ax.plot(xs, ys, marker='o')

    plt.title('Tag Location')


if __name__ == "__main__":
    # # initialize serial port
    # ser = serial.Serial()
    # ser.port = '/dev/ttyACM0'  # Arduino serial port
    # ser.baudrate = 115200
    # ser.timeout = 10  # specify timeout when using readline()
    # ser.open()
    # if ser.is_open == True:
    #     print(ser, "\n")  # print serial parameters

    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=200)
    plt.show()
