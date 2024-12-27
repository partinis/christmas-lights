from .pattern import Pattern
import time
import math
from .putil import *

class Cylon(Pattern):

    @classmethod
    def get_id(self):
        return 13

    @classmethod
    def update(self, strip, state):
        LED_COUNT = len(strip)
        EyeSize = 3
        red = 255
        green = 0
        blue = 0
        SpeedDelay = .1
        ReturnDelay = .5
        for i in range (0, (LED_COUNT - EyeSize - 2)):
            SetAll(strip, Color(0, 0, 0))
            strip.setPixelColor(i, Color(int(math.floor(red / 10)), int(math.floor(green / 10)), int(math.floor(blue / 10))))
            for j in range(1, (EyeSize + 1)):
                strip.setPixelColor(i + j, Color(red, green, blue))
            strip.setPixelColor(i + EyeSize + 1, Color(int(math.floor(red / 10)), int(math.floor(green / 10)), int(math.floor(blue / 10))))
            strip.show()
            time.sleep(SpeedDelay)
        time.sleep(ReturnDelay)
        for i in range ((LED_COUNT - EyeSize - 2), 0, -1):
            SetAll(strip, Color(0, 0, 0))
            strip.setPixelColor(i, Color(int(math.floor(red / 10)), int(math.floor(green / 10)), int(math.floor(blue / 10))))
            for j in range(1, (EyeSize + 1)):
                strip.setPixelColor(i + j, Color(red, green, blue))
            strip.setPixelColor(i + EyeSize + 1, Color(int(math.floor(red / 10)), int(math.floor(green / 10)), int(math.floor(blue / 10))))
            strip.show()
            time.sleep(SpeedDelay)
        time.sleep(ReturnDelay)