# Test 7 segment led display
import board
import busio as io
import time
import adafruit_ht16k33.segments

# Create display object
i2c = io.I2C(board.GP27, board.GP26) # SCL, SDA
display = adafruit_ht16k33.segments.Seg7x4(i2c, address=0x70)

## Clear
display.fill(0)

# Display individual characters
display[0] = '8'
display[1] = '7'
display[2] = 'a'
display[3] = 'm' # some chars can't display
display.show()
time.sleep(2)

# Display number
display.print(1234)
display.show()
time.sleep(2)

# Display letters
display.print('DEAL')
display.show()
time.sleep(2)