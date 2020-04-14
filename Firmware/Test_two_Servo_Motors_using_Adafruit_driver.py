# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Kareem Elzeftawy

#set_pwm(channel, on, off)
#channel: The channel that should be updated with the new values (0..15)
#on: The tick (between 0..4095) when the signal should transition from low to high
#off:the tick (between 0..4095) when the signal should transition from high to low

#set_pwm_freq(freq)
#freq: A number representing the frequency in Hz, between 40 and 1000

from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

def Motor1():
    # Move servo on channel O between extremes.
    
    for pulselen in range (servo_min, servo_max, +1):
        pwm.set_pwm(0, 0, pulselen)

    time.sleep(500)
      
    for pulselen in range (servo_max, servo_min, -1):
        pwm.set_pwm(0, 0, pulselen)

    time.sleep(500)

def Motor2():
    # Move servo on channel 15 between extremes.
    
    for pulselen in range (servo_min, servo_max, +1):
        pwm.set_pwm(15, 0, pulselen)

    time.sleep(500)
      
    for pulselen in range (servo_max, servo_min, -1):
        pwm.set_pwm(15, 0, pulselen)

    time.sleep(500)

while True:
    print('Moving servo1 on channel 0, press Ctrl-C to quit...')
    Motor1()
    print('Moving servo2 on channel 0, press Ctrl-C to quit...')
    Motor2()
