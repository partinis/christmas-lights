from .pattern import Pattern
import time
import random
from .putil import *

class FillDownRandom(Pattern):

    @classmethod
    def get_id(self):
        return 17

    @classmethod
    def update(self, strip, state):
        LED_COUNT = len(strip)
        SpeedDelay = 0
        DisplayDelay = .1
        PauseDelay = 1
        FlushDelay = .2
        SetAll(strip, Color(0, 0, 0))
        #Fill down with random colors
        for i in range(0, LED_COUNT):
            r=random.randint(0, 255)
            g=random.randint(0, 255)
            b=random.randint(0, 255)
            for j in range(0,LED_COUNT-i):
                strip.setPixelColor(j, Color(r, g, b))
                if j>0:
                    strip.setPixelColor(j-1, Color(0, 0, 0))
                strip.show()
                time.sleep(SpeedDelay)
            time.sleep(DisplayDelay)
        time.sleep(PauseDelay)
        #"Flush" results
        for i in range(LED_COUNT-1, -1, -1):
            for j in range(LED_COUNT-1, 0, -1):
                OldColor = strip.getPixelColor(j-1)
                strip.setPixelColor(j, OldColor)
            strip.setPixelColor(i-LED_COUNT+1, Color(0, 0, 0))
            strip.show()
            time.sleep(FlushDelay)
        time.sleep(PauseDelay)