from .pattern import Pattern
import time

class Rainbow(Pattern):

    def __init__(self):
        pass

    @classmethod
    def get_id(self):
        return 14

    @classmethod
    def update(self, strip, state):
        LED_COUNT = len(strip)
        SpeedDelay = 0
        for j in range(256):
            for i in range(LED_COUNT):
                strip[i] = wheel((i + j) & 255)
            strip.show()
            time.sleep(20 / 1000.0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def Color(red, green, blue, white = 0):
    """Convert the provided red, green, blue color to a 24-bit color value.
    Each color component should be a value 0-255 where 0 is the lowest intensity
    and 255 is the highest intensity.
    """
    return (white << 24) | (red << 16) | (green << 8) | blue