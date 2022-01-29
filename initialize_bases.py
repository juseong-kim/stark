import serial
from serial.tools import list_ports
ports = list_ports.comports()
bases = []

for i, p in enumerate(ports):
    if 'usbserial' in p[0]:
        print(p[0])
        ser = serial.Serial(p[0], baudrate=115200, timeout=1)
        ser.write(b"AT+RST\r\n")
        ser.write(b"AT+anchor_tag=1,\r\n")
        ser.write(i % 2)
        ser.write(b"\r\n")
        ser.write(b"AT+RST\r\n")
        x = ser.readlines()
        print(x)
