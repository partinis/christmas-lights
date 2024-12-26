from .pattern import Pattern
import time
import random
from .putil import *

class MeteorRain(Pattern):

    @classmethod
    def get_id(self):
        return 15

    @classmethod
    def update(self, strip, state):
        LED_COUNT = len(strip)
        red = 255
        green = 0
        blue = 0
        MeteorSize = 5
        MeteorTrailDecay = 64
        MeteorRandomDecay = True
        SpeedDelay = .1
        SetAll(strip, Color(0, 0, 0))
        for i in range(0, LED_COUNT + LED_COUNT):
            # Fade brightness all LEDs one step
            for j in range(0, LED_COUNT):
                if ((not MeteorRandomDecay) or ((random.randint(0, 10) > 5))):
                    FadeToBlack(strip, j, MeteorTrailDecay)
            # Draw meteor
            for j in range(0, MeteorSize):
                if (((i - j) < LED_COUNT) and ((i - j) >= 0)):
                    strip.setPixelColor(i - j, Color(red, green, blue))
            strip.show()
            time.sleep(SpeedDelay)


def FadeToBlack(strip, Position, FadeValue):
    OldColor = strip.getPixelColor(Position)
    if isinstance(OldColor, list):
        OldColor = (OldColor[0] << 16) | (OldColor[1] << 8) | OldColor[2]
    r = (OldColor & 0x00ff0000) >> 16
    g = (OldColor & 0x0000ff00) >> 8
    b = (OldColor & 0x000000ff)
    if (r <= 10):
        r = 0;
    else:
        r = r - int(r * FadeValue / 256)
    if (g <= 10):
        g = 0;
    else:
        g = g - int(g * FadeValue / 256)
    if (b <= 10):
        b = 0;
    else:
        b = b - int(b * FadeValue / 256)
    strip.setPixelColor(Position, Color(r, g, b))
