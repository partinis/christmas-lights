from .pattern import Pattern
import time
import random
from .putil import *

class RandomColors(Pattern):

    @classmethod
    def get_id(self):
        return 18

    @classmethod
    def update(self, strip, state):
        LED_COUNT = len(strip)
        SpeedDelay = .1
        SetAll(strip, Color(0, 0, 0))
        for i in range (0, 1000):
            for i in range(0, LED_COUNT):
                r=random.randint(0, 255)
                g=random.randint(0, 255)
                b=random.randint(0, 255)
                strip.setPixelColor(i, Color(r, g, b))
            strip.show()
            time.sleep(SpeedDelay)