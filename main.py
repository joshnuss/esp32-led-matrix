from machine import Pin
from neopixel import NeoPixel

# connect to pin #1
pin = Pin(1)

# matrix has 64 pixels
led_matrix = NeoPixel(pin, n=64)

# tuple is (r, g, b)
# index is pixel number (ie pixel 32)
led_matrix[32] = (0xFF, 0, 0)

# update led matrix
led_matrix.write()
