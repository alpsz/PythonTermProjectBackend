num = 97
n = 5
for i in range (0, n):
    for j in range (0, i+1):
        ch = chr(num)
        print(f"{ch} ", end="")
        num = num + 1
    print("\r")