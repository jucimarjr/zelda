from extended_parts import LeftArm, RightArm, LeftLeg, RightLeg
from base_parts import Head, Spine


class Human:
    
    __head = None
    __spine = None
    __right_arm = None
    __left_arm = None
    __right_leg = None
    __left_leg = None

    def __init__(self, head, spine, right_arm, left_arm, right_leg, left_leg):
        Human.__head = Head(head)
        Human.__spine = Spine(spine)
        Human.__right_arm = RightArm(right_arm)
        Human.__left_arm = LeftArm(left_arm)
        Human.__right_leg = RightLeg(right_leg)
        Human.__left_leg = LeftLeg(left_leg)

    def size_head(self):
        return Human.__head.size()

    def size_spine(self):
        return Human.__spine.size()

    def size_right_arm(self):
        return Human.__right_arm.size()
    
    def size_left_arm(self):
        return Human.__left_arm.size()

    def size_right_leg(self):
        return Human.__right_leg.size()
    
    def size_left_arm(self):
        return Human.__left_arm.size()
