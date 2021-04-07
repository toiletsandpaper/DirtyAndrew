from evdev import InputDevice, categorize, ecodes, KeyEvent
gamepad = InputDevice('/dev/input/event1')

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        keyevent = categorize(event)
        # print(event)
        if keyevent.keystate == KeyEvent.key_down:
            if keyevent.scancode == 306:
             print('B')
            elif keyevent.scancode == 307:
             print('Y')
            elif keyevent.scancode == 305:
             print('A')
            elif keyevent.scancode == 304:
             print('X')
	  #  print(keyevent.scancode)
