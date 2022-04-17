str = "racecar"

def palindrome(s):
    return s == s[::-1]

print(palindrome(str))