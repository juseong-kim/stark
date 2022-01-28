import serial
from serial.tools import list_ports
import time
ports = list_ports.comports()
port = ports[-1][0]
print(port)


ser = serial.Serial(port, baudrate=115200, timeout=1)


cmds = [b"AT+RST\r\n", b"AT+anchor_tag=0\r\n",
        b"AT+interval=5\r\n",
        b"AT+switchdis=1\r\n",
        b"AT+RST"]
for cmd in cmds:
    ser.write(cmd)
    x = ser.readlines()
    print(x)


while True:
    x = ser.readlines()
    if len(x) > 0:
        print(x)
    # inp = input("enter: ")
    # if len(inp)>0:
    #     ser.write((inp+'\r\n').encode())
