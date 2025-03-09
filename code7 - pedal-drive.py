# Bicycle activity

# Imports
from bicycle_lib import *

min_pot = 1450
mid_pot = 4000
max_pot = 6553

while True:
    if checkBike():
        # Get pot and candence values
        value = getPot()
        cadence = getCadence()

        # Convert cadence value to speed and pot value to braking
        speed = map(cadence, 0, 100, 0, 100)
        braking = map(value, mid_pot, min_pot, 0, 100)
        print(speed, braking)
        
        # Apply speed or braking
        if braking>0:
            brake(braking)
        elif speed>=0:
            accelerate(speed)

        actualSpeed = getActualSpeed()
        displayValue(actualSpeed)