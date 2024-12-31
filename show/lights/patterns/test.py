from .pattern import Pattern
import time
import math
from .putil import *

NUM_PIXELS = 300
NUM_LEDS = 300

class Test(Pattern):

    @classmethod
    def get_id(self):
        return 0

    @classmethod
    def update(self, strip, state):
        color = get_random_color()
        color1 = get_random_color()
        color2 = get_random_color()
        red = 200
        green = 0
        blue = 0
        iterations=100
        size = 5
        delay=0.1
        gravity=0.8
        EyeSize = 4
        center = random.randint(0, NUM_PIXELS - 1)
        snow = [0] * NUM_PIXELS
        pixel_pos = 0
        direction = 1
        speed_delay = 0.05
        while pixel_pos < NUM_LEDS:
            #Clear the strip
            strip.fill((0, 0, 0))

            # Set the current pixel
            strip[pixel_pos] = color

            # Update the strip
            strip.show()
            time.sleep(speed_delay)

            # Move the pixel
            pixel_pos += direction

            # Reverse direction if hitting boundaries
            if pixel_pos >= NUM_LEDS - 1 or pixel_pos <= 0:
                direction *= -1  # Change direction
                # Progressively move forward
                if direction == -1:  # Only progress after one full ping-pong cycle
                    pixel_pos += 1  # Move forward one step