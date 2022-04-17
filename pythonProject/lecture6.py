def alien_colors1(alien_color):
    if (alien_color == 'green'):
        print("Hurray! you earned 5 points")

alien_colors1('green')
alien_colors1('yellow')

def alien_colors2(alien_color):
    if (alien_color == 'green'):
        print("Hurray! you earned 5 points")
    else:
        print("Hurray! you earned 10 points")

alien_colors2('green')
alien_colors2('yellow')

def alien_colors3(alien_color):
    if (alien_color == 'green'):
        print("Hurray! you earned 5 points")
    elif(alien_color == 'yellow'):
        print("Hurray! you earned 10 points")
    elif (alien_color == 'red'):
        print("Hurray! you earned 15 points")

alien_colors3('green')
alien_colors3('yellow')
alien_colors3('red')


def stages_of_life(age):
    if(age < 2):
        print("The person is a baby")
    elif(age >=2 and age< 4):
        print("The person is a toddler")
    elif (age >= 4 and age < 13):
        print("The person is a kid")
    elif (age >= 13 and age < 20):
        print("The person is a teenager")
    elif (age >= 20 and age < 65):
        print("The person is an adult")
    elif (age >= 65):
        print("The person is an elder")

stages_of_life(25)

def favourite_fruit():
    favourite_fruits = ["Mango", "Apple", "Banana"]
    if 'Mango' in favourite_fruits:
        print(f"You really like Mangoes!")
    if 'Apple' in favourite_fruits:
        print(f"You really like Apples!")
    if 'Banana' in favourite_fruits:
        print(f"You really like Bananas!")
    if 'Avocado' in favourite_fruits:
        print(f"You really like Avocado!")
    if 'Cherry' in favourite_fruits:
        print(f"You really like Cherries!")

favourite_fruit()
def hello_admin():
    usernames = ['abc', 'xyz', 'pqr', 'admin', 'stu']

    for user in usernames:
        if(user == 'admin'):
            print("Hello Admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")

    usernames.clear()

    if len(usernames) == 0:
        print("We need to find some users")

hello_admin()

def unique_users():
    current_users = ['ABC', 'def', 'ghi', 'jkl', 'mno']
    new_users = ['abc', 'pqr', 'stu', 'ghi', 'xyz']

    current_users = list(map(str.lower,current_users))

    for user in new_users:
        if user.lower() in current_users:
            print(f"{user} username is already used. Try other username")
        else:
            print(f"{user} username is available")

unique_users()

def ordinal_numbers():
    numbers = [1,2,3,4,5,6,7,8,9]

    for i in numbers:
        if i == 1:
            print("1st")
        elif i == 2:
            print("2nd")
        elif i == 3:
            print("3rd")
        else:
            print(f"{i}th")

ordinal_numbers()
