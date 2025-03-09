# Test motor with kitronik robotics board

import PicoRobotics
import time

# Create robotics object
robot = PicoRobotics.KitronikPicoRobotics()

top_speed = 100
min_speed = 0
increment = 2
wait = 0.2
motor = 1

print("Forward")
for speed in range(min_speed,top_speed,increment):
    print(speed)
    robot.motorOn(motor, "f", speed)
    time.sleep(wait)
for speed in range(top_speed,min_speed,-increment):
    print(speed)
    robot.motorOn(motor, "f", speed)
    time.sleep(wait)
# 
# time.sleep(3)
# robot.motorOff(4)
# 
# print("Reverse")
# for speed in range(min_speed,top_speed,increment):
#     print(speed)
#     robot.motorOn(4, "r", speed)
#     time.sleep(wait)
# for speed in range(top_speed,min_speed,-increment):
#     print(speed)
#     robot.motorOn(4, "r", speed)
#     time.sleep(wait)
time.sleep(3)
#robot.motorOn(4, "f", 10)
time.sleep(3)
print("Stop")
robot.motorOff(4)