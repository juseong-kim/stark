import re
import serial
from serial.tools import list_ports
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

ports = list_ports.comports()
port = ports[-1][0]


fig, ax = plt.subplots(1, 1)
# ax, ax2 = ax

xs, ys, zs = [], [], []
t = []

dist_pattern = ":(.*?)m"


def triangulate(dists, U, Vx, Vy):
    # triangulate position from r1, r2 and r3
    r1, r2, r3 = dists
    x = (r1**2 - r2**2 + U**2)/(2*U)
    y = (r1**2 - r3**2 + Vx**2 + Vy**2 - 2*Vx*x)
    z = np.sqrt(r1**2 - x**2 - y**2)  # can be plus or minus with 3 bases

    return (x, y, z)


U = 1.2  # meters
Vx = 1.2/2
Vy = 1.2/2


def animate(i, t, xs, ys, zs):
    # Aquire and parse data from serial port
    dists = ser.readlines()

    dists = [float(re.search(dist_pattern, dist.decode()).group(1))
             for dist in dists]

    # steps += dists
    x, y, z = triangulate(dists, U, Vx, Vy)

    xs.append(x)
    ys.append(y)
    zs.append(z)

    xs = xs[-20:]
    ys = ys[-20:]
    zs = zs[-20:]

    t.append(i)
    print(f"x:{x},y:{y},z:{z}")

    ax.clear()
    # ax2.clear()
    # ax.scatter(t, steps)
    # ax2.scatter(t, steps)

    ax.plot(xs, ys, marker='o')
    # ax2.plot(t, zs)
    plt.ylim(-1, 3)
    plt.xlim(-1, 3)
    plt.title('Tag Location')


ser = serial.Serial(port, baudrate=115200, timeout=1)


cmds = [b"AT+RST\r\n", b"AT+anchor_tag=0\r\n",
        b"AT+interval=5\r\n",
        b"AT+switchdis=1\r\n",
        b"AT+RST"]
for cmd in cmds:
    ser.write(cmd)
    x = ser.readlines()
    print(x)


ani = animation.FuncAnimation(
    fig, animate, fargs=(t, xs, ys, zs,), interval=200)
plt.ylim(0, 5)
plt.xlim(0, 5)
plt.show()
