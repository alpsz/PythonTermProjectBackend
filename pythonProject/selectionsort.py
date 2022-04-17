# import sys

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

# for i in range(len(A)):
#     print("%d" % A[i], end=" ")