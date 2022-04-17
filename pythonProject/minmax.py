def minmax1 (x):
    # this function fails if the list length is 0
    minimum = maximum = x[0]
    for i in x[1:]:
        if i < minimum:
            minimum = i
        else:
            if i > maximum: maximum = i
    return (minimum,maximum)



print(minmax1([9,8,7,6,5,4,3,2,1,11,12,13,14,15,16,17,18,19]))
print(minmax1([1]))
print(minmax1([2, 0, 2, 7, 5, -1, -2]))