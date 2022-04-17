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

# for i in range(len(arr)):
#     print("%d" % arr[i], end=" ")