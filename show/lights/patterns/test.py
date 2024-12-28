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
        colors = [(0, 255, 128), (0, 64, 255), (0, 128, 128), (0, 255, 64)]
        for offset in range(NUM_PIXELS):
            for i in range(NUM_PIXELS):
                if (i + offset) % 3 == 0:
                    strip.setPixelColor(i, color)
                else:
                    strip.setPixelColor(i, (0, 0, 0))
            strip.show()
            time.sleep(delay)