#Fibonacci Series Generator
#Generate n Fibonacci numbers using recursion or iteration.

num=int(input("enter number:"))

list1=[]
def fibbo(n):
    a = 0
    b = 1
    list1.append(a)
    list1.append(b)
    for _ in range(n-2):
        c=a+b
        list1.append(c)
        a,b=b,c

    return list1

print(fibbo(num))
