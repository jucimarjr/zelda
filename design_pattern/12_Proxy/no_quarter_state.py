from random import randint
import abc
from state import state

class no_quarter_state(state):
 
  gumball_machine = None
 
  def __init__(self, gumball_machine):
    self.gumball_machine = gumball_machine
   
  def insert_quarter(self):
    print('voce inseriu uma moeda')
    self.gumball_machine.set_state(self.gumball_machine.get_has_quarter_state())
  def eject_quarter(self):
    print('Voce nao inseriu a moeda')
   
  def turn_crank(self):
    print('voce girou, mas nao tem nenhuma moeda')
 
  def dispense(self):
    print('Voce precisa primeiro pagar')
  def toString(self):
    return 'Esperando a moeda'