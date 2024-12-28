from .pattern import Pattern
import time
import math
from .putil import *

NUM_PIXELS = 300

class Test(Pattern):

    @classmethod
    def get_id(self):
        return 0

    @classmethod
    def update(self, strip, state):
        color1 = get_random_color()
        color2 = get_random_color()
        iterations=100
        delay=0.1
        for i in range(strip.numPixels() + size):
            for j in range(strip.numPixels()):
                strip.setPixelColor(j, (0, 0, 0))  # Clear all
            for j in range(size):
                if 0 <= i - j < strip.numPixels():
                    strip.setPixelColor(i - j, color)
            strip.show()
            time.sleep(delay)