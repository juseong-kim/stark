import serial
from serial.tools import list_ports
import time
ports = list_ports.comports()
bases = []

for i, p in enumerate(ports):
    if 'usbserial' in p[0]:
        print(p[0])
        ser = serial.Serial(p[0], baudrate=115200, timeout=1)
        ser.write(b"AT+RST\r\n")
        time.sleep(0.05)
        print(i % 3)
        for n in range(2):
            tag = f"AT+anchor_tag=1,{i%3}\r\n"
            ser.write(tag.encode())
            time.sleep(0.05)
        x = ser.readlines()
        print(x)
