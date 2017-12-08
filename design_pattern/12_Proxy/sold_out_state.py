from state import state

class sold_out_state(state):
 
  gumball_machine = None
 
  def __init__(self, gumball_machine):
    self.gumball_machine = gumball_machine
 
  def insert_quarter(self):
    print('Você não pode inserir um quarto, a máquina está esgotada')
  def eject_quarter(self):
    print('Você não pode ejetar, você ainda não inseriu um quarto ainda')
  def turn_crank(self):
    print('Você virou, mas não há gomas')
  def dispense(self):
    print('No gumball dispensed')
  def to_string(self):
    return 'sold out'