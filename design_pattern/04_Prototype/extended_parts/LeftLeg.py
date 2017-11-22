from base_parts import Leg


class LeftLeg(Leg):

    __size = None

    def __init__(self, size):
        LeftLeg.__size = size

    def size(self):
        return LeftLeg.__size()