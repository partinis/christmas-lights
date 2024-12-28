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
        iterations=100
        for _ in range(iterations):
            for i in range(NUM_PIXELS):
                if random.random() < 0.2:  # 20% chance of a snowflake
                    strip.setPixelColor(i, (255, 255, 255))  # White
                else:
                    strip.setPixelColor(i, (0, 0, 0))  # Off
            strip.show()
            time.sleep(.05)