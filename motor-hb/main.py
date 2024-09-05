from machine import Pin
from utime import sleep
from homebrew import Stepper

pins_leds = [Pin(15, Pin.OUT, 0),
            Pin(14, Pin.OUT, 0),
            Pin(13, Pin.OUT, 0),
            Pin(12, Pin.OUT, 0)]

pins_motor = [Pin(0, Pin.OUT, 0),
            Pin(1, Pin.OUT, 0),
            Pin(2, Pin.OUT, 0),
            Pin(3, Pin.OUT, 0)]

btn_left = Pin(16, Pin.IN, Pin.PULL_DOWN)
btn_right = Pin(17, Pin.IN, Pin.PULL_DOWN)
btn_reset = Pin(18, Pin.IN, Pin.PULL_DOWN)

#ledzz = Stepper(pins_leds)
motor = Stepper(pins_motor, pins_leds)

global step_count
step_count= 0

#motor.rotate_full()

# check out left and right, it is weird for some reason

def handler_btn_left(pin):
    global step_count
    while btn_left.value() == 1:
        pins_leds[1].value(1)
        motor.move()
        #motor.ledflasher()
        step_count += 1
        if step_count == 512: step_count = 0

def handler_btn_right(pin):
    global step_count
    while btn_right.value() == 1:
        motor.move(-1)
        #motor.ledflasher(-1)
        step_count -= 1
        if step_count == -512: step_count = 0

def handler_btn_reset(pin):
    global step_count
    global step_count
    if step_count > 0:
        while step_count > 0:
            motor.move(-1)
            step_count -= 1
    elif step_count < 0:
        while step_count < 0:
            motor.move(1)
            step_count += 1

btn_left.irq(trigger=Pin.IRQ_RISING, handler=handler_btn_left)
btn_right.irq(trigger=Pin.IRQ_RISING, handler=handler_btn_right)
btn_reset.irq(trigger=Pin.IRQ_RISING, handler=handler_btn_reset)

while True:
    sleep(0.001)