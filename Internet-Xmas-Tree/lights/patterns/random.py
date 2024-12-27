"""
Random pattern
"""
from .putil import *

from .pattern import Pattern
import time

class Random(Pattern):
    @classmethod
    def get_id(self):
        return 5

    @classmethod
    def update(self, strip, state):
        for _ in range(50):
            for i in range(10):
                strip[get_random_pixel()] = get_random_color()
                time.sleep(0.1)
            strip.show()
            time.sleep(0.1)
            strip.fill((0, 0, 0))