from .pattern import Pattern
import time
from .putil import *

NUM_LEDS = 300

class Randommove(Pattern):

    @classmethod
    def get_id(self):
        return 27

    @classmethod
    def update(self, strip, state):
        num_pixels = 10
        speed_delay = 0.05
        positions = [random.randint(0, NUM_LEDS - 1) for _ in range(num_pixels)]  # Random starting positions
        directions = [1 if random.random() > 0.5 else -1 for _ in range(num_pixels)]  # Random initial directions

        for _ in range(NUM_LEDS):
            # Clear the strip
            strip.fill((0, 0, 0))

            # Move each pixel
            for i in range(num_pixels):
                # Set the pixel color
                if 0 <= positions[i] < NUM_LEDS:  # Only light up if within bounds
                    strip[positions[i]] = get_random_color()

                # Update position
                positions[i] += directions[i]

                # Reverse direction if hitting bounds
                if positions[i] >= NUM_LEDS - 1 or positions[i] <= 0:
                    directions[i] *= -1

                # Progress to the left if the direction is now left
                if directions[i] == -1 and positions[i] > 0:
                    positions[i] -= 1  # Move leftward

            # Update the strip
            strip.show()
            time.sleep(speed_delay)
