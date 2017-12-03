from State import State

class NoQuarterState(State):

    def __init__(self, gumball_machine):
        self.__gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You inserted a quarter")
        self.__gumball_machine.set_state(self.__gumball_machine.get_has_quarter_state())

    def eject_quarter(self):
        print("You haven't inserted a quarter")

    def turn_crank(self):
        print("You turned, but there's no quarter")

    def dispense(self):
        print("You need to pay first")

    def __str__(self):
        return "Waiting for quarter"
