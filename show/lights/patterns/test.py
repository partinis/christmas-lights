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
        color1 = (255,0,0)
        color2 = (0,0,255)
        for i in range(NUM_PIXELS):
            r = int(color1[0] + (color2[0] - color1[0]) * (i / NUM_PIXELS))
            g = int(color1[1] + (color2[1] - color1[1]) * (i / NUM_PIXELS))
            b = int(color1[2] + (color2[2] - color1[2]) * (i / NUM_PIXELS))
            strip.setPixelColor(i, (r, g, b))
        strip.show()
        time.sleep(.05)