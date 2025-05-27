# Calculator (Add, Subtract, Multiply, Divide)
# Separate functions for each arithmetic operation.

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    if b != 0:
        return a/b
    else:
        return 'b should be non zero'

dict1= {'+':add,'-':sub,'*':multi,'/':div}
# dict1= {add:'+',sub:'-',multi:'*',div:'/'}
def calculate():
    global answer
    print("Calculator !!")
    cal=True
    while cal:
        ask=input('do you want to calculate (y/n):').lower()
        if ask== 'y':
            operation = input("enter operation (+,-,*,/):")
            a=int(input('enter n1:'))
            b=int(input('enter n2:'))

            if operation == '+':
                answer=dict1['+'](a,b)

            elif operation == '-':
                answer=dict1['-'](a,b)

            elif operation == '*':
                answer=dict1['*'](a,b)

            elif operation == '/':
                answer = dict1['/'](a, b)
            else:
                print('invalid input')
            print(f' {a} {operation} {b} = {answer}')
        elif ask == 'n':
            cal=False
        else:
            print('invalid input')

calculate()