# Higher oder function

# Exercise: Level 1
1. # Map returns the same length processed array back
   # Filter returns only the elements that satisfy the condition
   # Reduce returns a single value, such as sum or product of a list

# Explain the difference between higher order function, closure and decorator
   ## Higher order function, takes function as parameter, assign function to a variable
   ## Closure, python allows a nested function to access the outer scope of the enclosing function
   ## Decorator, is a design pattern in python that allows a user to add new functionality to an existing object without modifying it structure.

# Define a call function before map, filter or reduce, see examples.
def sum_arr(i):
    return i*2
sum_up = map(sum_arr,[1,2,3])
print(list(sum_up))

# use for loop to print each country in the countries list.
for i in countries:
    print(i)

    # use for to print each name in the names list
for i in names:
    print(i)

# use for to print each number in the numbers list
    for i in numbers:
        print(i)

# Exercise Level 2
# use map to create a new list by changing each country to uppercase in the countries lists
        def upper(x):
            return x.upper()
            make_upper = map(upper,country)
            print(list(make_upper))

# use map to create a new list by changing  each number to its square in the numbers list
            def square(x):
                return x**2
            make_square = map(square,numbers)
            print(list(make_square))

# use map to change each name to uppercase in the names list
def upper(x):
    return x.upper()
make_upper = map(upper,names)
print(list(make_upper))

# use filter to filter out countries containing 'land'.
def filter.country(country):
if "land" not in country:
    return True
return False

country_no_land = filter(filter_country,countries)
print(list(list_no_land))

# use filter to filter out countries having six characters.
def filter_country(country):
    if len(country) == 6:
        return True
    return False

country_no_land = filter(filter_country,countries)
print(list(country_no_land))

# use filter to filter out countries containing six letters and more in the country list.
def filter_country(country):
    if len(country) >= 6:
        return True
    return False

country_no_land = filter(filter_country,countries)
print(list(country_no_land))

# use filter to filter out countries starting with an 'E'
def filter_country(country):
    if country.startswith("E"):
        return True
    return False

country_no_land = filter(filter_country,countries)
print(list(country_no_land))

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
def get_string_lists(lis):
    return list(filter(lambda x : isinstance(x,str),lis))
print(get_string_lists([1,2,3,"a"]))

# use reduce to sum all the numbers in the numbers list.
numbers_str = ['1', '2', '3', '4', '5']
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)

# use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def concatenate_countries(x,y):
    return f"{x},{y}"
total = reduce(concatenate_countries, countries)
print(f"{total} are countries.")

# Declare a function called categorize_countries
def categorize_countries():

# create a function returning a dictionary, where keys stand for
def country_dictionary(countries):
    dict = {}
    for country in countries:
        if country[0] in dict:
            dict[country[0]]+=1
        else:
            dict[country[0]]=1
            return dict
        print(country_dictionary(all_countries))

# declare a get_first_ten_countries function that returns the first ten countries in the countries list.
def get_first_ten_countries(lis):
    return lis[10:]
print(get_first_ten_countries(all_countries))

# declare a get_last_ten_countries function
def get_last_ten_countries(lis):
    return lis[-10:]
print(get_last_ten_countries(all_countries))

# Exercise Level 3
# use the countries_data.py
# sort countries by name, by capital, by population

def name(data):
    arr = []
    for i in data:
        arr.append(i["name"])
        arr.sort()
        return arr
    print(name(data))

    def capital(data):
        arr = []
        for i in data:
            arr.append(i["capital"])
            arr.sort()
            return arr
    print(capital(data))

def population(data):
    arr =[]
    for i in data:
        arr.append(i["population"])
        arr.sort()
        return arr
    print(population(data))