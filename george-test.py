from __future__ import print_function
import time
from typing import Mapping
from dual_max14870_rpi import motors, MAX_SPEED

""" # Define a custom exception to raise if a fault is detected.
class DriverFault(Exception):
    pass """

""" def raiseIfFault():
    if motors.getFault():
        raise DriverFault """
    
motors.motor1.setSpeed(MAX_SPEED)
print("Motor 1 Forward Max Speed")
fault = motors.getFault()
print(fault)
time.sleep(5)

motors.motor1.setSpeed(MAX_SPEED) * -1
print("Motor 1 Reverse Max Speed")
fault = motors.getFault()
print(fault)
time.sleep(5)

print("Motor 1 off")
motors.motor1.setSpeed(0)

motors.motor2.setSpeed(MAX_SPEED)
print("Motor 2 Forward Max Speed")
fault = motors.getFault()
print(fault)
time.sleep(5)

motors.motor2.setSpeed(MAX_SPEED) * -1
print("Motor 2 Reverse Max Speed")
fault = motors.getFault()
print(fault)
time.sleep(5)

print("Motor 2 off")
motors.motor2.setSpeed(0)
time.sleep(1)

motors.disable()


""" # Set up sequences of motor speeds.
test_forward_speeds = list(range(0, MAX_SPEED, 1)) + \
  [MAX_SPEED] * 200 + list(range(MAX_SPEED, 0, -1)) + [0]

test_reverse_speeds = list(range(0, -MAX_SPEED, -1)) + \
  [-MAX_SPEED] * 200 + list(range(-MAX_SPEED, 0, 1)) + [0]

try:
    motors.setSpeeds(0, 0)

    print("Motor 1 forward")
    for s in test_forward_speeds:
        motors.motor1.setSpeed(s)
        raiseIfFault()
        time.sleep(0.002)

    print("Motor 1 reverse")
    for s in test_reverse_speeds:
        motors.motor1.setSpeed(s)
        raiseIfFault()
        time.sleep(0.002)

    # Disable the drivers for half a second.
    motors.disable()
    time.sleep(0.5)
    motors.enable()

    print("Motor 2 forward")
    for s in test_forward_speeds:
        motors.motor2.setSpeed(s)
        raiseIfFault()
        time.sleep(0.002)

    print("Motor 2 reverse")
    for s in test_reverse_speeds:
        motors.motor2.setSpeed(s)
        raiseIfFault()
        time.sleep(0.002)

except DriverFault:
    print("Driver fault!")

finally:
    # Stop the motors, even if there is an exception
    # or the user presses Ctrl+C to kill the process.
    motors.forceStop()
 """