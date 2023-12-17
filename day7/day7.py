# Sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
len(it_companies)

# Addition
it_companies = {'Facebook', 'Google', 'Microsot', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.add('Twitter')
print(it_companies)

# Add multiple items

it_companies = {'Facebook', 'Goggle', 'Microsoft', 'Apple'}
it_companies.update(['IBM', 'Oracle', 'Amazon', 'Twitter'])
print(it_companies.update)

# Removing items from set

it_companies = {'Facebook', 'Goggle', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Twitter' 'Amazon'}
it_companies.remove('Oracle')
print(it_companies.remove)

# Difference between remove and discard
# Remove: if the item is not found remove() method will raised errors
# Discard: method doesn't raised any errors.

# Exercise level 2

# Join two sets
it_companies1 = {'Facebook', 'Goggle', 'Microsoft', 'Apple'}
it_companies2 = {'IBM', 'Twitter', 'Oracle', 'Amazon'}
it_companies3 = it_companies1.union(it_companies2)
print(it_companies3)

# Intersections
it_companies1 = {'Facebook', 'Goggle', 'Microsoft', 'Apple'}
it_companies2 = {'IBM', 'Twitter', 'Oracle', 'Amazon'}
it_companies1.intersection(it_companies2)
print(it_companies1.intersection)

# Subset
it_companies1 = {'Facebook', 'Goggle', 'Microsoft',}
it_companies2 = {'Apple', 'IBM'}
it_companies2.issubset(it_companies1)
print(it_companies2.issubset)

# Disjoint set
it_companies1 = {'Facebook', 'Goggle', 'Microsoft'}
it_companies = {'Apple', 'IBM', 'Amazon', 'Oracle'}
it_companies1.isdisjoint(it_companies2)
print(it_companies1.isdisjoint)

# Join two sets
it_companies1 = {'Facebook', 'Goggle', 'Microsot'}
it_companies2 = {'Apple', 'IBM', 'Amazon'}
it_companies3 = it_companies1.union(it_companies2)
print(it_companies3)
it_companies3 = it_companies2.union(it_companies1)
print(it_companies3)

# Symmetric
it_companies1 = {'Facebook', 'Goggle', 'Microsoft'}
it_companies2 = {'Apple', 'IBM', 'Amazon'}
it_companies1.symmetric_difference(it_companies2)
print(it_companies1.symmetric_difference)

# Deleting sets
it_companies = {'Facebook', 'Goggle', 'Microsot', 'Apple', 'IBM', 'Amazon'}
del it_companies
print(it_companies3)

#Exercise level 3

# Converting Set
it_companies = {'Facebook', 'Goggle', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
age = {22, 19, 24, 25, 26, 24, 25, 24}
age = set(age)
print(age)
len(age)

# String is a collection of alphabets, words or other characters.
# List is a data structure that is mutable.
# Tuple is a data structure that is unmutable.
# List is a collection of items.

sentence = ['''I am a teacher,
I love to inspire,
And teach people''']
print(sentence)