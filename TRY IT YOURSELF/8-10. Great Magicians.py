def show_magicians(magicians):
	"""Print the name of each magician in the list."""
	for magician in magicians:
		print(magician.title())

def add_great(magicians):
	for great_magician in range(len(magicians)):
		magicians[great_magician] += " the Great"

magicians = ['david copperfield', 'criss angel']

add_great(magicians)
show_magicians(magicians)

