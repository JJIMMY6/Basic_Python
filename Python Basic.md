## 5. IF STATEMENTS
### A Simple Example
```python
#The value 'bmw' should be printed in all uppercase
cars = ['adui', 'bmw', 'subaru', 'toyota']

for car in cars:
    if cars == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```

```
Audi
BMW
Subaru
Toyota
```
---
### Ignoring Case When Checking for Equality
```
car = 'Audi'
car.lower() == 'adui'
#The lower() function doesn’t change the value that was originally stored in car
```

`True`

### Checking for Inequality
```python
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")
```

`Hold the anchovies!`

### Checking Multiple Conditions

```python
#Using and to Check Multiple Conditions
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21

age_1 = 22
age_0 >= 21 and age_1 >= 21
```

```
False
True
```
---
```python
#Using or to Check Multiple Conditions
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21

age_0 = 18
age_0 >= 21 or age_1 >= 21
```

```
True
False
```
---
```python
#Checking Whether a Value is in a List
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings

'pepperoni' in requested_toppings
```

```
True
False
```
---
### if Statements
```python
#The if-elif-else Chain
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

```

`Your admission cost is $5.`

---
```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")
```
---

### Using if Statements with Lists
```python
#Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry,we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")
```

```
Adding mushrooms.
Sorry,we don't have french fries.
Adding extra cheese.

Finished making your pizza!
```

## 6. DICTIONARIES
```python 
alien_0 = {'color': 'green', 'points':5}

print(alien_0['color'])
print(alien_0['points'])
```

```
green
5
```
---
```python
#Add New Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
```

```python
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5, 'y_position: 25', 'x_position: 0',}
#Python doesn’t care about the order in which you store each key-value pair; 
#it cares only about the connection between each key and its value.

```
>[Python 3 New dict](https://docs.python.org/3.6/whatsnew/3.6.html#new-dict-implementation)


### Modifying Values in a Dictionary
```python
alien_0 = {'x_position': 0,'y_position': 25, 'speed':, 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':#
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position'])) #I lost parentheses .
```

```
Original x-position: 0
New x-position: 2
```

### Looping Through a Dictionary
```python
# Looping Through All Key-Value Pairs
user_0 = {
    'user_name': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
```

```
Key: user_name
Value: efermi

Key: first
Value: enrico

Key: last
Value: fermi
```
---
```python
# Looping Through All the keys in a Dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")
```

```
Jen
Sarah
 Hi Sarah, I see your favorite language is C!
Edward
Phil
 Hi Phil, I see your favorite language is Python!
```

## Nesting
---
```python
# A list of Dictionaries.
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10        
'''    elif alien ['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
'''

# Show the first 5 aliens:
for alien in aliens[0:5]:
    print(alien)
print("...")
```

```
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
...
```

```python
# A list in a Dictionary.

```


```python
# A Dictionary in Dictionary.
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },

}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
```

```
Username: aeinstein
    Full name: Albert Einstein
    Location: Princeton

Username: mcurie
    Full name: Marie Curie
    Location: Paris
```

## 7. USER INPUT AND WHILE LOOPS
### How the input() Function Works
---
```python
# Writing Clear Prompts
prompt = "If you tell us who you are, we can personalize the messages you see." 
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")
```

```
If you tell us who you are, we can personalize the messages you see.
What is your first name? Eric

Hello, Eric!
```

### Introducing while Loops
---
```python
# The while Loop in Action
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

```
1
2
3
4
5
```

```python
# Letting the User Choose When to Quit
prompt = "\nTell me something, and I will repeat it back to you:" 
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

```

```
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. hello
hello

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
```

```python
# Using break to Exit a Loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

```

```
Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) new york
I'd love to go to New York!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) San Francisco
I'd love to go to San Francisco!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) quit
```

```python
# Using continue in a Loop
# A loop counts from 1 to 10 but prints only the odd numbers.
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

```

```
1
3
5
7
9
```

### Using a while Loop with Lists and Dictionaries
---
```python
# Moving Items frome One list to Another

# Start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

```

```
Verifying user: Candace
Verifying user: Brian
Verifying user: Alice

The following users have been confirmed:
Candace
Brian
Alice
```

```python
# Removing All Instances of Specific Values frome a List
# Remove all instances of that vaule, use a whille loop.
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
```

```
['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
['dog', 'dog', 'goldfish', 'rabbit']
```

```python
# Filling a Dictionary with User Input

responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary:
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

```

```
What is your name? Eric
Which mountain would you like to climb someday? Denali
Would you like to let another person respond? (yes/ no) yes

What is your name? Lynn
Which mountain would you like to climb someday? Devil's Thumb
Would you like to let another person respond? (yes/ no) no

--- Poll Results ---
Eric would like to climb Denali.
Lynn would like to climb Devil's Thumb.
```


## 8. FUNCTIONS
### Defining a Function
---
```python
# Passing Information to Funtion
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('jesse')
```

```
Hello, Jesse!
```

### Passing Arguments
---
```python
# Positional Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')

```

```
I have a hamster.
My hamster's name is Harry.
```

```python
# Order Matters in Positional Arguments
# If you mix up the order of the arguments in a function call when using positional arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('harry', 'hamster')

```

```
I have a harry.
My harry's name is hamster.
```

```python
# Keyword Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')

describe_pet(pet_name='harry', animal_type='hamster')
# The order of keyword arguments doesn't matter.
# Be sure to use the exact names of the paraments in the function's definition.

```

```python
# Default Values
# Set the default value of animal_type to 'dog'
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')

# The simplest way to use this function.
describe_pet('willie')

# To describe an animals other than a dog.
describe_pet(pet_name='harry', animal_type='hamster')

#Any parameter with a default value needs to be listed after all the parameters that don't have default values.
```

```
I have a dog.
My dog's name is Willie.

I have a dog.
My dog's name is Willie.

I have a hamster.
My hamster's name is Harry.
```


### Return Values
---
```python
# Returning a Simple Value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
# The value of full_names is converted to title case.
# And then returned to the calling line.

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

```

```
Jimi Hendrix
```

```python
# Making an Arguments Optional
def get_formatted_name(first_name, last_name, middle_name=''):
# Make the middle name optional, give the middle_name argument an empty default value.

# To make get_formatted_name() work without a middle name
# Set the default value of middle_name to an empty string and move it to the end of the list of parameters.
    """Return a full name, neatly formatted."""
    if middle_name:
    # Python interprets non-empty strings as True
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# Python interprets non-empty strings as True.

```

```
Jimi Hendrix
John Lee Hooker
```

```python
# Returning a Dictionary
```

```python
# Using a Function with a while Loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First_name: ")
    if f_name == 'q':
        break

    l_name = input("Last_name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

# The break statement offers a straightforward way to exit the loop.
```

```
Please tell me your name:
(enter 'q' at any time to quit)
First_name: jimmy
Last_name: chen

Hello, Jimmy Chen!

Please tell me your name:
(enter 'q' at any time to quit)
First_name: jimmy
Last_name: q
JIMMY:Desktop jimmy$
```

### Passing a List
---
```python
```
