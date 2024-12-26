"""
Lights Client

Responsible for setting the pattern of lights from the data file
"""

import neopixel
import board
import time
import threading
import sys
import inspect
import importlib
from patterns.pattern import Pattern
from config import Config
from state import State
from util import get_random_color

patterns = [
    'patterns.blink',
    'patterns.solid',
    'patterns.traditional',
    'patterns.pulse',
    'patterns.scroll',
    'patterns.scrollsmooth',
    'patterns.random',
    'patterns.larson',
    'patterns.wipeup',
    'patterns.wipedown',
    'patterns.colorbeams',
    ]


def update(strip, state, pattern_handlers):
    """
    Updates the neopixel state using the dynamically loaded modules from the list of the patterns
    :param strip:
    :return:
    """
    # update the random colors if used
    if state.random1:
        state.color1 = get_random_color()
    if state.random2:
        state.color2 = get_random_color()
    # run the update method for the pattern handler with the matching pattern id
    if state.pattern in pattern_handlers:
        pattern_handlers[state.pattern].update(strip, state)
    else:
        # if not found, use solid color, which should always be at 0
        pattern_handlers[0].update(strip, state)

if __name__ == '__main__':
    config_file = "../configuration.ini"
    conf = Config(config_file)
    conf.load()

    state = State()

    # import all the patterns
    pattern_handlers = {}
    for p in patterns:
        # import the module
        mod = importlib.import_module(p)
        # get all of the Pattern subclasses defined inside this module
        for name, obj in inspect.getmembers(mod):
            if obj is not Pattern and isinstance(obj, type) and issubclass(obj, Pattern):
                # append an instance of this class into the handler dict, by the pattern id
                instance = obj()
                pattern_handlers[instance.get_id()] = instance

    # initialize the led strip
    with neopixel.NeoPixel(board.D18, int(conf.count), bpp=3, auto_write=False, brightness=conf.brightness, pixel_order=neopixel.GRB) as strip:
        state = State()
        # state.pattern = sys.argv[1]
        state.pattern = 8
        state.color1 = (255, 0, 0)
        state.color2 = (0, 255, 0)
        state.len = 1
        state.delay = 5000
        state.random1 = False
        state.random2 = False
        try:
            while True:
                print("Calling function "+str(state.pattern))
                # update the state of the led strip
                update(strip, state, pattern_handlers)
                # write the data to the led strip
                strip.show()
                # don't delay at all because the writing process is already slow enough
        except (KeyboardInterrupt, SystemExit):
            pass
        except Exception as e:
            raise e