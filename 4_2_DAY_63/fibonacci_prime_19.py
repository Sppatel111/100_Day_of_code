## fibonacci
# def fibo(n):
#     list1 = []
#     a = 0
#     b = 1
#     for _ in range(n):
#         list1.append(a)
#         a,b=b,a+b
#     return list1
#
# n=int(input("enter the number:"))
# print(fibo(n))


## prime number factorization
def prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(n**0.5) + 1,2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2:
        factors.append(n)
    return factors

number = int(input("Enter a number: "))
factors = prime_factors(number)
print(f"Prime factors of {number} are: {factors}")








