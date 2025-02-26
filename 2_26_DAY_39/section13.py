# def create_cub(n):
#     result=[]
#     for x in range(n):
#         result.append(x**3)
#
#     return result
#
# for x in create_cub(10):
#     print(x)
#

#generator: it is similar to normal function to define but instend of return statemet we use yield.
# yeild statement produce value of generator.
#using yield

# def create_cub(n):
#     for x in range(n):
#         yield x**3
#
# for x in create_cub(10):
#     print(x)

# def generate_fibon(n):
#     a=1
#     b=1
#     for i in range(n):
#         yield a
#         a,b =b,a+b
#
# for i in generate_fibon(10):
#     print(i)
#
# def generator_1(n):
#     value=1
#
#     while value <= n:
#         yield value
#         value +=1
#
# for i in generator_1(10):
#     print(i)

# def non_generator(n):
#     value=1
#     list1=[]
#     while value <=n:
#         list1.append(value)
#         value+=1
#     return list1
#
# for i in non_generator(10):
#     print(i)

# def simple():
#     for i in range(3):
#         yield i
#
# x=simple()
# print(next(x))
# print(next(x))
# print(next(x))

# import random
#
# def random_1(low,high,n):
#     for i in range(n):
#         yield random.randint(low,high)
# for i in random_1(1,10,11):
#     print(i)


# use iterator
# string="hello"
# s=iter(string)
# for i in range(len(string)):
#     print(next(s))


def func():
    for i in range(1,11):
        yield i

x=func()
for i in x:
    print(i)