import sys
import struct
import serial

path = '/home/pi/python_test/RasPiUART/test.txt'

with open(path, 'rb') as f:
    s = f.read()

print(s)
port = serial.Serial(
            port = "/dev/ttyAMA0", 
            baudrate=2500000, 
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS,
            timeout = None
            )
#port = serial.Serial('/dev/ttyAMA0', 2500000)
port.write(s)
port.close
