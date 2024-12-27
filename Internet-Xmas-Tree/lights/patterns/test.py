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
        color = (255,0,0)
        for _ in range(50):  # Number of twinkles
            index = random.randint(0, len(strip) - 1)
            strip[index] = color
            strip.show()
            time.sleep(.01)
            for b in range(255, 0, -10):  # Fade out
                faded_color = tuple(c * b // 255 for c in color)
                strip[index] = faded_color
                strip.show()
                time.sleep(.01 / 5)
            strip[index] = (0, 0, 0)