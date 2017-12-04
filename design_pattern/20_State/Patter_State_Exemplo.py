import gumballMachine

global state, count, SOLD_OUT, NO_QUARTER, HAS_QUARTER, SOLD
gumball_machine = gumballMachine(5)

gumball_machine.insertQuarter()
gumball_machine.turnCrank()

gumball_machine.insertQuarter()
gumball_machine.ejectQuarter()
gumball_machine.turnCrank()

gumball_machine.insertQuarter()
gumball_machine.turnCrank()
gumball_machine.insertQuarter()
gumball_machine.turnCrank()
gumball_machine.ejectQuarter()

gumball_machine.insertQuarter()
gumball_machine.insertQuarter()
gumball_machine.turnCrank()
gumball_machine.insertQuarter()
gumball_machine.turnCrank()
gumball_machine.insertQuarter()
gumball_machine.turnCrank()