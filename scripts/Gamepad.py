from evdev import InputDevice, categorize, ecodes, KeyEvent
import serial
import time
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
gamepad = InputDevice('/dev/input/event9')

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        keyevent = categorize(event)
        #print(event)
        #if keyevent.keystate == KeyEvent.key_down:
        if event.value == 1:
            if keyevent.scancode == 306:
             print('B')
             ser.write(b"B")
            elif keyevent.scancode == 307:
             print('Y')
             ser.write(b"Y")
            elif keyevent.scancode == 305:
             print('A')
             ser.write(b"A")
            elif keyevent.scancode == 304:
             print('X')
             ser.write(b"X")
            elif event.code == 308:
             if event.value==1:
              print('L1')
              ser.write(b"L1")
            elif event.code == 309:
             if event.value==1:
              print('R1')
              ser.write(b"R1")
            elif event.code == 310:
             if event.value==1:
              print('L2')
              ser.write(b"L2")
            elif event.code == 311:
             if event.value==1:
              print('R2')
              ser.write(b"R2")
            elif event.code == 312:
             if event.value==1:
              print('Back')
              ser.write(b"Back")
            elif event.code == 313:
             if event.value==1:
              print('Start')
              ser.write(b"Start")
            elif event.code == 314:
             if event.value==1:
              print('Left Sosok')
              ser.write(b"LeftStick")
            elif event.code == 315:
             if event.value==1:
              print('Right Sosok')
              ser.write(b"RightStick")
	  #  print(keyevent.scancode)

    if event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        #if event.code == 1:
        #print(event)
        if event.code == 17:
           if event.value==-1:
              print('DPup')
              ser.write(b"DUp")
           elif event.value==1:
              print('DPdown')
              ser.write(b"DDown")
        elif event.code == 16:
           if event.value==1:
              print('DPright')
              ser.write(b"DRight")
           elif event.value==-1:
              print('DPleft')
              ser.write(b"DLeft")
        elif event.code == 1:
           if event.value>254:
              print('LSdown')
              ser.write(b"LSdown")
           elif event.value<1:
               print('LSup')
               ser.write(b"LSup")
        elif event.code == 0:
           if event.value>254:
              print('LSright')
              ser.write(b"LSright")
           elif event.value<1:
               print('LSleft')
               ser.write(b"LSleft")
        elif event.code == 5:
           if event.value>254:
              print('RSdown')
              ser.write(b"RSdown")
           elif event.value<1:
               print('RSup')
               ser.write(b"RSup")
        elif event.code == 2:
           if event.value>254:
              print('RSright')
              ser.write(b"RSright")
           elif event.value<1:
               print('RSleft')
               ser.write(b"RSleft")

    line = ser.readline().decode('utf-8').rstrip()
    print(line)             
    
