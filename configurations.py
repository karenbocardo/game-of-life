ON = 255
OFF = 0

class configuration:
  def __init__(self, name, conf):
    self.name = name
    self.conf = conf

# STILL LIFES

block = [[ON, ON],
          [ON, ON]]
BLOCK = configuration("block", [block])

beehive = [[OFF, ON, ON, OFF],
            [ON, OFF, OFF, ON],
            [OFF, ON, ON, OFF]]
BEEHIVE = configuration("beehive", [beehive])

loaf = [[OFF, ON, ON, OFF],
        [ON, OFF, OFF, ON],
        [OFF, ON, OFF, ON],
        [OFF, OFF, ON, OFF]]
LOAF = configuration("loaf", [loaf])

boat = [[ON, ON, OFF],
        [ON, OFF, ON],
        [OFF, ON, OFF]]
BOAT = configuration("boat", [boat])

tub = [[OFF, ON, OFF],
        [ON, OFF, ON],
        [OFF, ON, OFF]]
TUB = configuration("tub", [tub])

STILL = [BLOCK, BEEHIVE, LOAF, BOAT, TUB]

# OSCILATORS (period 2)
blinker = list()
blinker.append([[ON],
                [ON],
                [ON]])
blinker.append([[ON, ON, ON]])
BLINKER = configuration("blinker", blinker)

toad = list()
toad.append([[OFF, OFF, ON, OFF],
            [ON, OFF, OFF, ON],
            [ON, OFF, OFF, ON],
            [OFF, ON, OFF, OFF]])
toad.append([[OFF, ON, ON, ON],
             [ON, ON, ON, OFF]])
TOAD = configuration("toad", toad)

beacon = list()
beacon.append([[ON, ON, OFF, OFF],
                [ON, ON, OFF, OFF],
                [OFF, OFF, ON, ON],
                [OFF, OFF, ON, ON]])
beacon.append([[ON, ON, OFF, OFF],
                [ON, OFF, OFF, OFF],
                [OFF, OFF, OFF, ON],
                [OFF, OFF, ON, ON]])
BEACON = configuration("beacon", beacon)

OSC = [BLINKER, TOAD, BEACON]

# spaceships
glider = list()
glider.append([[OFF, ON, OFF],
                [OFF, OFF, ON],
                [ON, ON, ON]])
glider.append([[ON, OFF, ON],
                [OFF, ON, ON],
                [OFF, ON, OFF]])
glider.append([[OFF, OFF, ON],
                [ON, OFF, ON],
                [OFF, ON, ON]])
glider.append([[ON, OFF, OFF],
                [OFF, ON, ON],
                [ON, ON, OFF]])
GLIDER = configuration("glider", glider)

light = list()
light.append([[ON, OFF, OFF, ON, OFF],
              [OFF, OFF, OFF, OFF, ON],
              [ON, OFF, OFF, OFF, ON],
              [OFF, ON, ON, ON, ON]])
light.append([[OFF, OFF, ON, ON, OFF],
              [ON, ON, OFF, ON, ON],
              [ON, ON, ON, ON, OFF],
              [OFF, ON, ON, OFF, OFF]])
light.append([[OFF, ON, ON, ON, ON],
              [ON, OFF, OFF, OFF, ON],
              [OFF, OFF, OFF, OFF, ON],
              [ON, OFF, OFF, ON, OFF]])
light.append([[OFF, ON, ON, OFF, OFF],
              [ON, ON, ON, ON, OFF],
              [ON, ON, OFF, ON, ON],
              [OFF, OFF, ON, ON, OFF]])
LIGHT = configuration("light-w", light)

SPACE = [GLIDER]

ALL_CONFIGS = STILL + OSC + SPACE


counters = dict()