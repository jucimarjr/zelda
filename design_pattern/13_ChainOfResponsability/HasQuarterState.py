
from State import State

class HasQuarterState(State):

    def __init__(self, gumball_machine):
        self.__gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You can't insert another quarter")

    def eject_quarter(self):
        print("Quarter returned")
        self.__gumball_machine.set_state(self.__gumball_machine.get_no_quarter_state())

    def turn_crank(self):
        print("You turned")
        self.__gumball_machine.set_state(self.__gumball_machine.get_sold_state())

    def dispense(self):
        print("No gumball dispensed")

    def __str__(self):
        return "Waiting for turn of the crank"
