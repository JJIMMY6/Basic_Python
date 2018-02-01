class Restaurant():
	"""A class to describe an Restaurant"""

	def __init__(self, name, cuisine_type):
		"""Initialize name and cuisine_type attributes."""
		self.name = name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		""""""
		print(self.name.title() + " provide " + self.cuisine_type.title())

	def open_restaurant(self):
		"""Prints a message that restaurant is open."""
		print(self.name.title() + " is open.")


restaurant = Restaurant('fairmont peace hotel', 'chinese food')
print(restaurant.name.title())
print(restaurant.cuisine_type.title())

restaurant.describe_restaurant()
restaurant.open_restaurant()



	