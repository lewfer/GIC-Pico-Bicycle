# Test button input (button connected to ground)

import board
from digitalio import DigitalInOut, Direction, Pull
import time

# Set up the hall sensor as a button on pin 22 (digital input)
switch = DigitalInOut(board.GP22)
switch.direction = Direction.INPUT
switch.pull = Pull.UP               # Pull up so button value is True when not pressed

# Show the button status (False is pressed, True is not pressed)
count = 0
while True:
    if switch.value == False:
        count += 1
        print(switch.value, count)
    time.sleep(0.1)