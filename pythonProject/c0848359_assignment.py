# Ceasar Cypher Technique
def ceasarCypher(msg, shift):
    output = ""

    # using for loop to traverse entire msg
    for i in range(len(msg)):
        curr_char = msg[i]

        # If an uppercase letter is encountered then it gets encrypted (shifted)
        if (curr_char.isupper()):
            output += chr((ord(curr_char) + shift - 65) % 26 + 65)
            # ord function gives us the ASCII value of the given character and 65 is the starting value for Uppercase letters

        # If a lowercase letter is encountered then it gets encrypted (shifted)
        else:
            output += chr((ord(curr_char) + shift - 97) % 26 + 97)
            # ord function gives us the ASCII value of the given character and 97 is the starting value for lowercase letters

    return output


# Checking the applied technique
message = "ABC abc"
shift = 2
print(f"Message  : {message}")
print(f"Shift : {str(shift)}")
print(f"Cipher: {ceasarCypher(message, shift)}")

########################################################################################################################
########################################################################################################################

# Binary search algorithm
# Note: Given array is always sorted
# Technique 1: Iterative Approach
# Technique 2: Recursive Approach

# Iterative Approach

def iterativeBinarySearch(array, l_index, r_index, element):
    while l_index <= r_index:

        mid_index = l_index + (r_index - l_index) // 2

        # At first we check if element is present at mid-index
        if array[mid_index] == element:
            return mid_index

        # We will ignore the left half of the array if the element is greater than the mid-value
        elif array[mid_index] < element:
            l_index = mid_index + 1

        # We will ignore the right half of the array if the element is smaller than the mid-value
        else:
            r_index = mid_index - 1
    return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
element = 7

# Function call
output = iterativeBinarySearch(array, 0, len(array) - 1, element)
print(f"The given array is : {array}")
print(f"The element to be searched is : {element}")
if output != -1:
    print(f"Element is present at index {output}")
else:
    print("Element is not present in array")

########################################################################################################################

# Recursive Approach

def recursiveBinarySearch(array, l_index, r_index, element):
    # Checking for the base case
    if r_index >= l_index:

        mid_index = l_index + (r_index - l_index) // 2

        # At first we check if element is present at mid-index
        if array[mid_index] == element:
            return mid_index

        # We will ignore the right half of the array if the element is smaller than the mid-value
        elif array[mid_index] > element:
            return recursiveBinarySearch(array, l_index, mid_index - 1, element)

        # We will ignore the left half of the array if the element is greater than the mid-value
        else:
            return recursiveBinarySearch(array, mid_index+ 1, r_index, element)

    else:
        return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
element = 7

# Function call
output = recursiveBinarySearch(array, 0, len(array) - 1, element)
print(f"The given array is : {array}")
print(f"The element to be searched is : {element}")

if output != -1:
    print(f"Element is present at index {output}")
else:
    print("Element is not present in array")


########################################################################################################################
########################################################################################################################

# Estimate Pi using Srinivas Ramanujan infinite series

import math


def estimate_pi():
    k = 0
    summation = 1.0
    sigma = 0
    #iterating till the summation is not less than 10^-15
    while summation > 1e-15:
        summation = ((math.factorial(4 * k)) * (1103 + 26390 * (k))) / ((math.factorial(k) ** 4) * (396 ** (4 * k)))
        k += 1
        sigma += summation
    result = ((2 * math.sqrt(2)) / 9801) * sigma
    return 1 / result

print (f"Calculated value of pi using Ramanujan's equation is {estimate_pi()}")
print (f"Value of pi given by Math library: {math.pi}")

########################################################################################################################
########################################################################################################################

#Bubble sort implementation

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        print(f"Pass = {i+1}: ", end="\n")
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(arr, end="\n")
        print()
arr = [ 7,4,5,9,8,2,1]

bubbleSort(arr)


########################################################################################################################
########################################################################################################################

# Selection sort implementation

A = [7,4,5,9,8,2,1]

B = [10, 20, 30, 40 , 50 ,60 ,]
for i in range(len(A)):
    print(f"pass {i+1}: ", end="\n")
    min_idx = i
    for j in range(i + 1, len(A)):
        # print(f"current minimum : {A[min_idx]}")
        if A[min_idx] > A[j]:
            min_idx = j
        # print(f"Updated minimum: {A[min_idx]}")
    A[i], A[min_idx] = A[min_idx], A[i]
    print(f"{A} ", end="\n")
print()




