"""
Util functions

"""
import random
import colorsys

LED_COUNT = 300

def Color(red, green, blue, white = 0):
    """Convert the provided red, green, blue color to a 24-bit color value.
    Each color component should be a value 0-255 where 0 is the lowest intensity
    and 255 is the highest intensity.
    """
    return (white << 24) | (red << 16)| (green << 8) | blue

def SetAll(strip, color):
    strip.fill(color)

def get_random_color():
    """
    Gets a random color as a tuple
    """
    hsv = colorsys.hsv_to_rgb(random.random(), 1, 1)
    return int(hsv[0]*255), int(hsv[1]*255), int(hsv[2]*255)

def get_random_pixel():
    """Returns pseudo random pixel between 0..NUM_PIXELS"""
    return random.randrange(0, LED_COUNT)