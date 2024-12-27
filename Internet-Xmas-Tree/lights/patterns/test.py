from .pattern import Pattern
import time
from .putil import *

NUM_PIXELS = 300

class Test(Pattern):

    @classmethod
    def get_id(self):
        return 0

    @classmethod
    def update(self, strip, state):
        cooling=55
        sparking=120
        heat = [0] * len(strip)

        for _ in range(100):
            for i in range(len(strip)):
                heat[i] = max(0, heat[i] - random.randint(0, cooling))

            for i in range(len(strip) - 1, 1, -1):
                heat[i] = (heat[i - 1] + heat[i - 2] + heat[i - 2]) // 3

            if random.randint(0, 255) < sparking:
                heat[random.randint(0, len(strip) - 1)] += random.randint(160, 255)

            for i in range(len(strip)):
                # color = heat_to_color(heat[i])
                color = (255,0,0)
                strip[i] = color
            strip.show()
            time.sleep(0.03)
