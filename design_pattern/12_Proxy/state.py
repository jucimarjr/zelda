import abc

class state(metaclass = abc.ABCMeta):
 
  @abc.abstractmethod
  def insert_quarter(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def eject_quarter(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def turn_crank(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def dispense(self):
    raise NotImplementedError()