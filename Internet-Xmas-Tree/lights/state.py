class State(object):
    """
    Represents the state updated by the API
    """
    # the unix time when the file has been last updated
    last_updated_time = 0
    # the path of the file to read the state from
    # colors 1 and 2, that must be tuples or lists w/ max value 255
    color1 = (255, 0, 0)
    color2 = (0, 0, 0)
    # if color1/2 are random
    random1 = False
    random2 = False
    # the pattern id to use
    pattern = 1
    # depending on the pattern, typically is how many LEDs
    # wide the pattern is
    length = 5
    # how long in milliseconds the pattern takes to show a difference
    delay = 10

