import abc

class AbstractBuilder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def build_day():
        pass

    @abc.abstractmethod
    def add_hotel(date, name):
        pass
    
    @abc.abstractmethod
    def add_reservation(date, name):
        pass

    @abc.abstractmethod
    def add_special_event(date, name):
        pass

    @abc.abstractmethod
    def add_tickets(date, name):
        pass

    @abc.abstractmethod
    def get_vacation_planner():
        pass
