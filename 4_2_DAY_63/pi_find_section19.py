from math import factorial
from decimal import Decimal, getcontext
# Chudnovsky algorithm for figuring out pi


pi_input = input('How many digits of pi would you like?')
n = int(pi_input)

def cal(n):
    t= Decimal(0)
    val = Decimal(0)
    deno= Decimal(0)

    for k in range(n):
        t = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
        deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        val += Decimal(t)/Decimal(deno)
    pi = val * Decimal(12) / Decimal(640320 ** Decimal(1.5))
    pi = 1/pi
    return round(pi,n)

print(cal(n))