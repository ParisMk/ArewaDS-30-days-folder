# Empty tuple
# syntax
empty_tuple = ()
## or using the constructor
empty_tuple = ()

# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5', 'item6')

Brothers = ('Mustafa', 'Bashir', 'Abba')
Sisters = ('Maryam', 'Kadija', 'Rukayya')
Siblings = Brothers + Sisters
print(Siblings)
Siblings = ('Mustafa', 'Bashir', 'Abba', 'Maryam', 'Kadija', 'Rukayya')
Family = list(Siblings)
Family[0:1] = 'Mukhtar', 'Rahama'
print(Family)

# Exercise Level 2
Family = ('Mukhtar', 'Rahama', 'Mustafa', 'Bashir', 'Abba', 'Maryam', 'Kadija', 'Rukayya')
all_Family = Family[0:7]
print(all_Family)
Family = ['Mukhtar', 'Rahama', 'Mustafa', 'Bashir', 'Abba', 'Maryam', 'Kadija', 'Rukayya']
parent = Family[0:2]
Siblings = Family[2:7]
print('Parent:', parent)
print('siblings:', Siblings)

# syntax
tpl1 = ('item1', 'item2', 'item3', 'item4')
tpl2 = ('item5', 'item6', 'item7', 'item8', 'item9')
tpl3 = ('item10', 'item11', 'item12',)
tpl4 = tpl1 + tpl2 + tpl3

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animal_products = ('meat', 'milk', 'butter')
fruits_and_vegetables_and_animal_products = fruits + vegetables + animal_products
print(fruits_and_vegetables_and_animal_products)

# changing tuple to list
# syntax

food_stuffs = ('banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot', 'meat', 'milk', 'butter')
food_stuffs = list(food_stuffs)
food_stuffs[0] ='guava'
print(food_stuffs)
food_stuffs = tuple(food_stuffs)
print(food_stuffs)
food_stuffs = list(food_stuffs)
print(food_stuffs)
first_three = food_stuffs[0:3]
last_three = food_stuffs[8:11]
print('First three:', first_three)
print('Last three:', last_three)

# deleting tuple
# syntax
tpl = ('item1', 'item2', 'item3')
del tpl1

food_stuffs = ('banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot', 'meat', 'milk', 'butter')
del food_stuffs