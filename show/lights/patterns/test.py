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
        for j in range(0, 256 * 1):
            for i in range(strip.numPixels()):
                intensity = (math.sin(i + j) * 127 + 128) / 255  # Sine wave intensity
                adjusted_color = tuple(int(c * intensity) for c in color)
                strip.setPixelColor(i, adjusted_color)
            strip.show()
            time.sleep(.05)