# Exercise level 1
# Function

# declaring a function
def add_two_numbers ():
    num_one = 2
    num_two =3
    total = num_one + num_two
    print(total)
    add_two_numbers()

# function that calculate area of cycle
    def area_of_cycle (r):
        PI = 3.14
        area = PI * r ** 2
        return area
    print(area_of_cycle(10))

    # add all_nums
    def sum_all_nums(*nums):
        total = 0
        for num in nums:
            total += num
            return total
        print(sum_all_nums(2, 3, 5))

# converting function
celsius_temp = 45
fahrenheit_temp = celsius_temp * 1.8+32
print("The Fahrenheit equivalent of 45 celsius = ", fahrenheit_temp )

# checks month in a season
def get_season(month):
    season = {
        'Spring': ['September', 'October', 'November'],
        'Summer': ['December', 'January', 'February'],
        'Autumn': ['March', 'April', 'May'],
        'Winter': ['June', 'July', 'August']
    }
key = season.keys()
for k in key:
    if month in season[k]: return k
    return 'invalid month'
print(get_season('October'))

# calculate_slope
def slope(x1, x1, x2, x2):
    m = (y2-y1)/(x2-x1)
    return m
print slope(2, 3, 6, 7)

# Quadratic equation
import cmath
a = 1
b = 5
c = 6

d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
soln2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))

# declare a function named print list
n = [3, 5, 7]

def print_list(x):
    for i in range(0, len(x)):
        print x[i]

        print_list(n)

# declare a function named reverse_list
def reverse_list(arr =[]):
    for i in arr[::-1]:
        print(i)
        arr_num =[1, 2, 3, 4, 5]
        arr_alp =['a', 'b', 'c']

        print(reverse_list(arr_num))
        print(reverse_list(arr_alp))

# declare a function named capitalize list items
list = ['a', 'b', 'c']

for i in range(len(list)):
    list(i) = list(i).upper()

    print(list)

# declare a function named add item
def add_two_numbers  ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())

# declare a function remove
def remove_item(list, *args):
    return [i for i in list if i not in args]

list = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(list, 'Mango'))

# sum of numbers
def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=
        print(total)
        print(sum_of_numbers(10))
        print(sum_of_numbers(100))

# odd number
x=int(input(5))
y=int(input(100))

def sumOdds(x,y):
    count=0
    for i in range(x,y):
        if (int(i%2==1)):
            count=count+i

            print(count)
            sumOdds(x,y)

# sum of even
def sum_of_even_num(start, end)
    sum = 0
    start += start % 2
    while start <= end:
        sum += 2
        return sum
    
# Exercise level 2
    
# declare function of odd and even number
function sumOddEven(n) {
    const floor = Math.floor(n / 2);
    const ceil = Math.ceil(n / 2);
    return [ceil * ceil, floor * (1 + floor)];
}

console.log('sumOddEven'(100))
print(console.log)
print(sumOdds)
print(sumEven)

# call your function factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
n = int(input(10))
print(facorial(n))

# call your function is empty
my_list = [
    if not my_list:
    print("the list is empty")
    else:
    print("the list is not empty")
]

# write different functions
numbers = [4, 10, 29, 33, 42, 67]

def find_mean(list_of_numbers):
    sum_n = sum(list_of_numbers)
    len_n = len(list_of_numbers)
    mean = sum_n/len_n
    return mean

result = find_mean(numbers)
print(result)

# median
numbers_even = [4, 10, 29, 33, 42, 67]
numbers_odd = [4, 10, 29, 33, 42, 67, 99]
def find_median(list_of_numbers):
    list_of_numbers.sort()
    length = len(list_of_numbers)
    length_is_odd = True if length % 2 == 0 else False
    if length_is_odd:
      index = length//2
      median = list_of_numbers[index]
    else:
        index_1 = length//2
        index_2 = index_1 + 1
        median = (list_of_numbers[index_1] + list_of_numbers[index_2]) / 2
        return median
    find_median(numbers_odd)
    find_median(numbers_even)

    # mode
    n = [4, 4, 4,4, 6, 6, 6, 6, 6, 6, 8, 8, 8, 8, 9, 10, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    def calculate_mode(list_of_numbers):
        counter = {}
        for i in list_of_numbers:
            if i in counter:
                counter[i]+= 1
            else:
                counter[i] = 1
    key_max = sorted(counter, key=counter.get, reverse=True)[:1][0]
    frequency = counter[key_max]
    return key_max, frequency

calculate_mode(n)

# range
numbers = [4, 10, 29, 33, 42, -67]
def find_range(list_of_numbers):
    n_min = min(list_of_numbers)
    n_max = max(list_of_numbers)
    n_range = n_max - n_min
    return n_min, n_max, n_range
find_range(numbers)
(-67, 42, 109)

# variance
import statistics
list1 = [1, 2, 3, 4, 5, 6]
print("The original list is : " + str(list1))
statistics.variance(list1)
print("The variance of list is:" + str(ans))

# standard deviation
import statistics
sample = [1, 2, 3, 4, 5]
print("Standard Deviation of sample is % s"
      % (statistics.stdev(sample)))
# is_prime function
def is_prime(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
        return True
    
# is_unique function
def allUnique(x):
    seen = list()
    return not any(i in seen or seen.append(i) for i in x)
allUnique([list("ABC"),("DEF")])
True
allUnique([list("ABC"), list("DEF"), list("ABC")])
False

# same type function
def homogeneous_type(seq):
    iseq = iter(seq)
    first_type = type(next(iseq))
    return first_type if all( (type(x) is first_type) for x in iseq ) else False

# checks if variable is valid
'x'.isidentifier()
True
'x123'.isidentifier()
True
'2'.isidentifier()
False
'while'.isidentifier()
True

# create a function called the most spoken languages
def most_spoken_languages(data):
    dict = {}
    for country in data:
        for lan in country["language"]:
            if lan in dict:
            else:
                dict[lan]=1
                arr = list(dict.values())
                arr.sort(reverse=True)
                arr = arr[:10]
                result = []
                for i in arr:
                    for key in dict:
                        if i == dict[key]:
                            return list(set(result))[:10]
print(most_spoken_languages(data))

# create a function caalled the most populated countries
def most_populated_countries(data):
    dict = {}
    arr = []
    for i in data:
        arr.append(i["population"])
        arr.sort(reverse=True)
        arr = arr[:10]
        result = []
        for i in arr:
            for j in data:
                if i == j["population"]:
                    result.append(j["name"])
                    return result
print(most_populated_countries(data))