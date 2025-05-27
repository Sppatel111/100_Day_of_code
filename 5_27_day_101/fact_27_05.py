# Factorial Calculator (Recursive and Iterative)
#
# Returns the factorial of a number using both methods.

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return fact(n-1) * n
# num=int(input('enter number:'))
# print(fact(num))

def fact1(n):
    temp=1
    for i in range(1,n+1):
        temp *=i
    return temp

print(fact1(5))
