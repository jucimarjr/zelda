from inventory_visitor import InventoryVisitor
from pricing_visitor import PricingVisitor
from floppy_disk import FloppyDisk
from chassis import Chassis

chassi = Chassis("Chassi1",9,10,20)
floppy = FloppyDisk("FloppyDisk1",2,4,6)

pricingVis = PricingVisitor()
inventoryVis = InventoryVisitor()

chassi.Accept(pricingVis)
chassi.Accept(inventoryVis)

floppy.Accept(pricingVis)
floppy.Accept(inventoryVis)
