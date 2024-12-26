from .pattern import Pattern
import time
import math
from .putil import *

class NewKitt(Pattern):

    @classmethod
    def get_id(self):
        return 16

    @classmethod
    def update(self, strip, state):
        red = 255
        green = 0
        blue = 0
        EyeSize = 8
        SpeedDelay = .01
        ReturnDelay = .05
        RightToLeft(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)
        LeftToRight(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)
        OutsideToCenter(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)
        CenterToOutside(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)
        RightToLeft(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)
        LeftToRight(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)
        OutsideToCenter(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)
        CenterToOutside(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)

def RightToLeft(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay):
    LED_COUNT = len(strip)
    for i in range(LED_COUNT - EyeSize - 2, 0, -1):
        SetAll(strip, Color(0, 0, 0))
        strip.setPixelColor(i, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        for j in range(1, EyeSize + 1):
            strip.setPixelColor(i + j, Color(red, green, blue))
        strip.setPixelColor(i + EyeSize + 1, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)

def LeftToRight(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay):
    LED_COUNT = len(strip)
    for i in range(0, LED_COUNT - EyeSize - 2):
        SetAll(strip, Color(0, 0, 0))
        strip.setPixelColor(i, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        for j in range(1, EyeSize+1):
            strip.setPixelColor(i + j, Color(red, green, blue))
        strip.setPixelColor(i + EyeSize + 1, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)

def OutsideToCenter(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay):
    LED_COUNT = len(strip)
    for i in range(0, int(math.floor((LED_COUNT-EyeSize)/2))):
        SetAll(strip, Color(0, 0, 0))
        strip.setPixelColor(i, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        for j in range(1, EyeSize + 1):
            strip.setPixelColor(i + j, Color(red, green, blue))
        strip.setPixelColor(i + EyeSize + 1, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        strip.setPixelColor(LED_COUNT - i, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        for j in range(1, EyeSize + 1):
            strip.setPixelColor(LED_COUNT - i - j, Color(red, green, blue))
        strip.setPixelColor(LED_COUNT - i - EyeSize - 1, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)

def CenterToOutside(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay):
    LED_COUNT = len(strip)
    for i in range(int(math.floor((LED_COUNT-EyeSize)/2)), 0, -1):
        SetAll(strip, Color(0, 0, 0))
        strip.setPixelColor(i, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        for j in range(1, EyeSize + 1):
            strip.setPixelColor(i + j, Color(red, green, blue))
        strip.setPixelColor(i + EyeSize + 1, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        strip.setPixelColor(LED_COUNT - i, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        for j in range(1, EyeSize + 1):
            strip.setPixelColor(LED_COUNT - i - j, Color(red, green, blue))
        strip.setPixelColor(LED_COUNT - i - EyeSize - 1, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)