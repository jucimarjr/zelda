from state import state

class winner_state(state):
 
  gumball_machine = None
 
  def __init__(self, gumball_machine):
    self.gumball_machine = gumball_machine
  
  def insert_quarter(self):
    print('Aguarde, nós ja estamos lhe dando uma goma')
  def eject_quarter(self):
    print('Aguarde, nós ja estamos lhe dando uma goma')
  def turn_crank(self):
    print('Gire novamento')
  def dispense(self):
    print('VOCE VENCEU! Tome duas gomas pela sua moeda')
    try:
      self.gumball_machine.release_ball(self)
      if self.gumball_machine.get_count(self) == 0:
        self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state(self))
      else:
        if self.gumball_machine.get_count(self) > 0:
          self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state(self))
        else:
          print('Oops, out of gumballs!')
          self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state(self))
    except:
      print('ERROR!')
  def to_string(self):
    return 'despensing two gumballs for your quarter, because YOU\'RE A WINNER!'