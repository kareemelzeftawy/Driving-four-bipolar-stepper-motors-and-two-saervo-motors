#!/usr/bin/python
# -*- coding: utf-8 -*-

import easydriver as ed

# Direction of rotation is dependent on how the motor is connected.
# If the motor runs the wrong way swap the values of cw and ccw.
cw = True
ccw = False

"""
Arguments to pass or set up after creating the instance.

Step GPIO pin number.
Delay between step pulses in seconds.
Direction GPIO pin number.
Microstep 1 GPIO pin number.
Microstep 2 GPIO pin number.
Enable GPIO pin number.
Sleep GPIO pin number.
Reset GPIO pin number.
Name as a string.

"""

# Create an instance of the easydriver class.
# Not using sleep, enable or reset.
stepper1 = ed.easydriver(18, 0.004, 23, 24, 25, 12)
stepper2 = ed.easydriver(16, 0.004, 20, 21, 26, 19)
stepper3 = ed.easydriver(13, 0.004, 6, 5, 22, 27)
stepper4 = ed.easydriver(17, 0.004, 4, 3, 2, 14)

def Motor1(direction, steps):
    # Enable motor
    stepper1.enable()
    
    # Set motor direction to clockwise.
    stepper1.set_direction(direction)

    # Set the motor to run in 1/4 of a step per pulse.
    stepper1.set_quarter_step()
       
    # Do some steps.
    for i in range(0, steps):
        stepper1.step()

    # Disable motor
    stepper1.disable()

def Motor2(direction, steps):
    # Enable motor
    stepper2.enable()
    
    # Set motor direction to clockwise.
    stepper2.set_direction(direction)

    # Set the motor to run in 1/4 of a step per pulse.
    stepper2.set_quarter_step()

    # Do some steps.
    for i in range(0, steps):
        stepper2.step()

    # Disable motor
    stepper2.disable()

def Motor3(direction, steps):
    # Enable motor
    stepper3.enable()
    
    # Set motor direction to clockwise.
    stepper3.set_direction(direction)

    # Set the motor to run in 1/4 of a step per pulse.
    stepper3.set_quarter_step()

    # Do some steps.
    for i in range(0, steps):
        stepper3.step()

    # Disable motor
    stepper3.disable()

def Motor4(direction, steps):
    # Enable motor
    stepper3.enable()
    
    # Set motor direction to clockwise.
    stepper3.set_direction(direction)

    # Set the motor to run in 1/4 of a step per pulse.
    stepper3.set_quarter_step()

    # Do some steps.
    for i in range(0, steps):
        stepper3.step()

    # Disable motor
    stepper3.disable()
    
#Main Fn
print("Motor1 run 500 steps clockwise (1/4 of a step per pulse)")
Motor1(cw, 500)
print("Motor2 run 300 steps anti-clockwise (1/4 of a step per pulse)")
Motor2(ccw, 300)
print("Motor3 run 500 step anti-clockwise (1/4 of a step per pulse)")
Motor3(ccw, 500)
print("Motor4 run 300 step clockwise (1/4 of a step per pulse)")
Motor4(cw, 300)

# Clean up (just calls GPIO.cleanup() function.)
stepper1.finish()
stepper2.finish()
stepper3.finish()
stepper4.finish()
