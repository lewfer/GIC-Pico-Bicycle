# Bicycle activity

# Imports
from bicycle_lib import *

min_pot = 1450
mid_pot = 4000
max_pot = 6553

while True:
    if checkBike():
        cadence = getCadence()
        
        displayValue(cadence)