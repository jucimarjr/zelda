from contact_list import contact_list
from employee import employee

class contact_list_real(contact_list):
	_obj = None
	def get_employee_list(self):
		return self.get_emp_list()

	def get_emp_list(self):
		emp_list = [employee('Employee A', 2565.55, 'SE'), employee('Employee B', 22574, 'Manager'), employee('Employee C', 3256.77, 'SSE'), employee('Employee D', 4875.54, 'SSE'), employee('Employee E', 2847.01, 'SE')]
		return emp_list