def city_country(city, country):
	"""Return  a string like this 'Santiago, Chile'."""
	return(city.title() + ", " + country.title())

city = city_country('shanghai', 'china')
print(city)

city = city_country('beijing', 'china')
print(city)

city = city_country('tokyo', 'japan')
print(city)