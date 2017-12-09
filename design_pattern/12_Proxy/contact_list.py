import abc

class contact_list(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def get_employee_list(self):
		pass