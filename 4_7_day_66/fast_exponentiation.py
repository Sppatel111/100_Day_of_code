# Fast Exponentiation - Ask the user to enter 2 integers a and b and output a^b
# (i.e. pow(a,b)) in O(lg n) time complexity.

# import time
# start_time = time.time()
# print("for the n1^n2:")
# n1=int(input("enter the n1:"))
# n2=int(input("enter the n2:"))
#
# result=n1 **n2
# # result=pow(n1,n2)
# print(result)
# print("time elapsed: {:.2f}s".format(time.time() - start_time))

def fast_exponent(a,b):
    result =1
    base = a

    while b >0:
        if b % 2 ==1:
            result *= base

        base *=base
        b //=2

    return result

a = int(input("Enter the base (a): "))
b = int(input("Enter the exponent (b): "))

result=fast_exponent(a,b)

print(f"{a}^{b} = {result}")