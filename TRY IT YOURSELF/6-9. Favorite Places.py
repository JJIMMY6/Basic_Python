favorite_places = {
	'jimmy': ['shanghai', 'united states', 'canada'],
	'neal': ['united states', 'thailand', 'shanghai'],
	'anna': ['thailand', 'shanghai', 'japan']
	}

for name, places in favorite_places.items():
	print("\n" + name.title() + " likes these places:")
	for place in places:
		print(place.title())