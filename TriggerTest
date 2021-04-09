from evdev import InputDevice, categorize, ecodes, KeyEvent
gamepad = InputDevice('/dev/input/event0')
for event in gamepad.read_loop():
  if event.type == ecodes.EV_ABS:
          absevent = categorize(event)
          print(event)
