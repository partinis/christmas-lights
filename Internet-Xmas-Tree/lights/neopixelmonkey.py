import neopixel
import board
from scour.scour import colors


class NeoPixel(object):
    def __new__(cls, conf, *args, **kwargs):
        instance = neopixel.NeoPixel(board.D18, int(conf.count), bpp=3, auto_write=False, brightness=conf.brightness, pixel_order=neopixel.GRB)

        def setPixelColor(self, n, color):
            instance[n] = color

        return instance