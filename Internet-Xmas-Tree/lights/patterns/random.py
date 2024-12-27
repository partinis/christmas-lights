"""
Random pattern
"""
from .putil import *

from .pattern import Pattern
import random
import time

class Random(Pattern):
    @classmethod
    def get_id(self):
        return 5

    @classmethod
    def update(self, strip, state):
        for _ in range(50):
            index = random.randint(0, len(strip) - 1)
            strip[index] = get_random_color()
            strip.show()
            time.sleep(0.1)
            strip[index] = (0, 0, 0)