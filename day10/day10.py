# Exercise Level 1
# While loop

count = 0
while count < 10:
    print(count)
    count = count + 1
else:
    print(count)

    # for loop
    numbers = [0, 1, 2, 3, 4, 5]
    print(numbers)

    language = 'python'
    for letter in language:
        print(letter)

# iterate 10 to 0
        count = 10
        while count < 0:
            print(count)
            count = count + 1

# For loop
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)

# loops that make seven calls
    
n = int(input(7))
for i in range(1,n+1):
    for j in range(1, i+1):
        print(j,end="")
        print()

# Using nested loop to creat pattern
num = int(input(8))
n_list =[[0 for x in range (num)] for y in range(num)]
for i in range(num):
    for j in range(num):
        print(n_list[i][j],end="/t/")

def table(n):
    for i in range (1, 11):
n = 5
table(n)
print("%n * %n = %n %")

# iterate for loop
language = ['python', 'numpy', 'pandas', 'django', 'flask']
print(language)

# using loop to iterate 0 to 100 even numbers
for i in range(0, 101):
    if i % 2 == 0:
        print(i, end=",")

# using loop to iterate 0 to 100 odd numbers
        for i in range(1, 101):
            if i % 2 != 0:
                print(i,end=",")

#Exercise Level 2

# using loop to iterate sum 0 to 100
c = 0
for i in range(0, 101):
    c+=i
    print(c)

# using loop to iterate sum of 0 to 100 and print odds and evens
let i;
let sumE =0
let sumO = 0;
for (i = 0; i <= 100; i++) {
    i % 2 === 0 ? (sumE += i) : (sumO += 1);
}
console.log(sumE, sumO);
print(console.log)

# Exercise Level 3
 countries_with_the_word_land = [
     'Finland',
     'Iceland',
     'Ireland',
     'Marshall Islands',
     'Netherland',
     'New Zealand',
     'Poland',
     'Solomon Islands',
     'Swaziland',
     'Switzerland',
     'Thailand',
 ]
print(countries_with_the_word_land)

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
fruits.reverse()
print(fruits)

countries_languages =[365]
print(countries_languages)

Ten_most_spoken_languages = ['English', 'Portuguese', 'Mandarin', 'Hindi', 'Spanish', 'French', 'Arabic', 'Bengali', 'Russian', 'Portuguese', 'Urdu']
print(Ten_most_spoken_languages)

countries_with_highest_population = ['India', 'China', 'United states', 'Indonesia', 'Pakistan', 'Nigeria', 'Brazil', 'Bangaledash', 'Russia', 'Mexico']
print(countries_with_highest_population)
