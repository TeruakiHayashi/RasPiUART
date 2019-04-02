import sys
import struct
import serial

path = '/home/pi/python_test/RasPiUART/test.txt'

with open(path, 'rb') as f:
    s = f.read()

port = serial.Serial(
            port = "/dev/ttyS0", 
            baudrate=2.5*10^6, 
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS,
            timeout = None
            )

port.write(s)