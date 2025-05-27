# Palindrome Checker
# Checks if a given string or number is a palindrome.

def palindrome(str1):
    print(str1[::-1])
    return str1 == str1[::-1]

print(palindrome('123321'))