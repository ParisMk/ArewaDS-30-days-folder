# Creating empty dictionary
empty_dict = {}

dog = {
    'name':'Hunter',
    'color':'black',
    'breed':'German shepperd',
    'legs':'tall',
    'age':'3'
}
print(dog)

# Students dictionary
student = {
    'first_name':'Salmanu',
    'last_name':'last_name',
    'gender':'male',
    'age':'30',
    'marital status':'single'
    'skills':'learning'
    'country':'Nigeria'
    'city':'Katsina' 
}
print(student)
print(len(student))

# value of skill

skills = student.values()
print(skills)

# modify the skills
student = {
    'first_name':'Salmanu',
    'last_name':'Muntari',
    'gender':'male',
    'age':'30',
    'marital_status':'single',
    'skills':'learning',
    'country':'Nigeria',
    'city':'Katsina'
}
student['skills'] = 'python'
print(skills)

# dictionary values as a list
food = {'fruit1':'Banana', 'fruit2':'Orange', 'fruit3':'Mango', 'fruit4':'Lemon'}
values = food.values()
print(values)

# change the dictionary to a list of tuples
fruits = {'key1':'banana', 'key2':'orange', 'key3':'mango'}
print(fruits.items())

fruits = {'key1':'banana', 'key2':'orange', 'key3':'mango'}
del fruits

del fruits['key2']