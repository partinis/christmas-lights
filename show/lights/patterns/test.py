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
            # Generate a random range for back-and-forth movement
            move_range = random.randint(3, 8)  # Range length for ping-pong

            # Perform ping-pong movement within the random range
            for offset in range(move_range * 2):  # Forward and backward
                # Clear the strip
                strip.fill((0, 0, 0))

                # Calculate the ping-pong position
                local_pos = pixel_pos + offset if offset < move_range else pixel_pos + (2 * move_range - offset - 1)

                # Ensure it doesn't exceed strip boundaries
                if local_pos >= NUM_LEDS:
                    break

                # Set the current pixel
                strip[local_pos] = color

                # Update the strip
                strip.show()
                time.sleep(speed_delay)

            # Move forward on the strip after the random ping-pong cycle
            pixel_pos += 1