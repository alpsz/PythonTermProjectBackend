pizza = ["Neapolitan Pizza","Deep-Dish Pizza", "Sicilian Pizza"]

for i in pizza:
    print(f"I like eating {i}")

print("The pizza itself looks so yummy, crispy and so cheesy. There is no better feeling in the world than a warm pizza box on your lap. My love for Pizza is very high. I am always hungry for pizza, be it any time of the day. I really love pizza!")

animals = ["Dog", "cat", "horse"]

###################################################################################################

for i in animals:
    print(f" A {i} would make a great pet.")

print("All these animals are pet animals and any of these animals would make a great pet.")

###################################################################################################


for i in range(1, 21):
    print(i)

millions = range(1,1000001)
for million in millions:
    print(million)

print(min(millions))
print(max(millions))
print(sum(millions))

###################################################################################################

odd_numbers = range(1, 21, 2)
for i in odd_numbers:
    print(i)

###################################################################################################

recipes = ("Rice", "chicken", "eggs", "tacos", "soup")
for i in recipes:
    print(i)

###################################################################################################

recipes["soup"] = "Vegetable Soup"

recipes = ("Rice", "chicken", "Scrambled eggs", "tacos", "Vegetable soup")
for i in recipes:
    print(i)


###################################################################################################

def make_shirt(size, msg):
    print(f"The size of the shirt is {size} with a message on it as {msg}")

make_shirt("medium", "Laugh love live")
make_shirt(msg = "Laugh love live", size = "medium")


###################################################################################################


def make_shirt(size = "large", msg = "I love python"):
    print(f"The size of the shirt is {size} with a message on it as {msg}")
    size = "Medium"
    print(f"The size of the shirt is {size} with a message on it as {msg}")
    size = "Small"
    msg = "Laugh love live"
    print(f"The size of the shirt is {size} with a message on it as {msg}")

make_shirt()

###################################################################################################

def describe_city(name, country = "India"):
    print(f"{name} is in {country}")

describe_city("Mumbai")
describe_city("Delhi")
describe_city("Toronto", "Canada")

###################################################################################################


def city_country(name, country):
    return '"'+name+', '+country+'"'

print(city_country("Mumbai", "India"))
print(city_country("Delhi", "India"))
print(city_country("Toronto", "Canada"))

###################################################################################################


def make_album(artist_name, album_title, songs = "none"):
    albums = {}
    albums["artist_name"] = artist_name
    albums["album_title"] = album_title
    albums["songs"] = songs
    return albums

print(make_album("Arijit Singh", "Aashiqui 2"))
print(make_album("Atif Aslam", "Rustom", 5))
print(make_album("Jubin nautiyal", "Kabir singh", 4))

###################################################################################################


while (True):
    artist_name = input("Enter the name of artist: ")
    album = input("Enter the name of album: ")
    print(make_album(artist_name, album))
    break


###################################################################################################


