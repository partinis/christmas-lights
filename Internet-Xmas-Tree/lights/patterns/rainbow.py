from .pattern import Pattern
import time
from .putil import *

class Rainbow(Pattern):

    @classmethod
    def get_id(self):
        return 14

    @classmethod
    def update(self, strip, state):
        LED_COUNT = len(strip)
        SpeedDelay = 0
        for i in range(0, 256):
            for j in range(0, LED_COUNT):
                strip.setPixelColor(j, Wheel((j + i) & 255))
            strip.show()
            time.sleep(SpeedDelay)

def Wheel(WheelPosition):
    #Generate rainbow colors across 0-255 positions.
    if WheelPosition < 85:
        return Color(WheelPosition * 3, 255 - WheelPosition * 3, 0)
    elif WheelPosition < 170:
        WheelPosition -= 85
        return Color(255 - WheelPosition * 3, 0, WheelPosition * 3)
    else:
        WheelPosition -= 170
        return Color(0, WheelPosition * 3, 255 - WheelPosition * 3)