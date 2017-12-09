class employee:
	_employee_name = ''
	_employee_salary = 0.0
	_employee_designation = ''

	def __init__(self, employee_name, employee_salary, employee_designation):
		self._employee_name = employee_name
		self._employee_salary = employee_salary
		self._employee_designation = employee_designation

	def get_employee_name(self):
		return self._employee_name
	def get_employee_salary(self):
		return self._employee_salary
	def get_employee_designation(self):
		return self._employee_designation
	def to_string(self):
		return 'Employee Name: ' + self._employee_name + ', Employee Designation: ' + self._employee_designation + ', Employee Salary: ' + str(self._employee_salary)
		