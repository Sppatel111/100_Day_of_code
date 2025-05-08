import numpy as np




# print(np.__version__)
#
# print(type(arr))

arr1=np.array((6,7,8,9))
# print(arr1)
# print(type(arr1))

##
arrx=np.array([{1:'x',2:'y',3:'z'}])
# print(arrx)
# print(arrx[0][2])

##
data = np.array([
    {'x': 1, 'y': 2.0, 'z': 'Hello'},
    {'x': 2, 'y': 3.0, 'z': 'World'}
])
# print(data)
# print(data[0]['x'])

##
dict={1:'x',2:'y',3:'z'}
arr2=np.array(list(dict.items()))
# print(arr2)
# print(type(arr2))
# print(arr2[1])
# print(arr2[1][1])

## 0 dim
num=np.array(11)
# print(num)

arr=np.array([1,2,3,4,5])
print(arr)

# 2 dim
d2=np.array([[1,2,3],[2,3,4],[7,8,9]])
print(d2)
# print(type(d2))

# 3 dim
d3=np.array([ [ [1,2,3],[4,5,6] ], [ [6,7,8],[11,10,9] ] ])
print(d3)
# print(type(d3))

# print(num.ndim)
# print(arr.ndim)
# print(d2.ndim)
# print(d3.ndim)


a=np.array([1,2,3,4,5,6,7],ndmin=5)
# print(a)

# print(arr[0]+arr[1])

## indexing
# print(d2[1])
# print(d2[1,1])
#
# print(d3)
# print(d3[0])
# print(d3[0,0,1])


## Slicing

# print(arr[2:7])
# print(arr[-3:-1])
# print(d2[0,1:4])

# print(d2[0:3,2])
# print(d2[0:3,1:3])

print(d3[1,0,0:2])
print(d2.dtype)

# d=np.array([1,2,6,7,9,'abcv'],dtype='S')
# print(d.dtype)

d=np.array([1,2,6,7,9],dtype='i')
print(d.dtype)