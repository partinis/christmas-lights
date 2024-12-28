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
        for i in range(strip.numPixels()):
            r = random.randint(100, 255)
            g = random.randint(50, 150)
            b = random.randint(0, 50)
            strip.setPixelColor(i, (r, g, b))
        strip.show()
        time.sleep(0.1)