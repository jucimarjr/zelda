from gumball_machine import gumball_machine
from gumball_monitor import gumball_monitor
from random import randint
count = randint(0,10)

if count == 0:
	exit()
gumball_machine = gumball_machine(' ',count)
monitor = gumball_monitor(gumball_machine)
		
print(gumball_machine.__str__())
gumball_machine.insert_quarter()
gumball_machine.turn_crank()
gumball_machine.insert_quarter()
gumball_machine.turn_crank()
print('\n' + gumball_machine.__str__())
gumball_machine.insert_quarter()
gumball_machine.turn_crank()
gumball_machine.insert_quarter()
gumball_machine.turn_crank()

print('\n' + gumball_machine.__str__())
gumball_machine.insert_quarter()
gumball_machine.turn_crank()
gumball_machine.insert_quarter()
gumball_machine.turn_crank()

print('\n' + gumball_machine.__str__())
gumball_machine.insert_quarter()
gumball_machine.turn_crank()
gumball_machine.insert_quarter()
gumball_machine.turn_crank()

print('\n' + gumball_machine.__str__())
gumball_machine.insert_quarter()
gumball_machine.turn_crank()
gumball_machine.insert_quarter()
gumball_machine.turn_crank()

print('\n' + gumball_machine.__str__())

print('\n')
monitor.report()