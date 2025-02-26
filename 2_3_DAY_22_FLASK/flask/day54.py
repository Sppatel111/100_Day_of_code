# python decorator
# it is function which wrapped another function and give some additional functionality
# or modification functionality.

#prerequsites for learning decorator
## pass function as argument
# def add(a, b):
#     return a + b
#
# def sub(a, b):
#     return a - b
#
# def mul(a, b):
#     return a * b
#
# def div(a, b):
#     return a / b
#
# def calculate(cal_operation, n1, n2):
#     return cal_operation(n1,n2)
#
# r=calculate(mul, 2, 3)
# print(r)


## nested function , return function as value
def outer_fun():
    print("i ma outer")
    def inner_fun():
        print("I am inner")

    return inner_fun

nested=outer_fun()
nested()


# now decorater in two ways like,
# import time
# def delay_decorator(func):
#     def wrapper():
#         time.sleep(2)
#         func()
#     return wrapper
#
# def hello():
#     print("hi")
# decorator1=delay_decorator(hello)
# decorator1()
#
# @delay_decorator
# def bye():
#     print("ok bye!")
# bye()
#
