# Test Potentiometer

import time
import board
import analogio

#  Set up the potentiometer on pin 28 as an analogue input pin
pot = analogio.AnalogIn(board.GP28_A2)

# Value will be 0 to 65535 (direction of increase/decrease depending on the order of black/red wires)
while True:
    val = pot.value
    print(val)
    time.sleep(0.5)