import copy
from human import Human


class PrototypeHuman:

    __human = None

    def __init__(self):
        PrototypeHuman.__human = Human(head=0.0, spine=0.0, right_arm=0.0, left_arm=0.0, right_leg=0.0, left_leg=0.0)

    def clone(self):
        return copy.deepcopy(PrototypeHuman.__human)