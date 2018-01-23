def describe_city(city, country = 'china'):
	"""Describe a city."""
	print(city.title() + " is in " + country.title())

describe_city('shanghai')
describe_city('beijing')
describe_city('tokyo', 'japan')
