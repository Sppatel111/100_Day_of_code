# class Dog():
#     species = "mammal"
#     def __init__(self,breed,spots,name):
#         self.breed1=breed
#         self.spots1=spots
#         self.name1=name
#
#     def bark(self,number):
#         print("WOOF!! my name is {} and number is {}.".format(self.name1,number))
#
# my_dog=Dog(breed='Lab',spots=False,name="sammy")
#
# print(type(my_dog))
#
# print(my_dog.breed1)
# print(my_dog.species)
# print(my_dog.spots1)
# my_dog.bark(11)

# class Circle():
#
#     pi=3.14
#     def __init__(self,radius=1):
#         self.radius=radius
#         self.area=radius*radius*Circle.pi
#
#     def circumference(self):
#         return self.radius * Circle.pi * 2
#
# value=Circle(10)
# print(value.pi)
# print(value.radius)
# print(value.area)
#
# print(value.circumference())


# inheritiance

# class Animal:
#     def __init__(self):
#         print("animal class created.")
#
#     def who_am_i(self):
#         print("i am animal")
#
#     def eat(self):
#         print("i am eating")
#
#
# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print("dog created")
#
#     def who_am_i(self):
#         print(" iam dog.")
#
#     def eat(self):
#         print("i am dog and eating")
#
#
# my_dog = Animal()
# my_dog.who_am_i()
# my_dog.eat()
#
# my_dog2 = Dog()
# my_dog2.who_am_i()
# my_dog2.eat()

# polymorphism

# class Dog:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         return f"{self.name} speaks Woof-woof!!"
#
# class Cat:
#     def __init__(self,name):
#         self.name=name
#
#     def speak(self):
#         return f"{self.name} specks meow-meow!!"
#
# dog=Dog("jony")
# print(dog.speak())
#
# cat=Cat("chemy")
# print(cat.speak())
#
# for pet in [dog,cat]:
#     print(type(pet))
#     print(type(pet.speak()))
#
#
# def pet_speak(pet):
#     print(pet.speak())
#
# pet_speak(dog)

####
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         pass
#         # raise NotImplementedError("subclass must implemented this error.")
#
# a=Animal("jex")
# a.speak()
#
# class Dog(Animal):
#
#     def speak(self):
#         return self.name +"say woof!!"
#
# class Cat(Animal):
#     def speak(self):
#         return self.name +" say meow!!"
#
# jery=Dog("Jery")
# print(jery.speak())
#
# temy=Cat("Temy")
# print(temy.speak())


# class Book:
#     def __init__(self,title,auther,pages):
#         self.title=title
#         self.auther=auther
#         self.pages=pages
#
#     def __str__(self):
#         return f"title:{self.title}, auther:{self.auther} pages:{self.pages}"
#
#     def __len__(self):
#         return self.pages
#
#     def __del__(self):
#         print("A book object has been deleted.")
#
# b=Book("Python rocks","jose",2000)
#
# print(b)
# print(str(b))
# print(len(b))
#
# del b
#
# try:
#  print(b)
# except NameError as e:
#     print(e)

# class Line:
#
#     def __init__(self, coor1, coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2
#
#     def distance(self):
#         x1, y1 = self.coor1
#         x2, y2 = self.coor2
#
#         return (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
#
#     def slop(self):
#         x1, y1 = self.coor1
#         x2, y2 = self.coor2
#
#         return (y2 - y1) / (x2 - x1)
#
# c1=(2,3)
# c2=(4,5)
# line = Line(c1, c2)
# print(line.distance())
# print(line.slop())


# class Cylinder:
#     def __init__(self,height=1,radius=1):
#         self.height=height
#         self.radius=radius
#     def volume(self):
#         return self.height * 3.14 * (self.radius **2)
#     def surface_area(self):
#         top = 3.14 * (self.radius **2)
#         return (2*top) + 2 * 3.14 * self.radius * self.height
#
# c=Cylinder(20,20)
#
# print(c.volume())
# print(c.surface_area())

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amount):
        self.balance = self.balance + dep_amount
        print(f" the deposit amount {dep_amount} is done.")

    def withdrawal(self, wit_amount):

        if self.balance >= wit_amount:
            self.balance = self.balance - wit_amount
            print(f" the Withdrawal amount {wit_amount} is done.")

        else:
            return "Not enough money to withdraw"

    def __str__(self):
        return f" Owner :{self.owner} and the Balance:{self.balance}"


a = Account("joshep", 100000)

print(a.balance)
a.deposit(300)
print(str(a))

a.withdrawal(500)
print(str(a))
