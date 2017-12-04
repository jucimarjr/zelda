from equipment_visitor import EquipmentVisitor

class InventoryVisitor(EquipmentVisitor):
    def __init__(self):
        self._inventory = []

    def visitFloppyDisk(self,FloppyDisk):
        _inventory.append(FloppyDisk)

    def visitChassis(self,Chassis):
        _inventory.append(Chassis)
