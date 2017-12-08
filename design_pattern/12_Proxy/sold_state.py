from state import state

class sold_state(state):
 
  gumball_machine = None
 
  def __init__(self, gumball_machine):
    self.gumball_machine = gumball_machine
   
  def insert_quarter(self):
    print('Aguarde, nós já estamos lhe dando uma goma')
  def eject_quarter(self):
    print('Desculpe, você já virou a manivela')
  def turn_crank(self):
    print('Virar duas vezes não te leva a outra goma!')
  def dispense(self):
    self.gumball_machine.release_ball()
    try:
      if self.gumball_machine.get_count(self) > 0:
        self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())
      else:
        print('Oops, out of gumballs!')
        self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state())
    except:
      print('ERROR!')
  def to_string(self):
    return 'dispensing a gumball'