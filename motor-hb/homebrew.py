from machine import Pin
import utime

class Stepper:
    __states = [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 1],
    ]
    __steps_full_rotation = 4096

    def __init__(self, pinz_motor, pins_led):
        self.pinz_mtr = pinz_motor
        self.pins_led = pins_led

    def __reset(self):
        for p in self.pinz_mtr:
            p.value(0)
        for l in self.pins_led:
            l.value(0)
        
    def move(self, direction: int=1):
        _ordered_states = self.__states if direction == 1 else reversed(self.__states)
        for state in _ordered_states:
            utime.sleep_ms(1)
            for pin, value in zip(self.pinz_mtr, state):
                pin.value(value)
        self.__reset()

    def rotate_full(self):
        for i in range(512):
            self.move()

    def ledflasher(self, direction: int=1):
        _ordered_states = self.__states if direction == 1 else reversed(self.__states)
        for state in _ordered_states:
            for p in range(4):
                self.pins_led[p].value(state[p])
            utime.sleep_ms(250)
        self.__reset()
