# Function
# 8.2 message

def display_message():
    print("I am learning about functions in chapter 8.")

display_message()

# 8.2 Favorite book

def favorite_book(title):
    print("One of my favorite is " + title.title())

favorite_book("Rich Dad Poor Dad")    

# 8.3 Make Shirt

def make_shirt(size, text):
    print("\nYou have ordered a " + "shirt that says " + text)

make_shirt('large', '"Suck it Trebek"')
make_shirt(size = 'smedium', text = '"I need a bigger shirt"')

# 8.4 Large shirt

def make_shirt(size = 'medium', text = '"I love Python"'):
    print("\nYou have ordered a " + size + " shirt that says " + text)

make_shirt('large')
make_shirt()
make_shirt('small', '"I am a big brother"')

# 8.5 Cities

def describe_city(city, country = 'united states'):
    print("\n" + city.title() + country.title())

describe_city('Atlanta')
describe_city('las vegas')
describe_city('paris', 'france')

# 8.6 City names

def city_country(city, country):
    return(city.title() + ", " + country.title())

print(city_country('santiago', 'chile'))
print(city_country('berlin', 'germany'))
print(city_country('paris', 'france'))

# 8.7 Album

def make_album(artist, title, num_tracks = ''):
    album = {'artist': artist, 'title': title}
    if num_tracks:
        album['# of tracks'] = num_tracks
        return album
    
garth = make_album('garth brooks',"garth's greatest hits")
print(garth)

kenny = make_album('kenny chesney' 'road and the radio', 12)
print(kenny)

# 8.8 User albums

while True:
    print("\nEnter the album information:")
    print("(enter 'q' at any time to quit)")

# 8.9 magician's names
    
magicians = ['william', 'luke', 'allie']

def show_magicians(names):
    for name in names:
        print(name.title())

show_magicians(magicians)
greets = []
def make_greet(names):
    for name in names:
        greets.append(name.title() + ' the Great')

make_great(magicians)
print(greats)