from datetime import datetime, timedelta
from pymata4 import pymata4
import sys
import keyboard

HALL_PINS = [22, 24, 26, 28]
DRIVER_PINS = [6, 7]


def setup_all_drivers(my_board):
    my_board.set_pin_mode_pwm_output(DRIVER_PINS[0])
    my_board.set_pin_mode_pwm_output(DRIVER_PINS[1])


def move_driver(my_board, direction, speed):  # TODO: add speed and direction
    value_right = 0
    value_left = 0
    if direction == 'left':
        value_left = 1
    elif direction == 'right':
        value_right = 1
    my_board.pwm_write(DRIVER_PINS[0], value_left * speed)
    my_board.pwm_write(DRIVER_PINS[1], value_right * speed)


def stop_driver(my_board):
    my_board.pwm_write(DRIVER_PINS[0], 0)
    my_board.pwm_write(DRIVER_PINS[1], 0)


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
    # timer = datetime.now()
    # deltatime = 0

    while True:
        # deltatime = (deltatime + (datetime.now() - timer).total_seconds())
        # timer = datetime.now()

        if keyboard.is_pressed('d'):
            move_driver(board, 'right', 255)
        if keyboard.is_pressed('a'):
            move_driver(board, 'left', 50)
        if keyboard.is_pressed('s'):
            stop_driver(board)
            board.shutdown()
            sys.exit()
        if keyboard.is_pressed('spacebar'):
            stop_driver(board)

    # if deltatime > .5:
    #    deltatime = 0
    #   if is_hall_active(board, hall_index = 0):
    #      stop_driver(board)
