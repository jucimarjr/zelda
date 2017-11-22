from base_parts import Arm


class RightArm(Arm):

    __size = None

    def __init__(self, size):
        RightArm.__size = size

    def size(self):
        return RightArm.__size()