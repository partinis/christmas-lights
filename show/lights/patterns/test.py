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
        colors = [(0, 255, 128), (0, 64, 255), (0, 128, 255), (0, 255, 64)]
        for _ in range(50):  # Cycles
            for color in colors:
                for i in range(NUM_PIXELS):
                    strip.setPixelColor(i, color)
                strip.show()
                time.sleep(.1)