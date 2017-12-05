from gumballMachine import *

global state, count, SOLD_OUT, NO_QUARTER, HAS_QUARTER, SOLD, WINNER_STATE
gumball_machine = gumballMachine(5)
print (gumball_machine.__str__())

gumball_machine.insertQuarter()
gumball_machine.turnCrank()
print (gumball_machine.__str__())

gumball_machine.insertQuarter()
gumball_machine.ejectQuarter()
gumball_machine.turnCrank()
print (gumball_machine.__str__())

gumball_machine.insertQuarter()
gumball_machine.turnCrank()
gumball_machine.insertQuarter()
gumball_machine.turnCrank()
gumball_machine.ejectQuarter()
print (gumball_machine.__str__())

gumball_machine.insertQuarter()
gumball_machine.insertQuarter()
gumball_machine.turnCrank()
gumball_machine.insertQuarter()
gumball_machine.turnCrank()
gumball_machine.insertQuarter()
gumball_machine.turnCrank()
print (gumball_machine.__str__())