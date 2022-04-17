num = 65
n = 5
for i in  range (0, n):
    ch = chr(num)
    for j in range (0, i+1):
        print(f"{ch} ", end="")
    num = num + 1
    print("\r")
