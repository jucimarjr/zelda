from contact_list_proxy import contact_list_proxy
from company import company

def main():
	contact_list = contact_list_proxy()
	_company = company('ABC Company', 'India', '+91-011-28458965', contact_list)

	print('Company Address: ' + _company.get_company_address())
	print('Company Contact No.: ' + _company.get_company_contact_no())

	print('Requesting for contact list')

	contact_list = _company.get_contact_list()

	emp_list = ()
	emp_list = contact_list.get_employee_list()

	for emp in emp_list:
		print(emp.to_string())

if __name__ == '__main__':
	main()