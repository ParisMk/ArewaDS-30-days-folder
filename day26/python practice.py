x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')

    print('finis')

n = 5
while n > 0 :
    print(n)
    n = n - 1
    print('Blastoff:')

message = "Hello Python World!"
print(message)

message = "Hello Python Crash Course WOrld"

print(message)

message = "Ga rashin cika alkawari"
print(message)

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

print("Languages:\n\tpython\n\tC\n\tJavaScript")

print("names:\n\tSalman\n\tMukhtar\n\tKallamu")

print("numbers:\n\t1\n\t12\n\t123\n\t1234\n\t12345\n\t123456\n\1234567")

print("seven:\n\t#\n\t##\n\t###\n\t####\n\t#####\n\t######\n\t#######")

universe_age = 14_000_000_000
print(universe_age)
print(5+3)

# Lists
bycicles = ['trek', 'cannondale', 'redline', 'specialized']
print(bycicles)
print(bycicles[0])
print(bycicles[0].title())
print(bycicles[-1].title())

message = f"My first bycicle was a {bycicles[0].title()}."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

# Empty list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki') 
print(motorcycles)

# Inserts
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing elements from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# Removing an item using pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# popping items from any position in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Removing an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# Sorting list parmanently
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# reverse sorting
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# sorting list temporarily
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# Reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# Finding the lenght of a list
cars = ['bmw', 'audi', 'toyota', 'subaru'] 
len(cars)

# Loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

magicians = ['alice', 'david', ' carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    print("Thank you, everyone. That was a great magic show!")

# indentation error
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# forgetting to indent additional lines
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print("f{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I cant wait to see your next trick, {magician.title()}.\n")
    print("Thank you everyone, that was a great magic show!")

# Range function
for value in range(1, 5):
    print(value)

for value in range(1, 6):
    print(value)

for vaalue in range(6):
    print(value)

# Using range to make a list of numbers
numbers = list(range(1, 6))
print(numbers)

# How to list even numbers in a range
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# squares to list
squares = []
for value in range(1, 11):
    square = value ** 2
    print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)
    print(squares)

squares = []
for value in range(2,12):
    squares.append(value**2)
    print(squares)

squares = [value**2 for value in range(1, 11)]
print(squares)

squares = [value**2 for value in range(2, 12)]
print(squares)

# SLICE
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# Looping through a slice 
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players in my team:")
for player in players[:3]:
    print(player.title())

# copying list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_food)

my_foods.append('cannoli')
friend_food.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friends favorite foods are:")
print(friend_food)

# Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

dimensions = (200, 50)
print("original dimensions:")
for dimension in dimensions:
    print(dimension)

dimension = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# If statement
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# checking inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

    requested_toppings = ['mushrooms', 'onions', 'pineapple']
    'mushrooms' in requested_toppings
    'pepperoni' in requested_toppings
    
# simple if statement
age = 19

if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

 # if elif else
    age = 12
    if age < 4:
        print("Your admission cost is 0.")

    elif age < 18:
        print("Your admission cost is $25.")
    else:
        print("Your admission cost is $40.")

age = 12

if age < 4:
    price = 0

elif age < 18:

    price = 25

else:

    price = 40

print(f"Your admission cost is ${price}.")

# Using multiple elif blocks
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
    print(f"Your admission cost is${price}.")

# Omitting the else block
    age = 12
    if age < 4:
        price = 0
    elif age < 18:
        price = 25
    elif age < 65:
        price = 40
    elif age >= 65:
        price = 20
    print(f"Your admission cost is ${price}.")

# Testing multiple conditions
    requested_toppings = ['mushrooms', 'extra cheese']
    if 'mushrooms' in requested_toppings:
        print("Adding mushrooms.")
    if 'pepperoni' in requested_toppings:
        print("Adding pepperoni.")
    if 'extra cheese' in requested_toppings:
        print("Adding extra cheese.")
        print(f"\nFinished making your pizza!")
    
# function
        def greet_user():
            """Display a simple greeting."""
            print("Hello!")
            greet_user()
            
def greet_user(username):

    """Display a simple greeting."""
    print(f"Hello, {username.title()}!") 
    greet_user('jesse')

