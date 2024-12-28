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
        color = (0,0,255)
        trail_color=(0, 0, 0)
        for i in range(NUM_PIXELS + 3):
            for j in range(NUM_PIXELS):
                strip.setPixelColor(j, trail_color)  # Clear trail
            for j in range(3):
                if 0 <= i - j < NUM_PIXELS:
                    strip.setPixelColor(i - j, color)  # Draw moving light
            strip.show()
            time.sleep(.1)