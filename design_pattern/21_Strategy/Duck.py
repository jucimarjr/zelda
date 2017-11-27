import abc

class Duck(metaclass=abc.ABCMeta):
    __fly_behavior = 0
    __quack_behavior = 0

    @abc.abstractmethod
    def set_fly_behavior(self, fb):
        self.__fly_behavior=fb

    @abc.abstractmethod
    def set_quack_behavior(self, qb):
        sefl.__quack_behavior=qb

    @abc.abstractmethod
    def perform_fly(self):
        self.__fly_behavior.fly()

    @abc.abstractmethod
    def perform_quack(self):
        self.__quack_behavior.fly()

    @abc.abstractmethod
    def swim(self):
        print("All ducks float, even decoys!")

    @abc.abstractmethod
    def display():
        pass
