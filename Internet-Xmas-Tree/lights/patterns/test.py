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
        for j in range(255 * 10):
            for i in range(len(strip)):
                brightness = int((1 + math.sin(i + j / 10.0)) * 127.5)
                scaled_color = tuple(c * brightness // 255 for c in color)
                strip[i] = scaled_color
            strip.show()
            time.sleep(0.1)