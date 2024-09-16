from machine import Pin
from utime import sleep
from homebrew import Stepper

btn_left = Pin(17, Pin.IN, Pin.PULL_DOWN)
btn_right = Pin(16, Pin.IN, Pin.PULL_DOWN)
btn_reset = Pin(18, Pin.IN, Pin.PULL_DOWN)
btn_setpos = Pin(19, Pin.IN, Pin.PULL_DOWN)

led_red = Pin(15, Pin.OUT, 0)
led_green = Pin(14, Pin.OUT, 0)
led_yellow = Pin(13, Pin.OUT, 0)
led_blue = Pin(12, Pin.OUT, 0)

motor = Stepper(0,1,2,3)

#motor.rotate_full_ccw()

global step_count
step_count= 0

def handler_btn_left(pin):
    global step_count
    while btn_left.value() == 1:
        motor.move_counter_clockwise()
        led_red.value(1)
        step_count -= 1
        if step_count == -512: step_count = 0
    led_red.value(0)

def handler_btn_right(pin):
    global step_count
    while btn_right.value() == 1:
        led_blue.value(1)
        motor.move_clockwise()
        step_count += 1
        if step_count == 512: step_count = 0
    led_blue.value(0)

def handler_btn_reset(pin):
    # global step_count
    # global step_count
    # if step_count > 0:
    #     while step_count > 0:
    #         #motor.move(-1)
    #         step_count -= 1
    #         led_green.value(1) 
    # elif step_count < 0:
    #     while step_count < 0:
    #         #motor.move(1)
    #         step_count += 1
    #         led_yellow.value(1)
    # led_green.value(0)
    # led_yellow.value(0)
    motor.goto_startpos()

def handler_btn_setpos(pin):
    motor.set_startpos()


btn_left.irq(trigger=Pin.IRQ_RISING, handler=handler_btn_left)
btn_right.irq(trigger=Pin.IRQ_RISING, handler=handler_btn_right)
btn_reset.irq(trigger=Pin.IRQ_RISING, handler=handler_btn_reset)
btn_setpos.irq(trigger=Pin.IRQ_RISING, handler=handler_btn_setpos)

while True:
    sleep(0.001)