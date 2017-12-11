
from GumballMachine import GumballMachine

if __name__ == '__main__':
    GUMBALL_MACHINE = GumballMachine(5)

    print(GUMBALL_MACHINE)
    GUMBALL_MACHINE.insert_quarter()
    GUMBALL_MACHINE.turn_crank()

    print(GUMBALL_MACHINE)

    GUMBALL_MACHINE.turn_crank()
    GUMBALL_MACHINE.insert_quarter()
    GUMBALL_MACHINE.turn_crank()

    print(GUMBALL_MACHINE)
