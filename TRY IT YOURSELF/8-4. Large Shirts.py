def make_shirt(size = 'large', message = 'I love Python!'):
	"""Summarize the shirt."""
	print("\nI'm going to make " + size + " t-shirt.")
	print('It will say, "' + message + '"')

make_shirt()
make_shirt(size = 'medium')
make_shirt(size = 'small', message = 'use python.')