from evdev import InputDevice, categorize, ecodes, KeyEvent
gamepad = InputDevice('/dev/input/event7')

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        keyevent = categorize(event)
        print(event)
        if keyevent.keystate == KeyEvent.key_down:
            """ if keyevent.scancode == 308:
             print('Square')
            elif keyevent.scancode == 307:
             print('Triangle')
            elif keyevent.scancode == 305:
             print('Round')
            elif keyevent.scancode == 304:
             print('Cross') """
	  #  print(keyevent.scancode)
        
