# def hello(name='jose'):
#     print("here inside hello() method.")
#
#     def greet():
#         print("inside greet function.")
#
#     greet()
#
#
# hello()
# greet()

# def hello(name='jose'):
#     print("here inside hello() method.")
#     def greet():
#         return "inside greet function."
#     def welcome():
#         return "inside welcome function."
#     if name == 'jose':
#         return greet
#     else:
#         return welcome
#
#
#
# dec1=hello('jose')
# print(dec1())

# def hello():
#     return " hi!!!"
#
# def other(any_func):
#     print("other function have function argument.")
#     return (any_func())
#
# print(other(hello))


def new_decorator(any_function):
    def wrap_fun():
        print(" some extra code...")
        any_function()
        print(" some extra code...")

    return wrap_fun


# def func_need_decorator():
#     print(" i want decorator")
#
# decorator1=new_decorator(func_need_decorator)
# decorator1()

@new_decorator
def func_need_decorator():
    print(" i want decorator")


func_need_decorator()

# def add(a,b):
#     return a+b
#
# def calculation(ope_fun,n1,n2):
#     return ope_fun
#
# addition=calculation(add,1,2)
# add
# generator:IT ALLOWED YOU WRITE FUNCTION THAT CAN SEND BACK VALUE  AND
