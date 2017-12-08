from gumball_machine import gumball_machine

class gumball_monitor:
  machine = None
 
  def __init__(self, machine):
    self.machine = machine
 
  def report(self):
    print('Gumball Machine: ' + self.machine.get_location())
    print('Current inventory: ' + str(self.machine.get_count()) + ' gumballs')
    print('Current state: ' + str(self.machine.get_state()))