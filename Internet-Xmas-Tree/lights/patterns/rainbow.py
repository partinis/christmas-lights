"""
"Cylon" pattern
"""

from .pattern import Pattern
import time
import math

class Cylon(Pattern):

    def __init__(self):
        pass

    @classmethod
    def get_id(self):
        return 14

    @classmethod
    def update(self, strip, state):
        LED_COUNT = len(strip)
        SpeedDelay = .1
        for i in range(0, 256):
            for j in range(0, LED_COUNT):
                strip[j] = Wheel((j + i) & 255)
            strip.show()
            time.sleep(SpeedDelay)

def Wheel(WheelPosition):
    #Generate rainbow colors across 0-255 positions.
    if WheelPosition < 85:
        return (WheelPosition * 3, 255 - WheelPosition * 3, 0)
    elif WheelPosition < 170:
        WheelPosition -= 85
        return (255 - WheelPosition * 3, 0, WheelPosition * 3)
    else:
        WheelPosition -= 170
        return (0, WheelPosition * 3, 255 - WheelPosition * 3)