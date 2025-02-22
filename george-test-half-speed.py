from __future__ import print_function
import time
from typing import Mapping
from dual_max14870_rpi import motors, MAX_SPEED
import RPi.GPIO as GPIO 

try: 
    motors.setSpeeds(0, 0)
    
    s = float(input('Enter speed between 0 & 480: '))
    t = float(input('Enter the time to run the motors in seconds: '))
    
    motors.motor1.setSpeed(s)
    print("Motor 1 Forward at", s," seconds")
    time.sleep(t)
    
    motors.motor1.setSpeed(0)
    time.sleep(2)

    motors.motor1.setSpeed(-s)
    print("Motor 1 Reverse at", s," seconds")
    time.sleep(t)

    print("Motor 1 off")
    motors.motor1.setSpeed(0)

    motors.motor2.setSpeed(s)
    print("Motor 2 Forward at", s," seconds")
    time.sleep(t)
    
    motors.motor2.setSpeed(0)
    time.sleep(2)

    motors.motor2.setSpeed(-s)
    print("Motor 2 Reverse at", s," seconds")
    time.sleep(t)

    print("Motor 2 off")
    motors.motor2.setSpeed(0)
    time.sleep(1)

    motors.disable()

finally:
    motors.forceStop()
    gpio.cleanup()
    