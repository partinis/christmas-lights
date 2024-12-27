from .pattern import Pattern
import time
from .putil import *

NUM_PIXELS = 300

christmasColors = {
    0: (255, 0, 0),    #Red
    1: (0, 255, 0),    #Green
    2: (0, 0, 255),    #Blue
    3: (255, 140, 0),  #Orange
    4: (102, 0, 102),  #Puprle
    5: (0, 0, 0)       #off
}

class Test(Pattern):

    @classmethod
    def get_id(self):
        return 0

    @classmethod
    def update(self, strip, state):
        for idx in range(0, NUM_PIXELS):
            strip[idx] = get_random_color()
            strip.show()
            time.sleep(.025)

        for idy in range(0, 5):
            for idx in range(0, NUM_PIXELS):
                strip[idx] = christmasColors[idy]
                strip.show()
                time.sleep(.025)

        for idx in range(0, NUM_PIXELS):
            strip[idx] = get_random_color()
            strip.show()
            time.sleep(.025)