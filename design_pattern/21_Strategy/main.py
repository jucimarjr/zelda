from mallard_duck import MallardDuck
from model_duck import ModelDuck
from redhead_duck import RedHeadDuck
from rubber_duck import RubberDuck
from decoy_duck import DecoyDuck
from fly_rocket_powered import FlyRocketPowered

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
