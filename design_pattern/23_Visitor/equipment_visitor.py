import abc

class EquipmentVisitor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def visitFloppyDisk(self,FloppyDisk):
        pass

    @abc.abstractmethod
    def visitChassis(self,Chassis):
        pass

