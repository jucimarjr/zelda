import abc

class Duck(metaclass=abc.ABCMeta):
    __fly_behavior = 0
    __quack_behavior = 0

    def set_fly_behavior(self, fb):
        self.__fly_behavior=fb

    def set_quack_behavior(self, qb):
        self.__quack_behavior=qb

    def perform_fly(self):
        self.__fly_behavior.fly()

    def perform_quack(self):
        self.__quack_behavior.quack()

    def swim(self):
        print("All ducks float, even decoys!")

    def display():
        pass
