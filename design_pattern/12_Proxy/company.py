class company:
	_company_name = ''
	_company_address = ''
	_company_contact_no = ''
	_contact_list = None

	def __init__(self, company_name, company_address, company_contact_no, contact_list):
		self._company_name = company_name
		self._company_address = company_address
		self._company_contact_no = company_contact_no
		self._contact_list = contact_list

	def get_company_name(self):
		return self._company_name
	def get_company_address(self):
		return self._company_address
	def get_company_contact_no(self):
		return self._company_contact_no
	def get_contact_list(self):
		return self._contact_list
