# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Kareem Elzeftawy

#set_pwm(channel, on, off)
#channel: The channel that should be updated with the new values (0..15)
#on: The tick (between 0..4095) when the signal should transition from low to high
#off:the tick (between 0..4095) when the signal should transition from high to low

#set_pqm_freq(freq)
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

def clockwise(channel):
    # ON for 1.3ms & OFF for 20ms
    pwm.set_pwm(channel, 250, 3846)

def counterclockwise(channel):
    # ON for 1.7ms & OFF for 20ms
    pwm.set_pwm(channel, 321, 3775)

def stay_still(channel):
    # ON for 1.5ms & OFF for 20ms
    pwm.set_pwm(channel, 286, 3810)

def stop(channel):
    pwm.set_pwm(channel, 0, 0)

def forward(channel1, channel2):
    #motor1 rotate clockwise and motor2 stop
    clockwise(channel1)
    stop(channel2)

def backward(channel1, channel2):
    #motor1 stop and motor2 rotate clockwise
    stop(channel1)
    clockwise(channel2)

while True:
    forward(0, 15)
    
    
    
    
    

