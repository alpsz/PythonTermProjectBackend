# question 1

def stringLen(str):
    return len(str)

print(stringLen("python"))

########################################################################################################################

# question 2

def checkKey(dict, key):
    if key in dict:
        return True
    else:
        return False

def frequencyCounter(str):
    frequency = {}
    for i in str :
        if checkKey(frequency, i):
            frequency[i] = int(frequency[i]) + 1
        else:
            frequency[i] = 1
    return frequency

print(frequencyCounter("google.com"))

########################################################################################################################

# question 3
def stringFunctions(str, count, find):
    print(f"Capitalize the given string: {str.capitalize()}")
    print(f"Converting a string to lower case: {str.casefold()}")
    print(f"Calculating a word frequency in string: {str.count(count)}")
    print(f"Finding the first occurrence of a value: {str.find(find)}")
    print(f"Return first index of a given value: {str.index(find)}")
    print(f"Replace a given word from the string: {str.replace(count, 'Hi')}")
    print(f"Converts a string to uppercase: {str.upper()}")
    print(f"Returns a trimmed version of the string: {str.strip()}")


stringFunctions(" Hello, welcome to my world. ", "Hello", "welcome")

########################################################################################################################

# question 4

def tempConvertor(fahrenheit):
    return ((fahrenheit-32)*5)/9

print(f"The value of 54 fahrenheit in degree celsius is:{tempConvertor(54)}")