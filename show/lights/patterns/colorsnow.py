from .pattern import Pattern
import time
import math
from .putil import *

NUM_PIXELS = 300


class Colorsnow(Pattern):

    @classmethod
    def get_id(self):
        return 26

    @classmethod
    def update(self, strip, state):
        delay = 0.1
        snow = [0] * NUM_PIXELS
        for _ in range(100):
            snow[random.randint(0, NUM_PIXELS - 1)] = 1
            for i in range(NUM_PIXELS - 1, 0, -1):
                snow[i] = snow[i - random.randint(1, 3) - 1]
            snow[0] = 0
            for i in range(NUM_PIXELS):
                if snow[i]:
                    strip.setPixelColor(i, get_random_color())
                else:
                    strip.setPixelColor(i, (0, 0, 0))
            strip.show()
            time.sleep(delay * random.randint(1, 2))
