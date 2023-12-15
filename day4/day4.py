
# Single line comment
letter = 'P'              # A string could be a single character or a bunch of texts
print(letter)             # P
print(len(letter))        # 1
greeting = 'Hello, World!' # string could be a single or double quote, "Hello, World!"
print(greeting)            # Hello, World!
print(len(greeting))       # 13
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)

# Multiline String
Multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(Multiline_string)
# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

# String Concatenation
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name + space + last_name
print(full_name) # Asabeneh Yetayeh
# Checking lenght of a string using len() builtin function
print(len(first_name)) # 8
print(len(last_name)) # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 15

#### Unpacking characters
language = 'python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

# Accessing characters in strings by index
language = 'python'
first_letter =language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

# If we want start from right end we can use negative indexing. -1 is the last index
language = 'python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

# Slicing

language = 'python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three) # hon
last_three = language[3:]
print(last_three) # hon

# Skipping character while splitting python strings
language = 'python'
pto = language[0:6:2]
print(pto) # pto

# Escape sequence
print('I hope every one enjoying the python challenge./nDo you ?') # line break
print('day4/python/strings')
print('day1/python/Introduction')
print('day2/python/variables')
print('day3/python/operators')
print('day/python/strings')
print('This is a back slash symbol (//)') # To write a back slash
print('In every programming language it starts with /"Hello, World!"')

## String methods
# capitalize(): Converts the first character the string to Capital Letter

Challenge = 'thirty days of python'
print(Challenge.capitalize()) # 'Thirty  days of python'

# count(): return occurrences off substring in string, count(substring, start=.., end=..)

Challenge = 'thirty days of python'
print(Challenge.count('y')) # 3
print(Challenge.count('y', 7, 14)) # 1
print(Challenge.count('th')) # 2

# endswith(): Checks if a string ends with a specified ending

challenge = 'thirty days of python'
print(challenge.endswith('on')) # True
print(challenge.endswith('tion')) # False

# expandtabs(): Replaces tabs character with spaces, default tab size is 8. It takes tab size argument

challenge = 'Thirty/tdays/tof/tpython'
print(challenge.expandtabs()) # 'thirty days of python'
print(challenge.expandtabs(10)) # 'thirty days of python'

# find(): Return the index of first occurrence of substring 

challenge = 'thirty days of python'
print(challenge.find('y')) # 5
print(challenge.find('th')) # 0

# format()        formats string into nicer output
first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = 'I am {Salmanu} {Muntari}. I am a {student}. I live in {Nigeria}'
print(sentence)

radius = 10
pi = 3.14
area = pi # radius ## 2
result = 'The area of cycle with {} is {}'.format(str(radius), str(area))
print(result) # The area of cycle with 10 is 3.14.0

# index(): Return the index of substring
challenge = 'thirty days of python'
print(challenge.find('y')) # 5
print(challenge.find('th')) # 0

# isalnum(): checks alphanumeric character

challenge = 'ThirtyDayspython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

# isalpha(): Checks if all characters are alphabets

challenge = 'thirty days of python'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha()) # False

# isdecimal(): Checks decimal characters

challenge ='thirty days of python'
print(challenge.find('y')) # 5
print(challenge.find('th')) # 0

# isdigit(): Checks digit characters

challenge = 'thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit()) # True

# isdecimal(): Checks decimal characters

num = '10'
print(num.isdecimal()) # True
num = '10.5'
print(num.isdecimal()) # False


# isidentifier(): Checks for valid identifier means it check if a string is a valid variable name

challenge = '30Daysofpython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True


# islower(): checks if all alphabets in a string are lowercase

challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

# isupper(): returns if all characters are uppercase characters

challenge = 'thirty days of python'
print(challenge.isupper()) # False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True


# isnumeric(): checks numeric characters

num = '10'
print(num.isnumeric()) # True
print('ten'.isnumeric()) # False

# join(): Return a concatenated string

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
Result = '#, '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

# strip(): Remove both leading and trailing characters

challenge = 'thirty days of python'
print(challenge.strip('y')) # 5

# replace(): Replaces substring inside

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# split(): Splits string from left

challenge = 'thirty days of python'
print(challenge.split()) # ['thirty' 'days' 'of' 'python']

# title(): Returns a title cased string

challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

# swapcase(): checks if string starts with the specified string

challenge = 'thirty days of python'
print(challenge.swapcase())  # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase()) # tHIRTY dAYS oF pYTHON

# startswith(): checks if string starts with the string

challenge = 'thirty days of python'
print(challenge.startswith('thirty')) #  True
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False