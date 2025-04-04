# Factorial Finder - The Factorial of a positive integer, n, is defined
# as the product of the sequence n, n-1, n-2, ...1 and the factorial of zero,
# 0, is defined as being 1. Solve this using both loops and recursion.

n = int(input("enter the number of factorial you want!! :"))
#loop
def factorial(n):
    fact=1
    if n == 0:
        return fact
    if n < 0:
        return " enter positive number."
    while n > 0:
        fact = fact * n
        n -= 1
        if n <= 0:
            break
    return fact

## using recursion

# def factorial(n):
#     fact = 0
#     if n > 0:
#         fact = n * factorial(n-1)
#     elif n == 0:
#         fact = 1
#     else:
#         print("not valid !!")
#     return fact

print(factorial(n))


