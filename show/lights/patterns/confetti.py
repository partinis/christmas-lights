from .pattern import Pattern
import time
import math
from .putil import *

NUM_PIXELS = 300
fade_value = 10

class Test(Pattern):

    @classmethod
    def get_id(self):
        return 24

    @classmethod
    def update(self, strip, state):
        for _ in range(100):  # Number of iterations
            index = random.randint(0, len(strip) - 1)
            color = (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))
            strip[index] = color
            strip.show()
            time.sleep(.1)
            for i in range(len(strip)):
                faded_color = tuple(max(0, c - 10) for c in strip[i])
                strip[i] = faded_color
            strip.show()