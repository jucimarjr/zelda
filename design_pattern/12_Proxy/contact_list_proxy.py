from contact_list import contact_list
from contact_list_real import contact_list_real

class contact_list_proxy(contact_list):
	_contact_list = None

	def get_employee_list(self):
		if self._contact_list is None:
			print('Creating contact list and fetching list of employees...')
			self._contact_list = contact_list_real()
		return self._contact_list.get_employee_list()