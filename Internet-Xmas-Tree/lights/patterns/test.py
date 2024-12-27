from .pattern import Pattern
import time
import math
from .putil import *

NUM_PIXELS = 300
fade_value = 10

class Test(Pattern):

    @classmethod
    def get_id(self):
        return 0

    @classmethod
    def update(self, strip, state):
        color = (255, 0, 0)
        center = len(strip) // 2
        for radius in range(1, len(strip) // 2 + 1):
            strip.fill((0, 0, 0))  # Clear the strip
            if center - radius >= 0:
                strip[center - radius] = color
            if center + radius < len(strip):
                strip[center + radius] = color
            strip.show()
            time.sleep(0.1)