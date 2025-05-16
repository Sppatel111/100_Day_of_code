
# s1=input('enter string1:').lower()
# s2=input('enter string2').lower()
# def ngramstring(s1,s2):
#
#     x=sorted(s1)
#     y=sorted(s2)
#     print(sorted(s1))
#     if len(s1) == len(s2):
#
#         string1=''
#         string2=''
#         for i in x:
#             string1 += i
#         for j in y:
#             string2 +=j
#
#         if string1==string2:
#             return True
#         else:
#             return False
#     else:
#         return False
#
#
# print(ngramstring(s1,s2))

# only by list
# list1=[]
# list2=[]
# for i in s1:
#     list1.append(i)
# for j in s2:
#     list2.append(j)
#
# if len(s1)== len(s2):
#     for i in range(len(list1)):
#         i=0
#         for j in range(len(list2)):
#             print(i)
#             print(j)
#             if list1[i] == list2[j]:
#                 list1.pop(i)
#                 list2.pop(j)
#                 print(list1)
#                 print(list2)
#                 break
#     if len(list1) == 0:
#         print('true')
#     else:
#         print('false')
#
# else:
#     print('false')

# s1 = 'race'
# s2 = 'care'
#
# l1 = [i for i in s1]
# l2 = [i for i in s2]
#
# print(l1)
# l1.sort()
#
# l2.sort()
# print(l1)
# print(l2)
#
# if l1 == l2:
#     print("True")
# else:
#     print("false")


# list1=[1,5,11,3]
# list1.sort()
# print(list1)


n=0
while n>10:
    print(n)