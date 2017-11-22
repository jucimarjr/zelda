import abc

class Subject:

    def __init__(self):
        self._observers = set()
        self._subject_state = None

    def attach(self, observer):
        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        observer._subject = None
        self._observers.discard(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update(self._subject_state)

    @property
    def subject_state(self):
        return self._subject_state

    @subject_state.setter
    def subject_state(self, arg):
        self._subject_state = arg
        self._notify()


class Observer(metaclass=abc.ABCMeta):
    def __init__(self):
        self._subject = None
        self._observer_state = None

    @abc.abstractmethod
    def update(self, arg):
        pass


class ConcreteObserver(Observer):
    def update(self, arg):
        self._observer_state = arg

def main():
    subject1 = Subject()
    subject2 = Subject()
    concrete_observer = ConcreteObserver()
    subject1.attach(concrete_observer)
    subject1.subject_state = 123
    subject2.attach(concrete_observer)
    subject2.subject_state = 456



if __name__ == "__main__":
    main()