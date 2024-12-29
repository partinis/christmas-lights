"""
Color beams pattern 2

"""

from .pattern import Pattern

import colorsys
import time

NUM_PIXELS = 300

class ColorBeams(Pattern):

    @staticmethod
    def getHue(hue):
        hsv = colorsys.hsv_to_rgb(hue, 1, 1)
        return int(hsv[0] * 255), int(hsv[1] * 255), int(hsv[2] * 255)

    @staticmethod
    def highlight(strip, i, hue = 0.5):
        i = i % NUM_PIXELS
        # set the color of this pixel
        strip[i] = ColorBeams.getHue(hue)
        for x in range(20):
            index = (i - x) % NUM_PIXELS
            decay = pow(0.7, x)
            # strip[index] = (int(strip[index][0] * decay), int(strip[index][1] * decay), int(strip[index][2] * decay))
            strip[index] = (int(strip[i][0] * decay), int(strip[i][1] * decay), int(strip[i][2] * decay))
            strip[NUM_PIXELS-index] = (int(strip[i][0] * decay), int(strip[i][1] * decay), int(strip[i][2] * decay))

    @staticmethod
    def __get_time():
        return time.time() * 1000

    def __init__(self):
        pass

    @classmethod
    def get_id(self):
        return 0

    @classmethod
    def update(self, strip, state):
        for i in range(NUM_PIXELS):
            for y in range(0, NUM_PIXELS, 50):
                ColorBeams.highlight(strip, i + y, (5 * y / NUM_PIXELS) % 1)
            if i % 1 == 0:
                strip.show()