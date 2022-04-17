def conditional_test():
    car = 'subaru'
    carList = ["Subaru", "Audi", "BMW", "Toyota", "Mercedes", "Porche"]
    print("is car == 'subaru?' I predict True.")
    if (car == 'subaru'):
        print(f"car == '{car}'")
    print("\nis car == 'audi'? I predict False.")
    car = 'audi'
    if (car != 'subaru'):
        print(f"car == '{car}'")

    if (car.upper() == 'audi'):
        print(f"Case is similar, car == '{car}'")
    else:
        print(f"Case is not same, car == '{car}'")

    if (len(car) == len('audi')):
        print(f"Length is equal, car == '{car}'")
    else:
        print(f"Length is not equal, car == '{car}'")

    if (type(car) == type('audi')):
        print(f"Type is equal, car == '{car}'")
    else:
        print(f"Type is not equal, car == '{car}'")

    if (car[1] == 'u'):
        print(f"Character at index 1 is u")
    else:
        print(f"Character at index 1 is not u")

    if (len(car) >= 3 and len(car) <= 10):
        print(f"String is within the range of 3 to 10")
    else:
        print(f"String doest not validates the given condition")

    if 'Audi' in carList:
        print(f"Audi is present in the car list")

    if 'Jaguar' in carList:
        print(f"Jaguar is not in the car list")
    else:
        print(f"Jaguar is not in the car list")

    if 'audi' in carList or 'Audi' in carList:
        print(f"Audi is present in the car list")

    if (len(carList[0]) > len(carList[1])):
        print(f"Length of first string in the list is bigger then the second one")
    else:
        print(f"Length of second string in the list is bigger then the first one")

conditional_test()


