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
        color1 = get_random_color()
        color2 = get_random_color()
        iterations=100
        size = 5
        delay=0.1
        gravity=0.8
        center = random.randint(0, NUM_PIXELS - 1)
        center = random.randint(0, NUM_PIXELS - 1)
        snow = [0] * NUM_PIXELS
        for _ in range(100):
            snow[random.randint(0, NUM_PIXELS - 1)] = 1
            for i in range(NUM_PIXELS - 1, 0, -1):
                snow[i] = snow[i - 1]
            snow[0] = 0
            for i in range(NUM_PIXELS):
                if snow[i]:
                    strip.setPixelColor(i, get_random_color())
                else:
                    strip.setPixelColor(i, (0, 0, 0))
            strip.show()
            time.sleep(delay)