from .pattern import Pattern
import time
from .putil import *

NUM_PIXELS = 300

class Test(Pattern):

    @classmethod
    def get_id(self):
        return 13

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
                color = heat_to_color(heat[i])
                strip[i] = color
            strip.show()
            time.sleep(0.03)

def heat_to_color(heat):
    """
    Convert a heat value (0-255) into an RGB color representing a flame.
    Heat levels:
        - 0: Black
        - 128: Red/Orange
        - 255: Bright Yellow/White
    """
    # Scale 'heat' into three regions: black -> red -> orange -> yellow
    t192 = (heat * 192) // 255  # Scale to 0–192 for ease of calculations

    # Calculate RGB based on heat levels
    if t192 <= 64:
        # Scale from black to red
        red = t192 * 255 // 64
        green = 0
        blue = 0
    elif t192 <= 128:
        # Scale from red to orange
        red = 255
        green = (t192 - 64) * 255 // 64
        blue = 0
    else:
        # Scale from orange to yellow
        red = 255
        green = 255
        blue = (t192 - 129) * 255 // 126

    return (red, green, blue)
