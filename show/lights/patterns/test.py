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
        for _ in range(10):
            for i in range(NUM_PIXELS):
                if random.random() < 0.1:  # 10% chance to sparkle
                    color = random.choice([(0, 255, 0), (255, 0, 0), (255, 255, 0)])  # Green, Red, Yellow
                    strip.setPixelColor(i, color)
                else:
                    strip.setPixelColor(i, (0, 0, 0))
            strip.show()
            time.sleep(0.1)