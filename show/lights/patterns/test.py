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
        for _ in range(10):
            led = random.randint(0, NUM_PIXELS - 1)
            color = (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))  # Random soft colors
            strip.setPixelColor(led, color)
            strip.show()
            time.sleep(.05)
            strip.setPixelColor(led, (0, 0, 0))  # Turn it off