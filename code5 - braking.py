# Bicycle activity

# Imports
from bicycle_lib import *

min_pot = 1450
mid_pot = 4000
max_pot = 6553

while True:
    # Get pot value
    value = getPot()
    
    # Convert pot value to a speed or braking
    speed = map(value, mid_pot, max_pot, 0, 100)
    braking = map(value, mid_pot, min_pot, 0, 100)
    print(speed, braking)
    
    # Apply speed or braking
    if braking>0:
        brake(braking)
    elif speed>=0:
        accelerate(speed)
        
    displayValue(speed)
    sleep(0.2)

        