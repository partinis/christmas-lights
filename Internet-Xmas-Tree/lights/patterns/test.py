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
        for r in range(center):
            strip.fill((0, 0, 0))
            strip[center - r:center + r] = [color] * (2 * r)
            strip.show()
            time.sleep(0.1)