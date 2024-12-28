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
        colors = [(0, 255, 128), (0, 64, 255), (0, 128, 128), (0, 255, 64)]
        color = get_random_color()
        color1 = get_random_color()
        color2 = get_random_color()
        iterations=100
        size = 5
        delay=0.1
        gravity=0.8
        positions = [0] * len(colors)
        velocities = [0] * len(colors)
        while True:
            for i in range(len(colors)):
                velocities[i] += gravity
                positions[i] += velocities[i]
                if positions[i] >= NUM_PIXELS:
                    positions[i] = NUM_PIXELS - 1
                    velocities[i] *= -0.9
                strip.setPixelColor(int(positions[i]), colors[i])
            strip.show()
            time.sleep(delay)
            for i in range(NUM_PIXELS):
                strip.setPixelColor(i, (0, 0, 0))  # Clear strip