# Change Return Program - The user enters a cost and then the amount of money given. The program
# will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.
# price = float(input("Enter the price:"))
# paid = float(input(" enter the paid amount:"))
# print(price)
# print(paid)
# change = round(float(paid - price), 2)
# print(change)
# quarters = 0
# dimes = 0
# nickels = 0
# pennies = 0
#
# while change > 0.00:
#     if change >= .25:
#         change -= .25
#         quarters += 1
#     elif change >= .1:
#         change -= .1
#         dimes += 1
#     elif change >= .05:
#         change -= .05
#         nickels += 1
#     elif change >= .01:
#         change -= .01
#         pennies += 1
#
# print(quarters)
# print(dimes)
# print(nickels)
# print(pennies)

# Next Prime Number - Have the program find prime numbers until the user
# chooses to stop asking for the next one.

# num = int(input("Enter a positive number:"))
# def nextprime(n):
#     if n < 0:
#         raise ValueError
#     found_prime =False
#     for next1 in range(n + 1, n + 200):
#         if next1 > 1:
#             is_prime =True
#             for i in range(2, int(next1 **0.5)+1):
#                 if (next1 % i) == 0:
#                     is_prime =False
#                     break
#             if is_prime:
#                 print(next1)
#                 choice = input("do you want next prime number:type(Y/N):").upper()
#                 if choice != 'Y':
#                     return
#
# print(nextprime(num))


# Binary to Decimal and Back Converter - Develop a converter to convert a decimal
# number to binary or a binary number to its decimal equivalent.


# print(bin(3))
# print(int('111',2))
#
#
# converter =True
# while converter:
#     choice = input("Do you want to convert binary to decimal or decimal to binary ,type(BTOD,DTOB) or for exit type 'off':").upper()
#
#     if choice == 'BTOD':
#         n = input("enter the binary number:")
#         decimal=int(n,2)
#         print(f"the {n} of binary to decimal conversion is {decimal}")
#     elif choice == 'DTOB':
#         n = int(input("enter the decimal number:"))
#         binary=bin(n)
#         print(f" the {n} of decimal to binary conversion is {binary.split('b')[1]}")
#     elif choice == 'OFF':
#         converter =False
#     else:
#         print("invalid input..")
#         converter=False


# Calculator - A simple calculator to do basic operators.
# Make it a scientific calculator for added complexity.

# import math
# def add(a, b):
#     return a + b
#
#
# def mul(a, b):
#     return a * b
#
#
# def sub(a, b):
#     return a - b
#
#
# def div(a, b):
#     if b == 0:
#         return " should be non zero."
#     return a / b
#
#
# def square_root(a):
#     if a < 0:
#         return " should be greater than zero."
#     return math.sqrt(a)
#
#
# def power(a, b):
#     return a ** b
#
#
# def sine(a):
#     return math.sin(math.radians(a))
#
#
# def cosine(a):
#     return math.cos(math.radians(a))
#
#
# def tangent(a):
#     return math.tan(math.radians(a))
#
#
# def calculator():
#     print("Welcome to the Scientific Calculator!")
#     print("Select operation:")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Square Root")
#     print("6. Power")
#     print("7. Sine")
#     print("8. Cosine")
#     print("9. Tangent")
#     print("0. Exit")
#
#     while True:
#         choice = int(input("enter choice (0 for exit):"))
#
#         if choice in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#             n1 = float(input("enter number 1:"))
#         if choice in [1, 2, 3, 4, 6]:
#             n2 = float(input("enter number 2:"))
#
#         if choice == 1:
#             print(f"{n1} +{n2} = {add(n1, n2)}")
#         elif choice == 2:
#             print(f"{n1} -{n2} = {sub(n1, n2)}")
#         elif choice == 3:
#             print(f"{n1}  * {n2} = {mul(n1, n2)}")
#         elif choice == 4:
#             print(f"{n1} / {n2} = {div(n1, n2)}")
#         elif choice == 5:
#             print(f" square root of {n1} = {square_root(n1)}")
#         elif choice == 6:
#             print(f"{n1} power of {n2} = {power(n1, n2)}")
#         elif choice == 7:
#             print(f" sine of {n1} = {sine(n1)}")
#         elif choice == 8:
#             print(f" cosine of {n1}  = {cosine(n1)}")
#         elif choice == 9:
#             print(f" tangent of {n1}= {tangent(n1)}")
#         elif choice == 0:
#             break
#         else:
#             print(" incorrect input!!")
#
# calculator()

# Unit Converter (temp, currency, volume, mass and more) - Converts various units between one another.
# The user enters the type of unit being entered, the type of unit they want to convert to and then the value.
# The program will then make the conversion.

def calculation():
    option= input(" do you want to convert units.??\n for weight or length? type (W/L):").upper()
    if option == 'W':
        print("units kg,g,mg")
        unit1=input("which unit you want to convert from??:").lower()
        unit2=input("which unit you want to convert ??:").lower()
        n =float(input("enter number:"))

        if unit1 =='kg' and unit2 =='g':
            n1= n * 1000
            print(f" {n} kg = {n1} g")
        elif unit1 == 'kg' and unit2 == 'mg':
            n1 = n * 1000000
            print(f" {n} kg = {n1} mg")
        elif unit1 == 'g' and unit2 == 'kg':
            n1 = n / 1000
            print(f" {n} g = {n1} kg")
        elif unit1 == 'g' and unit2 == 'mg':
            n1 = n * 1000
            print(f" {n} g = {n1} mg")
        elif unit1 == 'mg' and unit2 == 'g':
            n1 = n / 1000
            print(f" {n} mg = {n1} g")
        elif unit1 == 'mg' and unit2 == 'kg':
            n1 = n / 1000000
            print(f" {n} mg = {n1} kg")
        else:
            print("incorrect input!! use above given units!")

    elif option == 'L':
        print("units m,cm,mm,km")
        unit1 = input("which unit you want to convert from??:").lower()
        unit2 = input("which unit you want to convert ??:").lower()
        n = float(input("enter number:"))
        if unit1 == "cm" and unit2 == "m":
            ans = n / 100
            print(f" {n} cm = {ans} m")
        elif unit1 == "cm" and unit2 == "mm":
            ans = n * 10
            print(f" {n} cm = {ans} mm")
        elif unit1 =="cm" and unit2 == "km":
            ans =n /100000
            print(f" {n} cm = {ans} km")
        elif unit1 == "mm" and unit2 == "cm":
            ans = n / 10
            print(f" {n} mm = {ans} cm")
        elif unit1 == "mm" and unit2 == "m":
            ans = n / 1000
            print(f" {n} mm = {ans} m")
        elif unit1 == "mm" and unit2 == "km":
            ans = n / 1000000
            print(f" {n} mm = {ans} km")
        elif unit1 == "m" and unit2 == "cm":
            ans = n * 100
            print(f" {n} m = {ans} cm")
        elif unit1 == "m" and unit2 == "mm":
            ans = n * 1000
            print(f" {n} m = {ans} mm")
        elif unit1 == "m" and unit2 == "km":
            ans = n / 1000
            print(f" {n} m = {ans} km")
        elif unit1 == "km" and unit2 == "m":
            ans = n * 1000
            print(f" {n} km = {ans} m")
        elif unit1 ==  "km" and unit2 == "cm":
            ans = n * 100000
            print(f" {n} km = {ans} cm")
        elif unit1 == "km" and unit2 == "mm":
            ans = n * 1000000
            print(f" {n} km = {ans} mm")
    else:
        print("invalid input option")

calculation()
