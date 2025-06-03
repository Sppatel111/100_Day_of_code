# Pattern Printer
#
# Print patterns like pyramids, stars, numbers using loops and parameterized functions.

# def pyramid(n):
#     for i in range(1,n+1):
#         for j in range(n-i):
#             print('_',end='')
#
#         for k in range(2*i-1):
#             print('*',end='')
#         print()
#
# pyramid(5)


def pyramid(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(' ',end='')

        for k in range(1,2*i):
            print(i,end='')
        print()

pyramid(5)