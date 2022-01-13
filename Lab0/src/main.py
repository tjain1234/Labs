"""!
@file main.py
This file contains code that lights up the LED at pinA0 on the
NUCLEO-L476RG. The pattern executed is a sawtooth wave, where
LED’s brightness slowly increase from 0 to maximum over 5
seconds, then go back to 0 and repeat the process indefinitely.

@author Jonathan Cederquist, Tim Jain, Philip Pang
@date   01-Jan-2022
"""

import pyb
import utime

def led_setup ():
    """!
    Sets up pin, timer, and channel objects to control LED
    """
    pinA0 = pyb.Pin (pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    tim2 = pyb.Timer (2, freq=20000)
    # channel object needs to be global in order to be accessed...
    # ...by led_brightness() function later
    global ch1
    ch1 = tim2.channel (1, pyb.Timer.PWM_INVERTED, pin=pinA0)

def led_brightness (brightness):
    """!
    Sets LED brightness on channel defined in led_setup()
    @param brightness A percentage for the PWM control
    """
    ch1.pulse_width_percent (brightness)

# Test Code
if __name__ == "__main__":
    # Sets period for sawtooth wave as 5 seconds
    led_setup()
    start = utime.ticks_ms()
    period = 5000
    while True:
        # elapsed time is computed as a multiple of the period
        elapsed = utime.ticks_diff(utime.ticks_ms(), start)/period
        # brightness is calculated as a percentage of the...
        # ...period using elapsed time
        bright = 100 * (elapsed % 1)
        led_brightness(bright)
    
