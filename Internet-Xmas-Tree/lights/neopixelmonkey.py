import neopixel
import board

class NeoPixel(object):
    def __new__(cls, conf, *args, **kwargs):
        instance = neopixel.NeoPixel(board.D18, int(conf.count), bpp=3, auto_write=False, brightness=conf.brightness, pixel_order=neopixel.GRB)

        def setPixelColor(self, n, color):
            instance[n] = color

        instance.setPixelColor = setPixelColor.__get__(instance)

        return instance