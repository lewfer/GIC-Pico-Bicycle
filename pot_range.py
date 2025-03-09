# Determine pot range

import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
import time
import busio as io
import adafruit_ht16k33.segments

#  Set up the potentiometer on pin 28 as an analogue input pin
pot = AnalogIn(board.GP28_A2)

# Create display object
i2c = io.I2C(board.GP3, board.GP2) # SCL, SDA
display = adafruit_ht16k33.segments.Seg7x4(i2c, address=0x70)

# Value will be 0 to 65535 (direction of increase/decrease depending on the order of black/red wires)
maxPot = 0
minPot = 6553
mid = 0
while True:
    try:
        val = int(pot.value/10)
        if val>maxPot: maxPot = val
        if val<minPot: minPot = val
        print(val, minPot, maxPot)
        display.print(val)
        display.show()
        time.sleep(.2)
    except KeyboardInterrupt:
        break
    
print("ended")
