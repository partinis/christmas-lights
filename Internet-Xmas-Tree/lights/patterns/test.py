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
        length = 20
        color = (255, 0, 0)
        for i in range(len(strip) + length):
            strip.fill((0, 0, 0))  # Clear the strip
            for j in range(length):
                if 0 <= i - j < len(strip):
                    strip[i - j] = color
            strip.show()
            time.sleep(.1)