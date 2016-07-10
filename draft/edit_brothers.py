import json

path_to_brothers = ""
brothers_json_file = "brothers.json"

class Brother:
	"""
	Class to validate and keep track of fields for each brother
	"""
	Brother.fields = {
		'name' : ['not_none', 'as_str'],
		'year' : ['not_none', 'as_str'],
		'photo': ['as_str']
		'major' : ['as_str'],
		# 'hometown' : ['as_str'],
		# 'big' : ['as_str'], 
		# 'littles' : ['as_list'], 
		# 'sports' : ['as_list'], 
		# 'description' : ['as_str'], 
		# 'organizations' : ['as_list']
	}

	def __init__(self, **kwargs):
		self.values = dict(kwargs)

		## if not provided set none
		fields = list(Brother.fields.keys())
		for field, value in kwargs:
			if field in field:
				fields.remove(field)

		for field in fields:
			self.values[field] = None

	def validate(self):
		try:
			for field in Brother.fields:
				for validation in Brother.fields[field]:
					getattr(self, validation)(field)
			return True
		except:
			return False
		

	def as_str(self, field):
		assert self.values[field] is None or type(self.values['name']) in [str, int]
		if self.values[field] is not None:
			self.values[field] = str(self.values[field])

	def not_none(self, field):
		assert self.values[field] is not None
		
	def as_year(self, field):
		assert self.values[field] is None or type(self.values[field]) in [str, tuple, list]
		self.values['year'] = str(self.values['year'])
		if len(self.values['year']) == 2:
			self.values['year'] = "20" + self.values['year']

	def as_list(self, field):
		assert self.values[field] is None or type(self.values[field]) in [str, tuple, list]
		if type(self.values[field]) == str:
			self.values[field] = [self.values[field]]
		elif self.values[field] is not None:
			self.values[field] = list(self.values[field])


def create_brothers_file():
	with open(path_to_brothers + brothers_json_file, 'w') as f:
	    data = {}
	    json.dump(data, f, indent=4)

def add_brother():
	kerb = raw_input("Kerberos: ")
	name = raw_input("Name: ")
			
	with open(path_to_brothers + brothers_json_file, 'w') as f:
	    data = {}
	    json.dump(data, f, indent=4)

def edit_brother():


def delete_brother():

def main():
	quit = False
	while not quit:
		i = 0
		while i not in ['1', '2', '3', '4']:
			print "Options:"
			print "1. Add brother"
			print "2. Edit brother"
			print "3. Delete brother"
			print "4. Quit"
			i = raw_input("Select an option (1-4)")
			print 
		i = int(i)
		if i == 1: # add brother
			print "ADD BROTHER:"
			add_brother()
		elif i == 2: # edit brother
			pass
		elif i == 3: # delete brother
			pass

def read_brothers():
	pass





