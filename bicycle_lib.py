# Bicycle library

# Imports
import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
from time import sleep, monotonic_ns
import busio as io
import PicoRobotics
import adafruit_ht16k33.segments

#  Set up the potentiometer on pin 28 as an analogue input pin
pot = AnalogIn(board.GP28_A2)

# Create object for 7 segment display
i2c = io.I2C(board.GP27, board.GP26) # SCL, SDA
display = adafruit_ht16k33.segments.Seg7x4(i2c, address=0x70)

# Create robotics object for motor control
robot = PicoRobotics.KitronikPicoRobotics()

# Set up the hall sensor as a button on pin 22 (digital input)
hall = DigitalInOut(board.GP22)
hall.direction = Direction.INPUT
hall.pull = Pull.UP               # Pull up so button value is True when not pressed

display_time_stamp = monotonic_ns()

def displayValue(value):
    global display_time_stamp
    
    new_display_time_stamp = monotonic_ns()
    seconds = (new_display_time_stamp-display_time_stamp)/1000000000
    
    if seconds>0.25:    
        display.print('{:4d}'.format(int(value)))
        display.show()
        display_time_stamp = new_display_time_stamp

# Track the current motor speed (0-100)
currentSpeed = 0
actualSpeed = 0

# Limit the speed
topSpeed = 100
minSpeed = 0
increment = 1
motor = 1


# Drive the wheel at the specified speed, which is in range 0 to 100
def drive(speed):
    global currentSpeed
    global actualSpeed
    
    # Move speed towards the requested speed (up or down)
    currentSpeed = speed
        
    # Don't go above top speed
    if currentSpeed>topSpeed:
        currentSpeed = topSpeed
    actualSpeed = currentSpeed

    # Turn motor
    robot.motorOn(motor, "f", actualSpeed)
    
    # Show speed
    #displayValue(actualSpeed)
    
# Accelerate the wheel towards the specified speed, which is in range 0 to 100
def accelerate(speed):
    global currentSpeed
    global actualSpeed
    
    # Move speed towards the requested speed (up or down)
    if speed>currentSpeed:
        currentSpeed += 1
    elif speed<currentSpeed:
        currentSpeed -= 1
        
    # Don't go above top speed
    if currentSpeed>topSpeed:
        currentSpeed = topSpeed
    actualSpeed = currentSpeed
    
    #print("-----------------Actual", actualSpeed)

    # Turn motor
    robot.motorOn(motor, "f", actualSpeed)
    


# Apply braking to slow wheel, amount is 0 to -100
def brake(amount):
    global currentSpeed
    global actualSpeed
    global prev_seconds_since_last
    global _cadence
    
    # Slow down relative to the amount specified
    currentSpeed -= amount/10
    _cadence = 0
    prev_seconds_since_last = 5
    print("Brake", amount)
#     if amount<-topSpeed:
#         currentSpeed -= 5
#         print("------------------brake5")
#     elif amount<-5:
#         currentSpeed -= 1        
#         print("------------------brake1")
    
    # Don't go below 0
    if currentSpeed<0:
        currentSpeed = 0
    actualSpeed = currentSpeed

    # Turn motor
    robot.motorOn(motor, "f", actualSpeed)
    


time_stamp = monotonic_ns()
toggle = True
seconds_since_last = 0
prev_seconds_since_last = 5
_cadence = 0

    

count = 5
 
        
def checkBike():
    global toggle
    global seconds_since_last
    global prev_seconds_since_last
    global time_stamp
    global _cadence
    global count
    
    # Get time
    new_time_stamp = monotonic_ns()

    # Compute time in seconds since last trigger
    seconds_since_last = (new_time_stamp-time_stamp)/1000000000
            
    # Check hall sensor
    if hall.value == False:
        print(".", end="")
        # Hall sensor was triggered
        if toggle: # toggle so only sensed once per turn
            toggle = False
            
            # Compute cadence
            _cadence = 60 / seconds_since_last
            
            # Remember time stamp
            time_stamp = new_time_stamp
            prev_seconds_since_last = seconds_since_last
    else:
        # Hall sensor was not triggered, so reset toggle
        toggle = True
        if seconds_since_last > 5:
            _cadence = 0
            prev_seconds_since_last = 5
        elif seconds_since_last>prev_seconds_since_last:
            _cadence = 60 / seconds_since_last
            
    #print("C", _cadence)
    sleep(0.01)
        
    # Return true every 5 runs.  This allows cadence checks frequently but other things less frequently
    count -= 1
    if count==0:
        count = 5    
        return True
    else:
        return False
        #print("TOGGLEOFF")

def getCadence():
    global _cadence
    print("Cadence", _cadence)
    
    return _cadence


# Map a value from one range to another
def map(value, minFrom, maxFrom, minTo, maxTo):
    mapped = minTo + (maxTo - minTo) * ((value - minFrom) / (maxFrom - minFrom))
    if mapped < minTo:
        mapped = minTo
    elif mapped > maxTo:
        mapped = maxTo
    return mapped


maxPot = 6000
midPot = 4000
minPot = 2000

def getPot():
    # pot.value will be 0 to 65535 (direction of increase/decrease depending on the order of black/red wires)
    val = int(pot.value/10)
    return val

def getThrottle():
    # pot.value will be 0 to 65535 (direction of increase/decrease depending on the order of black/red wires)
    val = int(pot.value/10)
    throttle = map(val, minPot, maxPot, -100, 100)
    return throttle

def getActualSpeed():
    return actualSpeed

    