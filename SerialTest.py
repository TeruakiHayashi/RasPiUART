import serial
ser = serial.Serial('/dev/ttyAMA0',2500000)
ser.write("hello")
ser.close()
