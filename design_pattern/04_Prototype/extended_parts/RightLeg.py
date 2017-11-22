from base_parts import Leg


class RightLeg(Leg):

    __size = None

    def __init__(self, size):
        RightLeg.__size = size

    def size(self):
        return RightLeg.__size()