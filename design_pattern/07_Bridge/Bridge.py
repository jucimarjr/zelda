from ConcreteRemote import *
from RemoteControl import *
from RCA import *

def main():
    control = RCA()
    concrete = ConcreteRemote(RCA)
    abstraction = RemoteControl(concrete)
    abstraction.on()
    control.tune_channel(5)

if __name__ == "__main__":
    main()
