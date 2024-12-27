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
        steps = 1
        color = (255, 0, 0)
        for b in range(0, 256, steps):
            scaled_color = (color[0] * b // 255, color[1] * b // 255, color[2] * b // 255)
            strip.fill(scaled_color)
            strip.show()
            time.sleep(0.1)
        for b in range(255, -1, -steps):
            scaled_color = (color[0] * b // 255, color[1] * b // 255, color[2] * b // 255)
            strip.fill(scaled_color)
            strip.show()
            time.sleep(0.1)
