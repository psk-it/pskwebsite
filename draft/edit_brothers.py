import json
import pandas as pd
import datetime

path_to_brothers = ""
brothers_json_file = "brothers.json"

def load():
	with open(path_to_brothers + brothers_json_file, 'r') as f:
		data = json.load(f)
	return pd.DataFrame(data)

def save(data):
	data[['year', 'pledge no']] = data[['year', 'pledge no']].astype(int)
	data = data.sort_values(by = ['year', 'pledge no'], ascending=[True, True])
	data = add_class_labels(data)
	data.to_json(path_to_brothers + brothers_json_file, orient="records")

def add_bro():
	data = load()
	cols = ['name', 'year', 'major', 'hometown','pledge no',
			'picture', 'year matches graduation']
	new_bro = dict()
	for c in cols:
		inp = raw_input(c.capitalize() + ": ")
		inp = parse_value(c, inp)
		new_bro[c] = inp
	data = data.append(new_bro, ignore_index = True)
	save(data)

def parse_value(col, value):
	if value == "":
		value = None
	elif col in ['year', 'pledge no']:
		value = int(value)
	elif col in ['year matches graduation']:
		value = value.lower() in ['y', 'yes', 'true']
	return value

def search_select(names):
	inp = "***"
	while inp != "":
		for n in names:
			print "\t", n
		names_lower = names.apply(lambda x: x.lower()).values
		inp = raw_input("Select a brother: ").lower()
		where_still = pd.Series(names_lower).apply(lambda n: inp in n)
		n_left = where_still.sum()
		print n_left
		if n_left == 0:
			print "No options contain '%s'." % inp
		elif n_left >= 1:
			if n_left == 1:
				print names
				print where_still
				name = names[where_still.values].iloc[0]
				break
			else:
				names = names[where_still.values].copy()
				print names
				print "%s options left:" % n_left
	if inp == "":
		return inp
	else:
		return name

def edit_bro():
	data = load()
	include_former_bros = raw_input("Include former bros? ").lower() in ['y', 'yes', 'true']
	if include_former_bros:
		names = data['name']
	else:
		names = data[data['in school'].astype(bool)]['name']
	print "Availible Bros:"
	if len(names) > 0:
		inp = search_select(names)
		print inp
		if inp != "":
			name = inp
			where_bro = data['name'] == name
			if inp != "":
				inp = "***"
				while inp != "":
					bro = data[where_bro]
					print "\nSelected Brother:\n", bro.transpose()
					print
					inp = raw_input("Select column to modify: ")
					if inp in bro:
						val = raw_input("New value: ")
						if val != "":
							data[inp][where_bro] = parse_value(inp, val)
						else:
							print "Update aborted."
					elif inp != "":
						print "Invalid column input."
				save(data)
			else:
				print "Edit aborted."
	else:
		print "No availible brothers."

def delete_bro():
	data = load()
	inp = search_select(data['name'])
	print inp
	bro = data[data['name'] == inp]

	if inp != "":
		print "\nSelected Brother:\n", bro.replace("\n", "\t\n")

		sure = raw_input("Are you sure you want to delete?").lower()
		if sure in ['y', 'yes', 'true']:
			data = data[data['name'] != inp]
			save(data)
		else:
			print "Delete aborted."

def view_bros():
	print load()
	print 
	

def get_class_mapping():
	now = datetime.datetime.now()
	seniors = now.year
	if now.month >= 8:
		seniors += 1
	return {
		seniors : 'Senior',
		seniors + 1 : 'Junior',
		seniors + 2 : 'Sophomore',
		seniors + 3 : 'Freshman'
	}

def add_class_labels(data):
	if "year matches graduation" not in data:
		data['year matches graduation'] = True
	class_mapping = get_class_mapping()
	classes = data['year'].map(class_mapping)
	data.loc[data['year matches graduation'], 'class'] = classes[data['year matches graduation']]
	data.loc[data['year matches graduation'], 'in school'] = data['year'].isin(class_mapping)
	return data

def main():
	inp = "**"
	while inp != "q":
		print "Options:"
		print "1. Add brother"
		print "2. Edit brother"
		print "3. Delete brother"
		print "4. View data"
		print "Q. Quit"
		inp = raw_input("Select option (Q to quit): ").lower()
		if inp == "1":
			add_bro()
		elif inp == "2":
			edit_bro()
		elif inp == "3":
			delete_bro()
		elif inp == "4":
			view_bros()
	print "Goodbye!"

if __name__ == "__main__":
	main()




