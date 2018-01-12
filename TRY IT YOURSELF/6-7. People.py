# Make an empty list to store people in.
people = []

# Define people and add them to the list.
person = {
	'first_name': 'jimmy',
	'last_name': 'chen',
	'age': 23,
	'city': 'shanghai'
	}
people.append(person)

person = {
	'first_name': 'neal',
	'last_name': 'sun',
	'age': 26,
	'city': 'shanghai'
	}
people.append(person)

person = {
	'first_name': 'anna',
	'last_name': 'shen',
	'age': 27,
	'city': 'shanghai'
	}
people.append(person)

for person in people:
	name = person['first_name'].title() + " " + person['last_name'].title()
	age = str(person['age'])
	city = person['city'].title()

	print(name + ", " + city + ", is " + age + " years old.")