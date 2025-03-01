"""
Configuration Object

Stores information about the configuration, 
as parsed from the configuration file.
"""

import configparser

class Config(object):
    patterns = {}
    count = 300
    brightness = .05

    def __init__(self, **kwargs):
        """
        Constructor
        """