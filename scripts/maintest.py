from datetime import datetime, timedelta
from pymata4 import pymata4
import sys
import keyboard
from evdev import InputDevice, categorize, ecodes, KeyEvent


gamepad = InputDevice('/dev/input/event0')
HALL_PINS = [22, 24, 26, 28]
DRIVER_1_PINS = [3, 8]   # left
DRIVER_2_PINS = [2, 9]   # right
DRIVER_3_PINS = [12, 13] # elevator


def setup_all_drivers(my_board):
    my_board.set_pin_mode_pwm_output(DRIVER_1_PINS[0])
    my_board.set_pin_mode_pwm_output(DRIVER_1_PINS[1])
    my_board.set_pin_mode_pwm_output(DRIVER_2_PINS[0])
    my_board.set_pin_mode_pwm_output(DRIVER_2_PINS[1])
    my_board.set_pin_mode_pwm_output(DRIVER_3_PINS[0])
    my_board.set_pin_mode_pwm_output(DRIVER_3_PINS[1])
    print('Drivers setted up')


def move_driver(my_board, driver_name, direction, speed):  # TODO: add speed and direction
    value_right = 0
    value_left = 0
    if direction == 'left':
        value_left = 1
    elif direction == 'right':
        value_right = 1
    if driver_name == 'left_driver':
        my_board.pwm_write(DRIVER_1_PINS[0], value_left * speed)
        my_board.pwm_write(DRIVER_1_PINS[1], value_right * speed)
    if driver_name == 'right_driver':
        my_board.pwm_write(DRIVER_2_PINS[0], value_left * speed)
        my_board.pwm_write(DRIVER_2_PINS[1], value_right * speed)
    if driver_name == 'elevator_driver':
        my_board.pwm_write(DRIVER_3_PINS[0], value_left * speed)
        my_board.pwm_write(DRIVER_3_PINS[1], value_right * speed)


def stop_driver(my_board, driver_name):
    if driver_name == 'left_driver':
        my_board.pwm_write(DRIVER_1_PINS[0], 0)
        my_board.pwm_write(DRIVER_1_PINS[1], 0)
        print('left driver moved')
    if driver_name == 'right_driver':
        my_board.pwm_write(DRIVER_2_PINS[0], 0)
        my_board.pwm_write(DRIVER_2_PINS[1], 0)
        print('right driver moved')
    if driver_name == 'elevator_driver':
        my_board.pwm_write(DRIVER_3_PINS[0], 0)
        my_board.pwm_write(DRIVER_3_PINS[1], 0)

def stop_all_drivers(my_board):
        my_board.pwm_write(DRIVER_1_PINS[0], 0)
        my_board.pwm_write(DRIVER_1_PINS[1], 0)
        my_board.pwm_write(DRIVER_2_PINS[0], 0)
        my_board.pwm_write(DRIVER_2_PINS[1], 0)
        my_board.pwm_write(DRIVER_3_PINS[0], 0)
        my_board.pwm_write(DRIVER_3_PINS[1], 0)

def servo_left(my_board, pin):
    my_board.set_pin_mode_servo(pin)
    my_board.servo_write(pin, 45)

def servo_right(my_board, pin):
    my_board.set_pin_mode_servo(pin)
    my_board.servo_write(pin, 135)

def servo_stop(my_board, pin)
    my_board.set_pin_mode_servo(pin)
    my_board.servo_write(pin, 90)



# def setup_all_hall(board)

def is_hall_active(my_board, hall_index):
    my_board.set_pin_mode_digital_input(HALL_PINS[hall_index])
    print(my_board.digital_read(HALL_PINS[hall_index]))
    value, time_stamp = my_board.digital_read(HALL_PINS[hall_index])
    # print(not value)
    return not value

i = False

if __name__ == "__main__":
    board = pymata4.Pymata4()
    setup_all_drivers(board)
    # timer = datetime.now()
    # deltatime = 0
    for event in gamepad.read_loop():
        if event.type == ecodes.EV_KEY:
            keyevent = categorize(event)
            #print(event)
            #if keyevent.keystate == KeyEvent.key_down:
            if event.value == 1 and i == False :
                if keyevent.scancode == 306:
                    move_driver(board, 'right_driver', 'right', 255)
                    if event.value == 0:
                        stop_driver(board, 'right_driver')
                    print('B')
                elif keyevent.scancode == 307:
                    print('Y')
                    i= True
                elif keyevent.scancode == 305:
                    stop_all_drivers(board)
                    print('A')
                elif keyevent.scancode == 304:
                    move_driver(board, 'left_driver', 'left', 255)
                    if event.value == 0:
                        stop_driver(board, 'right_driver')
                    print('X')
                elif event.code == 308:
                    print('L1')
                elif event.code == 309:
                    print('R1')
                elif event.code == 310:
                    print('L2')
                elif event.code == 311:
                    print('R2')
                elif event.code == 312:
                    print('Back')
                elif event.code == 313:
                    stop_all_drivers(board)
                    board.shutdown()
                    sys.exit()
                    print('Start')
                elif event.code == 314:
                    
                    print('Left Sosok')
                elif event.code == 315:
                    print('Right Sosok')
            if event.value == 1 and i == True :
                if keyevent.scancode == 306:
                    print('altB')
                elif keyevent.scancode == 307:
                    print('altY')
                    i= False
                elif keyevent.scancode == 305:
                    print('altA')
                elif keyevent.scancode == 304:
                    print('altX')
                elif event.code == 308:
                    print('altL1')
                elif event.code == 309:
                    print('altR1')
                elif event.code == 310:
                    print('altL2')
                elif event.code == 311:
                    print('altR2')
                elif event.code == 312:
                    print('altBack')
                elif event.code == 313:
                    print('altStart')
                elif event.code == 314:
                    print('altLeft Sosok')
                elif event.code == 315:
                    print('altRight Sosok')
        if event.type == ecodes.EV_ABS and i == False:
            absevent = categorize(event)
            if event.code == 17:
               if event.value==-1:
                    print('DPup')
               elif event.value==1:
                    print('DPdown')
            elif event.code == 16:
               if event.value==1:
                    print('DPright')
               elif event.value==-1:
                    print('DPleft')
            elif event.code == 1:
               if event.value>254:
                    print('LSdown')
               elif event.value<1:
                    print('LSup')
            elif event.code == 0:
               if event.value>254:
                    print('LSright')
               elif event.value<1:
                    print('LSleft')
            elif event.code == 5:
               if event.value>254:
                    print('RSdown')
               elif event.value<1:
                    print('RSup')
            elif event.code == 2:
               if event.value>254:
                    print('RSright')
               elif event.value<1:
                    print('RSleft')
        if event.type == ecodes.EV_ABS and i == True:
            absevent = categorize(event)
            if event.code == 17:
               if event.value==-1:
                    print('altDPup')
               elif event.value==1:
                    print('altDPdown')
            elif event.code == 16:
               if event.value==1:
                    print('altDPright')
               elif event.value==-1:
                    print('altDPleft')
            elif event.code == 1:
               if event.value>254:
                    print('altLSdown')
               elif event.value<1:
                    print('altLSup')
            elif event.code == 0:
               if event.value>254:
                    print('altLSright')
               elif event.value<1:
                    print('altLSleft')
            elif event.code == 5:
               if event.value>254:
                    print('altRSdown')
               elif event.value<1:
                    print('altRSup')
            elif event.code == 2:
               if event.value>254:
                    print('altRSright')
               elif event.value<1:
                    print('altRSleft')
