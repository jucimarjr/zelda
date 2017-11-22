from base_parts import Arm


class LeftArm(Arm):

    __size = None

    def __init__(self, size):
        LeftArm.__size = size

    def size(self):
        return LeftArm.__size()