from machine import Pin
from utime import sleep_ms

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
    __full_rotation_steps = 512
    #__step_count = 0

    def __init__(self, IN1, IN2, IN3, IN4):
        pins_stepper = [IN1, IN2, IN3, IN4]
        self.pins_stepper = [Pin(p, Pin.OUT, 0) for p in pins_stepper]
        self.set_startpos()

    def __reset(self):
        for p in self.pins_stepper:
            p.value(0)

    def set_startpos(self):
        self.__step_count = 0

    def goto_startpos(self):
        print(self.__step_count)
        #if self.__step_count > 0:
        while self.__step_count > 0:
            self.move_counter_clockwise()
        #elif self.__step_count < 0:
        while self.__step_count < 0:
            self.move_clockwise()

    def move_clockwise(self):
        for state in self.__states:
            for p in range(4):
                self.pins_stepper[p].value(state[p])
            sleep_ms(1)
        self.__step_count += 1
        if self.__step_count == self.__full_rotation_steps: self.__step_count = 0
        self.__reset()

    def move_counter_clockwise(self):
        for state in reversed(self.__states):
            for p in range(4):
                self.pins_stepper[p].value(state[p])
            sleep_ms(1)
        self.__step_count -=1
        if self.__step_count == -self.__full_rotation_steps: self.__step_count = 0
        #print(self.__step_count)
        self.__reset()

    def rotate_full_cw(self):
        for i in range(self.__full_rotation_steps):
            self.move_clockwise()
    
    def rotate_full_ccw(self):
        for i in range(self.__full_rotation_steps):
            self.move_counter_clockwise()
        #print(self.__step_count)
