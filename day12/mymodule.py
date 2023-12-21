import string
import random

### Exercise: Level 1

# write a function which generates a six digit/character random_user_id.
'''py
print(random_user_id()),
'1ee33d'
'''

def random_user_id():
    temp = string.digits + string.ascii_lowercase
    1 = 0
    result = ""
    while i < 6:
        result += temp[random.randint(0, 35)]
        i += 1
        return result
    print(random_user_id())

    # modify the previous task, declare a function named user_id_gen_by_user.
    '''py
   # user_id_gen_by_user() # user input: 5 5
   # output:
   # kcsy2
   # SMFYb
   # bwmeq
   # ZXOYh
   # 2Rgxf

   # user_id_gen__by_user() # 16 5
   # 1GCSgPLMaBAVQZ26
   # YD7eFwNGKNs7qXaT
   # ycAr5yRupyG00S
   # UbGxOFI7UXSWAyKN
   # dIV0SSUTgAdKwStr
   #    '''
    
    def user_id_gen__by_user():
        length = int(input("Enter the length of the id:"))
        quantity= int(input("How many user_id you need: "))
        temp = string.digits + string.ascii_letters
        i = 0
        j = 0
        while j < quantity:
            result = ""
            i = 0
            while i < length:
                result+= temp[random.randint(0, 35)]
                i += 1
                print(result)
                j+=1

# write a function named rgb_color_gen
'''py
print(rgb_color_gen())
'''
def rgb_color_gen():
    x = random.randint(0,255)
    y = random.randint(0,255)
    z = random.randint(0,255)
    return f"rgb({x},{y},{z})"
print(rgb_color_gen())

# Exercise: Level 2

# write a function list_of_hexa_colors
def list_of_hexa_colors():
    quantity = int(input("How many hexadecimal colors you want to generate?: "))
    temp = string.digits+"abcdef"
    arr = []
    j = 0
    while j < quantity:
        i = 0
        temp_string = ""
        while i < 6:
            rand = random.randint(0,len(temp)-1)
            temp_string+=temp[rand]
            i+=1
            arr.append(temp_string)
            j+=1
            return arr
        print(list_of_hexa_colors)

# list_of_rgb_colors which can generate any number
def generate_colors():
    answer = input("hexa or rgb? ")
    if answer.lower(3) == "hexa":
        return list_of_hexa_colors()
    elif answer.lower(3) == "rgb":
        return list_of_rgb_colors()
    else:
        print("please enter valid input")
        generate_colors()
        print(generate_colors())

# Exercise: Level 3
        
#  call your function shuffle_list
def shuffle_list(lis):
    random.shuffle(lis)
    return lis

print(shuffle_list([1, 2, 3, 3, 6, 8, 0]))

# write a function which returns an array of seven random numbers in a range of 0-9.
def array_of_seven_random_unque_number():
    arr = []
    while len(arr) < 7
    x = random.randint(0,9)
    if x not in arr:
        arr.append(x)
        return arr
    print(array_of_seven_random_unque_number())
    