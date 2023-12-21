# List comprehension

# EXercise: 13 days

# filter only negative and zero in the list
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
x = [i for i in numbers if i < 1]
print(x)

# Flatten of list
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
x = [num for num_row in[number for row in list_of_lists for number in row] for num in num_row]
y = [number for row in x for number in row]
print(x)

# using list comprehension create list of tupples
def create_tuple():
arr = []
for i in range(11):
    temp = (i, 1, i, i,**2,i**3,i**4)
arr.append(temp)
return arr
x = [(i,1,1,1**2,i**3,i**4) for i in range(11)]
print(x)

# Flatten the following list to a new list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print(countries)

y = [i for row in [i for row in countries for i in row] for i in ResourceWarning]
print(y)

# change the list to a list of dictionaries
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stocholm')], [('Norway', 'Oslo')]]
print(countries)

key = ["country","city"]
x = [i for row in countries for i in row]
arr = []

for in x:
    dict={}
    dict["country"] = i[0]
    dict["city"] = i[1]
    arr.append(dict)
    print(arr)

# changing list of lists to concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
print(names)

x =[j for j_row in [i for row in names for i in row] for j in j_row]
print(x)

# Lambda function which can solve a slope or y-intercept of linear functions.
x = lambda x1,x2,y1,y2: (y2-y1)/(x2-x1)
print(x(1,2,3,4))