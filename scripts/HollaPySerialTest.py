import serial

ser = serial.Serial("COM5", 9600, timeout=1)

ser.write(b'B')
