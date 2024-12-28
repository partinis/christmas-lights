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
        delay=0.1
        for _ in range(iterations):
            burst_center = random.randint(0, NUM_PIXELS - 1)
            for radius in range(1, 10):
                for i in range(max(0, burst_center - radius), min(NUM_PIXELS, burst_center + radius)):
                    strip.setPixelColor(i, (255, 255, 255))  # Bright explosion
                strip.show()
                time.sleep(delay)
                for i in range(max(0, burst_center - radius), min(NUM_PIXELS, burst_center + radius)):
                    strip.setPixelColor(i, (0, 0, 0))  # Fade out