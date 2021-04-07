from pyfirmata import Arduino, util
import time

board = Arduino('/dev/ttyACM0')
servo_pin = board.get_pin('d:6:s')
angle = 90
angle_s = input('a')
while True:
	angle = int(angle_s)
	servo_pin.write(angle)
	board.digital[13].write(1)
	board.digital[6].write(angle)
	time.sleep(1)
	board.digital[13].write(0)
	time.sleep(1)
