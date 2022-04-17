#List and its functions
random_List = [1986, 2022, 1997, 2000] #creating a list of integers

random_List.append(20544) #appending a value to the list
print(random_List)

print(len(random_List)) #printing total number of elements in the list

print(random_List.index(1997)) #printing the index of a particular element of the list

random_List.insert(2,10087) #inserting an element in the list
print(random_List)

print(random_List.pop()) #pospping out the element from the list
print(random_List)

random_List.remove(2000) #removing an element from the list
print(random_List)

random_List.sort() #sorting the list
print(random_List)

random_List.reverse()#reversing the list
print(random_List)

random_List.clear()#removing all the elements from the list
print(random_List)

#tuples and its functions
random_tuple = (1, 5, 2)

print(len(random_tuple)) #printing total number of elements in the tuple

# set and its functions
random_set = {"apple", "orange", "grapes"} #creating a set
random_set.add("cherry") # adding a value to the set
print(random_set)

random_set.remove("orange") #removing a value from the set
print(random_set)

random_set.pop()# popping a value from the set
print(random_set)

random_set.clear() #removing all the elemenst from the set
print(random_set)

#dictionary and its functions
dict = {"name": 'Alpesh', "salary": 1234, "age": 23, "gender": "male"} #creating a dictionary
print(dict)

dict.pop("gender") # Removes the element with the specified key
print(dict)

print(dict.get("name")) #get the value with the specified key

print(dict.items()) #get all the key value pairs in form of tuples

print(dict.keys()) #list down all the keys of the dictionary

print(dict.values()) #list down all the value from the dictionary

dict.clear() #removing all the elements from the dictionary
print(dict)


#task 2

dict1 = {  # creating a dictionary
    1: 2.0,
    2: 2.1,
    3: 2.2
}

print(dict1)

dict1.update({4:2.3}) #adding key value pair to the dictionary
print(dict1)

#task3

random_tuple1 = (1, 2, 3)
print( list(random_tuple1) ) #type casting tuple to a list




