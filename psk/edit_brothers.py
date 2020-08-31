from __future__ import print_function
import json
import pandas as pd
import datetime
import time
import pdb

from urllib.request import Request, urlopen, URLError

# Load API key for Google API
key_file = "secrets.json"
with open(key_file, 'r', encoding='utf-8') as f:
    key_json = json.load(f)

def help_info():
    message = (
        """
        Hello IT Chair! Run "python edit_brothers.py "to use this
        program. From there, here are some of the less intuitive
        points:

        1. The year matches graduation can be used to keep a brother
           on an extra year. Most of the time, this will be true,
           but if you have a sophomore rush or 5th year senior,
           this option gives you flexibility.

        2. Sports, internships, courses, clubs. These columns exist
           for possible future projects where you might want to use
           D3 or some other javascript package to make interactive
           stuff. Might not be a good idea. Either way, entering the
           input like "[Goldman Sachs], [Tesla]" will be parsed into
           a list "['Goldman Sachs', 'Tesla']"

        3. "Hometown ??? was unsuccessfully queried." This program
           automatically queries Google for long-lat coords and
           other info about people's hometowns to put into a map
           visualization. If you get this, it means either Google
           could not find that hometown, or you have made too many
           requests.

        4. All past brother info is saved, and every June running
           the "update years" command re-saves the data, and moves
           Juniors to Seniors, Soph to Jr and so on.

        5. To do anything beyond the command line interface is not
           hard, you just have to manipulate the underlying Pandas
           dataframe. For example, if you want a new column, you
           just add it to the dataframe, and add that column into
           the logic of the add_bro() and parse_value() functions.
        """ )
    print(message)

def query_location(where):
    formatted = "+".join(where.split(" "))
    query = "https://maps.googleapis.com/maps/api/geocode/json?address=" + formatted + "&sensor=false&key={}".format(key_json["google_api"])
    # print(query)
    request = Request(query)
    try:
        response = urlopen(request)
        data = eval(response.read())['results'][0]
        lat_lng = data['geometry']['location']
        full_address_short_long = [(d['types'][0], d['short_name'], d['long_name']) for d in data['address_components']]
        full_address_short_long.reverse()
        address_type, full_address_short, full_address_long = zip(*full_address_short_long)
        value_dict = dict([(x[0], x[1:]) for x in full_address_short_long])
        if value_dict['country'][0] == 'US':
            use_values = ['country','administrative_area_level_1', 'locality']
        elif 'locality' in value_dict:
            use_values = ['country', 'locality']
        else:
            use_values = ['country']
        try:
            full_address_short = ".".join([value_dict[x][0] for x in use_values])
            full_address_long = ".".join([value_dict[x][1] for x in use_values])
        except:
            full_address_short = None
            full_address_short = None
        return (lat_lng['lat'], lat_lng['lng']), full_address_long, full_address_short, data
    except URLError as e:
        print('No kittez. Got an error code:', e)

path_to_brothers = "data/"
brothers_json_file = "brothers.json"

def load():
    with open(path_to_brothers + brothers_json_file, 'r') as f:
        data = json.load(f)
    return pd.DataFrame(data)

def save(data, fileName = brothers_json_file):
    data[['year', 'pledge no']] = data[['year', 'pledge no']].astype(int)
    data = data.sort_values(by = ['year', 'pledge no'], ascending=[True, True])
    data = add_class_labels(data)
    data = validate_locations(data)
    data.to_json(path_to_brothers + fileName, orient="records")

def add_bro():
    data = load()
    cols = ['name', 'year', 'major', 'hometown','pledge no',
            'picture', 'year matches graduation', 'blurb', 'sports', 'internships', 'courses', 'clubs']
    new_bro = dict()
    for c in cols:
        inp = input(c.capitalize() + ": ")
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
    elif col in ['sports', 'internships', 'courses', 'clubs']:
        print(value)
        value = str(value)
        if not value.startswith("["):
            value = '[' + value
        if not value.endswith("]"):
            value = value + ']'
        print(value)
        value = eval(value)
        print(value)
        value = [str(v) for v in value]
    return value

def validate_locations(data):
    lon_lats = []
    long_names = []
    short_names = []
    for index in data.index:
        town = data['hometown'][index]
        lon_lat = data['coords'][index]
        long_name = data['hometown_long'][index]
        short_name = data['hometown_short'][index]
        if lon_lat is None or long_name is None or short_name is None:
            try:
                lon_lat, long_name, short_name, full = query_location(town)
                success = True
            except:
                print("Hometown %s was unsuccessfully queried" % town)
        lon_lats += [lon_lat]
        long_names += [long_name]
        short_names += [short_name]

    data['coords'] = lon_lats
    data['hometown_long'] = long_names
    data['hometown_short'] = short_names
    return data


def search_select(names):
    inp = "***"
    while inp != "":
        for n in names:
            print("\t", n)
        names_lower = names.apply(lambda x: x.lower()).values
        inp = input("Select a brother: ").lower()
        where_still = pd.Series(names_lower).apply(lambda n: inp == n)
        n_left = where_still.sum()
        print(n_left)
        if n_left == 0:
            print("No options contain '%s'." % inp)
        elif n_left >= 1:
            if n_left == 1:
                print(names)
                print(where_still)
                name = names[where_still.values].iloc[0]
                break
            else:
                names = names[where_still.values].copy()
                print(names)
                print("%s options left:" % n_left)
    if inp == "":
        return inp
    else:
        return name

def edit_bro():
    data = load()
    include_former_bros = input("Include former bros? ").lower() in ['y', 'yes', 'true']
    if include_former_bros:
        names = data['name']
    else:
        names = data[data['in school'].astype(bool)]['name']
    print("Availible Bros:")
    if len(names) > 0:
        inp = search_select(names)
        print(inp)
        if inp != "":
            name = inp
            where_bro = data['name'] == name
            if inp != "":
                inp = "***"
                while inp != "":
                    bro = data[where_bro]
                    print("\nSelected Brother:\n", bro.transpose())
                    print()
                    inp = input("Select column to modify: ")
                    if inp in bro:
                        try_again = True
                        while try_again:
                            try_again = False
                            print ("Old value: %s" % data[where_bro][inp].iloc[0])
                            val = input("New value: ")
                            print("Val: ", val)
                            if val != "":
                                try:
                                    index = data[where_bro].index[0]
                                    print(index, inp, val)
                                    print(parse_value(inp, val))
                                    print("Parse works")
                                    data.at[index, inp] = parse_value(inp, val)
                                except Exception as e:
                                    print(e)
                                    print("Parsing failed. Try again.")
                                    try_again = True
                            else:
                                print("Update aborted.")
                    elif inp != "":
                        print("Invalid column input.")
                save(data)
            else:
                print("Edit aborted.")
    else:
        print("No availible brothers.")

def delete_bro():
    data = load()
    inp = search_select(data['name'])
    print(inp)
    bro = data[data['name'] == inp]

    if inp != "":
        print("\nSelected Brother:\n", bro.replace("\n", "\t\n"))

        sure = input("Are you sure you want to delete?").lower()
        if sure in ['y', 'yes', 'true']:
            data = data[data['name'] != inp]
            save(data)
        else:
            print("Delete aborted.")



def view_bros():
    print(load())
    print()


def get_class_mapping():
    now = datetime.datetime.now()
    seniors = now.year
    # New class year update starts after June
    if now.month >= 6:
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
        print("Options:")
        print("1. Add brother")
        print("2. Edit brother")
        print("3. Delete brother")
        print("4. View data")
        print("5. Update years")
        print("6. Help")
        print("Q. Quit")
        inp = input("Select option (Q to quit): ").lower()
        if inp == "1":
            add_bro()
        elif inp == "2":
            edit_bro()
        elif inp == "3":
            delete_bro()
        elif inp == "4":
            view_bros()
        elif inp == "5":
            save(load()) # the updating happens in the save function
        elif inp == "6":
            help_info()

    print("Goodbye!")

if __name__ == "__main__":
    main()




