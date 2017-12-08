from random import randint
import abc
from state import state

class has_quarter_state(state):
 
  gumball_machine = None
 
  def __init__(self, gumball_machine):
    self.gumball_machine = gumball_machine
   
  def insert_quarter(self):
    print('Você não pode inserir outro moeda')
  def eject_quarter(self):
    print('A moeda retornou')
    self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())
  def turn_crank(self):
    print('Voce girou...')
    winner = randint(0,5)
    print(winner)
    if winner == 0:
      self.gumball_machine.set_state(self.gumball_machine.get_winner_state())
    else:
      self.gumball_machine.set_state(self.gumball_machine.get_sold_state())
 
  def dispense(self):
    print('Sem goma')
  def toString(self):
    return 'Esperando por um giro na manivela'