"""
"Cylon" pattern
"""

from .pattern import Pattern
import time
import math

class Cylon(Pattern):

    def __init__(self):
        super(Pattern, self).__init__()

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
        # set all to color2
        for i in range (0, (LED_COUNT - EyeSize - 2)):
            strip.fill((0, 0, 0))
            strip[i] = (int(math.floor(red / 10)), int(math.floor(green / 10)), int(math.floor(blue / 10)))
            for j in range(1, (EyeSize + 1)):
                strip[i + j] = (red, green, blue)
            strip[i + EyeSize + 1] = (int(math.floor(red / 10)), int(math.floor(green / 10)), int(math.floor(blue / 10)))
            strip.show()
            time.sleep(SpeedDelay)
        time.sleep(ReturnDelay)
        for i in range ((LED_COUNT - EyeSize - 2), 0, -1):
            strip.fill((0, 0, 0))
            strip[i] = (int(math.floor(red / 10)), int(math.floor(green / 10)), int(math.floor(blue / 10)))
            for j in range(1, (EyeSize + 1)):
                strip[i + j] = (red, green, blue)
            strip[i + EyeSize + 1] = (int(math.floor(red / 10)), int(math.floor(green / 10)), int(math.floor(blue / 10)))
            strip.show()
            time.sleep(SpeedDelay)
        time.sleep(ReturnDelay)