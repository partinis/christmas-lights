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
        color = get_random_color()
        for i in range(NUM_PIXELS):
            if i % 2 == 0:
                strip.setPixelColor(i, (0, 0, 255))  # Blue
            else:
                strip.setPixelColor(i, (255, 255, 255))  # White
        strip.show()
        time.sleep(.1)
        for i in range(NUM_PIXELS):
            strip.setPixelColor(i, (0, 0, 0))  # Turn off for dripping effect
            strip.show()
            time.sleep(.1 / 2)