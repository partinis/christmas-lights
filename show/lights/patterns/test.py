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
        color = (255, 255, 255)
        for i in range(NUM_PIXELS):
            strip.setPixelColor(i, (0, 0, 0))  # Clear all LEDs
        snowflakes = [random.randint(0, NUM_PIXELS - 1) for _ in range(5)]  # Random starting points
        for _ in range(NUM_PIXELS):
            for i in range(len(snowflakes)):
                if snowflakes[i] > 0:
                    strip.setPixelColor(snowflakes[i], (0, 0, 0))  # Turn off old position
                    snowflakes[i] -= 1
                    strip.setPixelColor(snowflakes[i], color)  # Set new position
            strip.show()
            time.sleep(0.1)