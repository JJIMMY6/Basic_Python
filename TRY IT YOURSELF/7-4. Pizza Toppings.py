prompt = "\nWhat toppings would you like to add?"
prompt += "\nEnter 'quit' if you are finished: "

while True:
	topping = input(prompt)
	if topping != 'quit':
		print("I will add " + topping + ".")
	else:
		break