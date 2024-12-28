from .pattern import Pattern
import time
import math
from .putil import *

NUM_PIXELS = 300

class Fireworks(Pattern):

    @classmethod
    def get_id(self):
        return 25

    @classmethod
    def update(self, strip, state):
        for _ in range(20):  # Number of fireworks
            burst_center = random.randint(0, NUM_PIXELS - 1)
            for radius in range(1, 10):  # Expand outward
                for i in range(max(0, burst_center - radius), min(NUM_PIXELS, burst_center + radius)):
                    strip.setPixelColor(i, get_random_color())
                strip.show()
                time.sleep(.05)
                for i in range(max(0, burst_center - radius), min(NUM_PIXELS, burst_center + radius)):
                    strip.setPixelColor(i, (0, 0, 0))  # Clear