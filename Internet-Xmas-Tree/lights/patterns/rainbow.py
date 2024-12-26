"""
"Cylon" pattern
"""

from .pattern import Pattern
import time
import math
import Color

class Cylon(Pattern):

    def __init__(self):
        pass

    @classmethod
    def get_id(self):
        return 14

    @classmethod
    def update(self, strip, state):
        LED_COUNT = len(strip)
        SpeedDelay = 0
        for j in range(256):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, wheel((i + j) & 255))
            strip.show()
            time.sleep(20 / 1000.0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

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