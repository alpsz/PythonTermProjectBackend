n = 5
for i in range(0 ,n):
    for j in  range(1, n+1):
        if(j < n - i):
            print("  ", end="")
        else:
            print("* ", end="")
    print("\r")
