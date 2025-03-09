# Bicycle activity

# Imports
from bicycle_lib import *

min_pot = 1450
mid_pot = 4000
max_pot = 6553

while True:
    # Get pot value
    value = getPot()
    
    # Convert pot value to a speed
    speed = map(value, min_pot, max_pot, 0, 100)
    accelerate(speed)
    
    displayValue(speed)
    sleep(0.2)
