# Find GCD and LCM of Two Numbers
#
# Functions to find GCD (Euclidean method) and LCM using GCD.

#Euclidean basic method
x = int(input('enter number 1:'))
y = int(input('enter number 2:'))


def gcd(a, b):
    print(a)
    print(b)
    if b == 0:
        return a

    return gcd(b, a % b)


gcd1 = gcd(max(x, y),min(x,y))

print(gcd1)


def lcm(a, b, gcd1):
    lcm = (a * b) / gcd1
    return lcm


print(lcm(x,y, gcd1))
