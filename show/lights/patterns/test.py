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
        color1 = get_random_color()
        color2 = get_random_color()
        iterations=100
        size = 5
        delay=0.1
        gravity=0.8
        center = random.randint(0, NUM_PIXELS - 1)
        for i in range(NUM_PIXELS):
            if i % 2 == 0:
                strip.setPixelColor(i, (255, 0, 0))  # Red
            else:
                strip.setPixelColor(i, (255, 255, 255))  # White
        strip.show()
        time.sleep(delay)