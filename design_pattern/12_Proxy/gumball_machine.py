from sold_state import sold_state
from sold_out_state import sold_out_state
from has_quarter_state import has_quarter_state
from no_quarter_state import no_quarter_state
from winner_state import winner_state
from state import state
class gumball_machine:
  _sold_out_state = None
  _no_quarter_state = None
  _has_quarter_state = None
  _sold_state = None
  _winner_state = None

  _state = _sold_out_state
  location = ''
 
  def __init__(self, location, count):
    self._sold_out_state = sold_out_state(self)
    self._no_quarter_state = no_quarter_state(self)
    self._has_quarter_state = has_quarter_state(self)
    self._sold_state = sold_state(self)
    self._winner_state = winner_state(self)

    self.count = count
    if self.count > 0:
      self._state = self._no_quarter_state
    self.location = location

  def insert_quarter(self):
    self._state.insert_quarter()
  
  def eject_quarter(self):
    self._state.eject_quarter()
  
  def turn_crank(self):
    self._state.turn_crank()
    self._state.dispense()
  
  def set_state(self, state):
    self._state = state
  
  def release_ball(self):
    print('Uma goma esta vindo...')
    if self.count != 0:
      self.count -= 1
 
  def get_count(self):
    return self.count
  
  def refill(self, count):
    self.count = count
    self._state = self._no_quarter_state
  
  def get_state(self):
    return self._state
  
  def get_location(self):
    return self.location
  
  def get_sold_out_state(self):
    return self._sold_out_state
  
  def get_no_quarter_state(self):
    return self._no_quarter_state
  
  def get_has_quarter_state(self):
    return self._has_quarter_state
  
  def get_sold_state(self):
    return self._sold_state
  
  def get_winner_state(self):
    return self._winner_state
  
  def to_string(self):
    result = ''
    result += '\nMighty Gumball, Inc.'
    result += '\nPython-enabled Standing Gumball Model #2017'
    result += '\nInventory: ' + str(self.count) + 'gumball'
    if self.count != 1:
      result += 's'
    result += '\n'
    result += 'Machine is ' + str(self.state) + '\n'
    return result