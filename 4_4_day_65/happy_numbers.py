# Happy Numbers - A happy number is defined by the following process. Starting withany positive integer,
# replace the number by the sum of the squares of its digits,and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers,
# while those that do not end in 1 are unhappy numbers.
# Display an example of your output here.Find first 8 happy numbers.



## for find happy number by input
# n = int(input("Enter number:"))
#
# def happy_check(n):
#     if n == 1:
#         return f" {n} is happy number."
#     elif n > 1:
#         if n < 9:
#             n =n ** 2
#             while True:
#                 sum1 = 0
#                 for i in str(n):
#                     sum1 += int(i) ** 2
#                 print(sum1)
#                 n=sum1
#                 if n == 1:
#                     return f" it is happy number."
#                 elif n == 4:
#                     return f"it is unhappy number"
#                 else:
#                     continue
#         else:
#             while True:
#                 sum1 = 0
#                 for i in str(n):
#                     sum1 += int(i) ** 2
#                 print(sum1)
#                 n = sum1
#                 if n == 1:
#                     return f" it is happy number."
#                 elif n == 4:
#                     return f"it is unhappy number"
#                 else:
#                     continue
#
#     else:
#         print("enter valid positive number")
#
#
# print(happy_check(n))

## first 8 happy number
def happy():
    list1=[]
    for i in range(1,100):
        n=i
        while True:
            sum1 = 0
            for j in str(n):
                sum1 += int(j) ** 2
            n = sum1
            if n == 1:
                list1.append(i)
                break
            elif n == 4:
                break
            else:
                continue
        if len(list1)== 8:
            break
    return list1

print(happy())