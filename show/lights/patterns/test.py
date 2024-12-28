from .pattern import Pattern
import time
import math
from .putil import *

NUM_PIXELS = 300

class Test(Pattern):

    @classmethod
    def get_id(self):
        return 0

    @classmethod
    def update(self, strip, state):
        color = get_random_color()
        color1 = get_random_color()
        color2 = get_random_color()
        iterations=100
        size = 5
        delay=0.1
        gravity=0.8
        colors = [(0, 255, 128), (0, 64, 255), (0, 128, 128), (0, 255, 64)]
        for j in range(256):
            for i in range(NUM_PIXELS):
                color_index = (i + j) % len(colors)
                intensity = (math.sin(i + j) * 127 + 128) / 255  # Sine wave
                adjusted_color = tuple(int(c * intensity) for c in colors[color_index])
                strip.setPixelColor(i, adjusted_color)
            strip.show()
            time.sleep(delay)