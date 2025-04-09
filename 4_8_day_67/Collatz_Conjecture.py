# Classic Algorithms
# Collatz Conjecture - Start with a number n > 1. Find the number of steps it
# takes to reach one using the following process:
# If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

def collatz_steps(n):
    if n <= 1:
        print("it should be greater than 1")

    steps=0
    while n != 1:
        if n % 2 == 0:
            n= n //2
        else:
            n=3 * n + 1
        steps +=1
    return steps

print(collatz_steps(6))

