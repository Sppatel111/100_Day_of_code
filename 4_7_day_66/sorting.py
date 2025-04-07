# Sorting - Implement two types of sorting algorithms: Merge sort and bubble sort.

## bubble sort
# list1=[]
# print("enter the list for sorting:")
#
# for i in range(100):
#     type = input(" type 'y' for insert element and 'n' for end insert:").lower()
#     if type =='y':
#        list1.append(int(input("enter input:")))
#     else:
#         break

# list1=[23,4,67,1]
# print(list1)
#
# for i in range(len(list1)):
#     for j in range(i+1,len(list1)):
#         if list1[i] > list1[j]:
#             temp=list1[i]
#             list1[i]=list1[j]
#             list1[j]=temp
#
# print(list1)


## merge sort
list2 = [23, 4, 67, 1]
print(list2)


def mergesort(list1):
    if len(list1) > 1:
        r = len(list1) // 2
        l = list1[:r]
        m = list1[r:]

        mergesort(l)
        mergesort(m)
        i = j = k = 0

        while i < len(l) and j < len(m):
            if l[i] < m[j]:
                list1[k] = l[i]
                i += 1
            else:
                list1[k] = m[j]
                j += 1
            k += 1

        while i < len(l):
            list1[k] = l[i]
            i += 1
            k += 1

        while j < len(m):
            list1[k] = m[j]
            j += 1
            k += 1
            print(list1)


mergesort(list2)


