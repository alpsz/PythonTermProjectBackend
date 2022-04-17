class Customer:
    def __init__(self, name, age, address, ac_no, exp):
        self.name = name
        self.age = age
        self.address = address
        self.ac_no = ac_no
        self.exp = exp

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} {self.age} {self.address} {self.ac_no} with an experience of {self.exp} at amazon"


class Address:
    def __init__(self, st_no, st_name, city, zip, state):
        self.st_no = st_no
        self.st_name = st_name
        self.city = city
        self.zip = zip
        self.state = state

    def __str__(self):
        return f"{self.st_no} {self.st_name} {self.city} {self.zip} {self.state}"

    def print_address(self):
        return f"{self.st_no} {self.st_name} {self.city} {self.zip} {self.state}"




c1_address = Address("12", "Lanyard rd", "North York", "M1H 2K2", "Ontario")
c1 = Customer("Santosh is", "20 years old and living at", c1_address, " with account number 123456789", "5")

print(c1)


########################################################################################################################

class Animal:

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} makes a sound")

    def can_eat(self):
        print(f"{self.name} is omnivore")

    def can_run(self):
        print(f"{self.name} runs very fast")

    def __str__(self):
        return f"{self.name} {self.age} {self.breed}"


class Cat(Animal):
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} makes a sound from cat class")

    def can_eat(self):
        print(f"{self.name} is omnivore from cat class")

    def can_run(self):
        print(f"{self.name} runs very fast from cat class")

class Dog(Animal):
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} makes a sound from dog class")

    def can_eat(self):
        print(f"{self.name} is omnivore from dog class")

    def can_run(self):
        print(f"{self.name} runs very fast from dog class")


animal = Animal("lion", "5", "African")
cat = Cat("snowfy", "6", "persian")
dog = Dog("leo", "7", "golden retriever")

animal.make_sound()
cat.can_eat()
dog.can_run()
