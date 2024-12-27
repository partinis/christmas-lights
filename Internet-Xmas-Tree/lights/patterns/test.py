from .pattern import Pattern
import time
from .putil import *

NUM_PIXELS = 300
HALF_NUM_PIXELS = 150

class Test(Pattern):

    @classmethod
    def get_id(self):
        return 0

    @classmethod
    def update(self, strip, state):
        delay_count = 0
        while(delay_count < 1000):
            print("fdsf"+str(get_random_pixel())+"fdsf"+str(get_random_color()))
            strip[get_random_pixel()] = get_random_color()
            time.sleep(.01)
            delay_count = delay_count + 1

        random_color = get_random_color()

        for idx in range(0, HALF_NUM_PIXELS):
            strip[idx] = random_color
            strip[(NUM_PIXELS - 1) - idx] = random_color
            time.sleep(.01)

        time.sleep(.25)

        for idx in range(0, HALF_NUM_PIXELS):
            strip[HALF_NUM_PIXELS + idx] = get_random_color()
            strip[(HALF_NUM_PIXELS - 1) - idx] = get_random_color()
            time.sleep(.01)