# Modifying Attribute Values


class Car():
	"""A simple attempt to respresent a car."""

	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		"""
		Set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	
	# Incrementing an Attribute’s Value Through a Method
	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles
# The __init__() Method for a Child Class
class ElectricCar(Car):
	"""/Resporesent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""
		Initialize attriubutes of the parent class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(make, model, year)
		# add a new attribute
		self.battery_size = 70

	# Defining Attributes and Methods for the Child Class
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesls', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()



