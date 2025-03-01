"""
Lights Client

Responsible for setting the pattern of lights from the data file
"""

import neopixelmonkey
import time
import threading
import sys
import random
import inspect
import importlib
from patterns.pattern import Pattern
from config import Config
from state import State
from util import get_random_color

patterns = [
    # 'patterns.solid',
    # 'patterns.blink',
    'patterns.scroll',
    'patterns.wipeup',
    # 'patterns.wipedown',
    'patterns.random',
    'patterns.larson',
    # 'patterns.scrollsmooth',
    # 'patterns.pulse',
    'patterns.traditional',
    # 'patterns.colorbeams',
    'patterns.colorbeams2',
    'patterns.cylon',
    'patterns.rainbow',
    'patterns.meteorrain',
    'patterns.newkitt',
    'patterns.filldownrandom',
    'patterns.randomcolors',
    'patterns.twinkle',
    'patterns.scrollrows',
    'patterns.chaser',
    'patterns.dashedchaser',
    'patterns.fire',
    'patterns.confetti',
    'patterns.fireworks',
    'patterns.colorsnow',
    'patterns.randommove',
    # 'patterns.test',
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
    conf = Config()
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
    with neopixelmonkey.NeoPixel(conf) as strip:
        state = State()
        # state.pattern = sys.argv[1]
        # state.pattern = int(sys.argv[1])
        try:
            while True:
                if len(sys.argv) > 1:
                    state.pattern = int(sys.argv[1])
                else:
                    state.pattern = random.choice(list(pattern_handlers.keys()))
                print("Calling function " + str(state.pattern))
                # update the state of the led strip
                try:
                    update(strip, state, pattern_handlers)
                    # write the data to the led strip
                    strip.show()
                except:
                    pass
        except Exception as e:
            raise e
