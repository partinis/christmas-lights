from .pattern import Pattern
import time
from .putil import *

rowOrginList = [0, 45, 80, 104, 117, 128, 158, 203, 236, 264, 290]
numPixelList = [45, 35, 24, 13, 14, 30, 45, 33, 28, 26, 10]

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
        color = 0
        loop = 0
        count = 25
        while(loop < count):

            color = loop % 5

            for row in range(0, 5):
                if(color > 4):
                    color = 0
                fill_row(strip, row, christmasColors[color])
                color = color + 1

            strip.show()
            time.sleep(.5)
            loop = loop + 1

def fill_row(strip, row, color):
    """"Fills row with given color
        row - row to fill (0..4)
        color - color from christmasColors dictionary
        Returns - none
    """

    idxStart = rowOrginList[row]
    numPixels = numPixelList[row]

    for idx in range(idxStart, (idxStart + numPixels)):
        strip[idx] = color