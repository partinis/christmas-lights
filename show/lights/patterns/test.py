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
        for t in range(50):
            blend_color = tuple(
                int(color1[i] + (color2[i] - color1[i]) * (t / 50)) for i in range(3)
            )
            for i in range(NUM_PIXELS):
                strip.setPixelColor(i, blend_color)
            strip.show()
            time.sleep(.01)