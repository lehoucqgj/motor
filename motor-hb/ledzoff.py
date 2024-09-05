import machine
from homebrew import Stepper

pins_step_leds = [machine.Pin(15, machine.Pin.OUT, 0),
                 machine.Pin(14, machine.Pin.OUT, 0),
                 machine.Pin(13, machine.Pin.OUT, 0),
                 machine.Pin(12, machine.Pin.OUT, 0)]

for led in pins_step_leds:
    led.value(0)

pins_motor = [machine.Pin(0, machine.Pin.OUT, 0),
            machine.Pin(1, machine.Pin.OUT, 0),
            machine.Pin(2, machine.Pin.OUT, 0),
            machine.Pin(3, machine.Pin.OUT, 0)]

for pin in pins_motor:
    pin.value(0)