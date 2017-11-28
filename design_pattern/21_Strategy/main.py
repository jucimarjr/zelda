from MallardDuck import MallardDuck
from ModelDuck import ModelDuck
from RedHeadDuck import RedHeadDuck
from RubberDuck import RubberDuck
from DecoyDuck import DecoyDuck
from FlyRocketPowered import FlyRocketPowered

mallard = MallardDuck()
rubber_duckie = RubberDuck()
decoy = DecoyDuck()

model = ModelDuck()
mallard.perform_quack()
rubber_duckie.perform_quack()
decoy.perform_quack()

model.perform_fly()
model.set_fly_behavior(FlyRocketPowered)
model.perform_fly()
