pinNumber = [3, 5, 6, 7, 11]
pin = [None, None, None, None, None]
try:
	board = Arduino('/dev/ttyACM3')
	for i in range(5):
		board.servo_config(pinNumber[i], angle=90)
		# Caution: Don't use board.get_pin('d:*:s') as it calls servo_config method with angle=0, which damages your servo.
		pin[i] = board.digital[pinNumber[i]]
except Exception as e:
	pin[0].write(80)

