from evdev import InputDevice, categorize, ecodes, KeyEvent
import serial
ser = serial.Serial('COM4', 9800, timeout=1)
gamepad = InputDevice('/dev/input/event7')

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        keyevent = categorize(event)
        # print(event)
        if keyevent.keystate == KeyEvent.key_down:
            if keyevent.scancode == 308:
             print('Square')
             ser.write(b"H")
            elif keyevent.scancode == 307:
             print('Triangle')
             ser.write(b"L")
            elif keyevent.scancode == 305:
             print('Round')
            elif keyevent.scancode == 304:
             print('Cross') """
	  #  print(keyevent.scancode)
        
