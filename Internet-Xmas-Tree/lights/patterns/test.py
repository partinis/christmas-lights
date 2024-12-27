from .pattern import Pattern
import time
from .putil import *

NUM_PIXELS = 300
fade_value = 10

class Test(Pattern):

    @classmethod
    def get_id(self):
        return 0

    @classmethod
    def update(self, strip, state):
        for i in range(len(strip) + len(strip) // 2):
            for j in range(len(strip)):
                if random.randint(0, 10) > 5:
                    strip[j] = (10,10,10)

            if i < len(strip):
                strip[i] = (255, 0, 0)
            strip.show()
            time.sleep(0.1)

def fade_to_black(strip, index):
    """
    Fades the brightness of a specific LED to simulate a 'fade to black' effect.

    Parameters:
    - strip (neopixel.NeoPixel): The NeoPixel strip object.
    - index (int): The index of the pixel to fade.
    - fade_value (int): The amount to fade the pixel by (0-255).

    Returns:
    - None: The function updates the pixel color in the strip directly.
    """
    # Get the current color of the pixel
    color = strip[index]

    # Calculate the faded color
    # faded_color = tuple(max(0, c - fade_value) for c in color)

    # Update the pixel color
    strip[index] = (10, 10, 10)