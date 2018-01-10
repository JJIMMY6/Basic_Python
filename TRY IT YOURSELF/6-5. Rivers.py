rivers = {
	'nile': 'egypt',
	'yangtze': 'China',
	'saint lawrence': 'Canada',
	'mississippi': 'United States'
	}

for river, countary in rivers.items():
	print("The " + river.title() + " runs through " + countary.title() + ".")

print("\nThe name of each river:")
for river in rivers.keys():
	print(river.title())

print("\nThe countary of each river:")
for countary in rivers.values():
	print(countary.title())