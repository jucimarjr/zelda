from equipment_visitor import EquipmentVisitor

class PricingVisitor(EquipmentVisitor):
    def __init__(self):
        self._total = 0;

    def GetTotalPrice(self):
        return self._total

    def visitFloppyDisk(self,FloppyDisk):
        _total += FloppyDisk.NetPrice()

    def visitChassis(self,Chassis):
        _total += Chassis.DiscountPrice()
