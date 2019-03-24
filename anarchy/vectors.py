import math

from anarchy import *

class Vector2:
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, val):
        return Vector2(self.x + val.x, self.y + val.y)

    def __sub__(self, val):
        return Vector2(self.x - val.x, self.y - val.y)

    def correction_to(self, ideal):
        correction = math.atan2(self.y, -self.x) - math.atan2(ideal.y, -ideal.x) # The in-game axes are left handed, so use -x
        return correction if abs(correction) <= math.pi else (sign(correction) * 2 * math.pi) # Make sure we go the 'short way'
