class Spine:

    __size = None

    def __init__(self, size):
        Spine.__size = size

    def size(self):
        return Spine.__size