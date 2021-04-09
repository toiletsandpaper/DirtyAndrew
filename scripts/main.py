from datetime import datetime, timedelta
from pymata4 import pymata4
import sys
import keyboard
from evdev import InputDevice, categorize, ecodes, KeyEvent


gamepad = InputDevice('/dev/input/event0')
HALL_PINS = [22, 24, 26, 28]
DRIVER_1_PINS = [7, 8]   # left
DRIVER_2_PINS = [9, 10]   # right
DRIVER_3_PINS = [5, 6] # elevator


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
        print('elevator driver moved')

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

def servo_stop(my_board, pin):
    my_board.set_pin_mode_servo(pin)
    my_board.servo_write(pin, 90)



# def setup_all_hall(board)

def is_hall_active(my_board, hall_index):
    my_board.set_pin_mode_digital_input(HALL_PINS[hall_index])
    print(my_board.digital_read(HALL_PINS[hall_index]))
    value, time_stamp = my_board.digital_read(HALL_PINS[hall_index])
    # print(not value)
    return not value


if __name__ == "__main__":
    board = pymata4.Pymata4()
    setup_all_drivers(board)
    speed = 255
    altY = False
    # timer = datetime.now()
    # deltatime = 0

    for event in gamepad.read_loop():
        if event.type == ecodes.EV_KEY:
            keyevent = categorize(event)
            # deltatime = (deltatime + (datetime.now() - timer).total_seconds())
            # timer = datetime.now()
            
            #alternate move
            if keyevent.scancode == 307:
                altY = True if event.value == 1 else False
            #right
            if keyevent.scancode == 309: # right
                if event.value == 1:
                    move_driver(board, 'right_driver' , 'right' if not altY else 'left', speed)
                if event.value == 0:
                   stop_driver(board, 'right_driver')
            #left
            if keyevent.scancode == 308: # left
                if event.value == 1:
                    move_driver(board, 'left_driver', 'left' if not altY else 'right', speed)
                if event.value == 0:
                   stop_driver(board, 'left_driver')
            #stop system
            if keyevent.scancode == 313:
                stop_all_drivers(board)
                board.shutdown()
                sys.exit()
            if keyevent.scancode == 304:
                if event.value == 1:
                    servo_right(board, 4)
                if event.value == 0:
                    servo_stop(board, 4)
            if keyevent.scancode == 305:
                stop_all_drivers(board)
        if event.type == ecodes.EV_ABS:
            absevent = categorize(event)
            if event.code ==17:
                if event.value == -1:
                    move_driver(board, 'elevator_driver', 'right', 255)
                if event.value == 1:
                    move_driver(board, 'elevator_driver', 'left', 255)
                if event.value == 0:
                    stop_driver(board, 'elevator_driver')
            if event.code ==16:
                if event.value == 1:
                    servo_right(board, 44)
                if event.value == -1:
                    servo_left(board, 44)
                if event.value == 0:
                    servo_stop(board, 44)       
                

        # if deltatime > .5:
        #    deltatime = 0
        #   if is_hall_active(board, hall_index = 0):
        #      stop_driver(board)
