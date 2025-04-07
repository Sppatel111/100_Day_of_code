# Limit Calculator - Ask the user to enter f(x)
# and the limit value, then return the value of the limit statement
# Optional: Make the calculator capable of supporting infinite limits.

import sympy as sp

f=input("enter the function f(x):")
v=input(" enter the limit or for the infinity type 'y':").lower()

x=sp.symbols('x')
if v=='y':
    limit_result = sp.limit(f, x, sp.oo)
else:
    limit_result=sp.limit(f,x,int(v))

print(f"here you can see the result of {f} is {limit_result}")


