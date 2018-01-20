prompt = "How old are you?"
prompt += "\nEnter 'quit' when you finished. "

while True:
	age = input(prompt)
	if age =='quit':
		break
	age = int(age)

	if age < 3:
		print("The ticket is free.")
	elif age < 13:
		print("Ticket is $10.")
	else:
		print("Ticket is $15.")