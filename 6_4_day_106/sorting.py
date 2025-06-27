# Sorting Algorithm (e.g., Bubble Sort, Quick Sort)
#
# Implement sorting using functional approach.

#bubble sort

# def bubble(lst):
#     for i in range(len(lst)):
#         for j in range(len(lst)):
#             if lst[i] < lst[j]:
#                 temp = lst[i]
#                 lst[i]= lst[j]
#                 lst[j]=temp
#
#     return lst
#
# print(bubble([22,1,34,56,12]))


# quick sort
arr1=[1, 12, 5, 26, 7, 14, 3, 7, 2]


def quicksort(ar,left,right):
    arr=ar
    print(f'left:{left}')
    print(f'right:{right}')
    p= int((left+right)/2)
    print(p)
    i=left
    j=right
    print(i,j)

    #partition
    while i <= j:
        print(i,j)
        print('hey')
        while arr[i] < arr[p]:
            print('yes1')
            i+=1
            # print(i)
        while arr[j] > arr[p]:
            print('yes2')
            j-=1
            # print(j)
        # print(i,j)
        if i <= j:
            arr[i], arr[j]=arr[j],arr[i]
            i+=1
            j-=1
            print(f'arr:{arr}')

    # recursion
    if left < j:
        print('yeah')
        print('on left')
        quicksort(arr,left,j)

    if i < right:
        print('yeah')
        print('on right')
        quicksort(arr,i,right)
    print(arr)
    return arr

x=quicksort(arr1,0,len(arr1)-1)
print(x)




