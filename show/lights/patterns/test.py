from .pattern import Pattern
import time
import math
from .putil import *

NUM_PIXELS = 300
NUM_LEDS = 300

class Test(Pattern):

    @classmethod
    def get_id(self):
        return 0

    @classmethod
    def update(self, strip, state):
        color = get_random_color()
        color1 = get_random_color()
        color2 = get_random_color()
        red = get_random_color()
        green = get_random_color()
        blue = get_random_color()
        iterations=100
        size = 5
        delay=0.1
        gravity=0.8
        EyeSize = 4
        center = random.randint(0, NUM_PIXELS - 1)
        snow = [0] * NUM_PIXELS
        for i in range(NUM_LEDS - EyeSize - 2):
            strip.setAll(Color(0, 0, 0))  # Turn off all LEDs

            # Set the leading dim pixel
            strip.setPixelColor(i, Color(red // 10, green // 10, blue // 10))

            # Set the "eye" of the effect
            for j in range(1, EyeSize + 1):
                strip.setPixel(i + j, Color(red, green, blue))

            # Set the trailing dim pixel
            strip.setPixelColor(i + EyeSize + 1, Color(red // 10, green // 10, blue // 10))

            strip.show()  # Update the LED strip
            time.sleep(delay)