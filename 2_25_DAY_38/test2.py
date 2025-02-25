
n=int(input("enter input value :"))
for i in range(1,n+1):
    for j in range(1,i):
        print(j,end='')
    print("\r")

for i in range(n+1,1,-1):
    for j in range(1,i):
        print(j,end='')
    print('\r')

