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
        return 22

    @classmethod
    def update(self, strip, state):
        color = 0
        loops = 130 * 3

        for idx in range(0, NUM_PIXELS):
            strip[idx] = christmasColors[color]
            strip.show()
            time.sleep(.025)

            if(((idx + 1) % 26) == 0):
                color = color + 1
                if(color > 4):
                    color = 0

        while(loops):
            loops = loops - 1
            temp = strip[NUM_PIXELS - 1]
            for idx in range((NUM_PIXELS - 1), -1, -1):
                if(idx):
                    strip[idx] = strip[idx -1]
            strip[0] = temp
            strip.show()