from State import State

class SoldStates(State):

    def __init__(self, gumball_machine):
        self.__gumball_machine = gumball_machine

    def insert_quarter(self):
        print("Please wait, we're already giving you a gumball")

    def eject_quarter(self):
        print("Sorry, you already turned to crank")

    def turn_crank(self):
        print("Turning twice doesn't get you another gumball")

    def dispense(self):
        self.__gumball_machine.release_ball()
        if self.__gumball_machine.get_count() > 0:
            self.__gumball_machine.set_state(self.__gumball_machine.get_no_quarter_state())

        else:
            print("Oops, out of gumballs")
            self.__gumball_machine.set_state(self.__gumball_machine.get_sold_state())

    def __str__(self):
        return "Dispensing a gumball"
