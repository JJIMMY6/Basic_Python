# Make an empty list.
pets = []

# Make owner's pets and store in the list.
pet = {
	'kind of animal': 'dog',
	'owner': 'jimmy'
	}
pets.append(pet)

pet = {
	'kind of animal': 'cat',
	'owner': 'neal'
	}
pets.append(pet)

pet = {
	'kind of animal': 'bird',
	'owner': 'anna'
	}
pets.append(pet)

for pet in pets:
	print(pet['owner'].title() + " has a " + pet['kind of animal'] + ".")