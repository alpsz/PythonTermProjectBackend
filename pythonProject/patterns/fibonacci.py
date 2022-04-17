n = 10
a = 0
b = 1

if (n == 0):
    print(0)
if (n == 1):
    print(1)

c = 1
n = n - 3
while (n > 0):
    c = a + b
    print(c)
    a = b
    b = c
    n = n - 1
print(c)
