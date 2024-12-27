from .pattern import Pattern
import time
from .putil import *

NUM_PIXELS = 300

class Test(Pattern):

    @classmethod
    def get_id(self):
        return 0

    @classmethod
    def update(self, strip, state):
        for j in range(255):
            for i in range(len(strip)):
                pixel_index = (i * 256 // len(strip)) + j
                strip[i] = wheel(pixel_index & 255)
            strip.show()
            time.sleep(wait)
