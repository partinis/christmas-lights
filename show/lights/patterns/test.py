from .pattern import Pattern
import time
import math
from .putil import *

NUM_PIXELS = 10
NUM_LEDS = 300

pixels = [
    {
        "pos": random.randint(0, NUM_LEDS - 1),  # Random initial position
        "range_start": random.randint(0, NUM_LEDS // 2),  # Random start of range
        "range_end": random.randint(NUM_LEDS // 2, NUM_LEDS - 1),  # Random end of range
        "direction": random.choice([-1, 1]),  # Random initial direction
        "color": (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)),  # Random color
    }
    for _ in range(NUM_PIXELS)
]

class Test(Pattern):

    @classmethod
    def get_id(self):
        return 0

    @classmethod
    def update(self, strip, state):
        speed_delay = 0.05
        while True:
            # Clear the strip
            strip.fill((0, 0, 0))

            # Update each pixel's position
            for pixel in pixels:
                # Move pixel position
                pixel["pos"] += pixel["direction"]

                # Check boundaries within the range
                if pixel["pos"] >= pixel["range_end"] or pixel["pos"] <= pixel["range_start"]:
                    pixel["direction"] *= -1  # Reverse direction

                # Render the pixel
                strip[pixel["pos"]] = pixel["color"]

            # Progress all pixels to the left after each cycle
            for pixel in pixels:
                pixel["range_start"] = max(0, pixel["range_start"] - 1)
                pixel["range_end"] = max(pixel["range_start"] + 1, pixel["range_end"] - 1)
                pixel["pos"] = max(pixel["range_start"], min(pixel["pos"], pixel["range_end"]))

            # Update the strip
            strip.show()
            time.sleep(speed_delay)