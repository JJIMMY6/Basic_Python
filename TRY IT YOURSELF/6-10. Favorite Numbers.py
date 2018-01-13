favorite_numbers = {
	'neal': [3, 6, 9],
	'anna': [1, 6, 7],
	'robin': [1, 5, 8]
	}

for name, numbers in favorite_numbers.items():
	print("\n" + name.title() + " likes these numbers:")
	for num in numbers:
		print(str(num))