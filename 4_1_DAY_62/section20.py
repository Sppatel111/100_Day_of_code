## hex,binary

# print(hex(20))
#
# print(bin(1234))

#power
# print(2 ** 4)
#
# print(pow(2,4))
#
# print(pow(2,4,3))

#absult
# print(abs(-3))
#
# print(abs(2))

#round
# print(round(3.1))
#
# print(round(3.9))
#
# print(round(-3.1))
#
# print(round(-3.9))
#
# print(round(3.1425345,2))

## string
# s='Hello world'

# print(s.capitalize())
# print(s.lower())
# print(s.upper())
# print(s.count('o'))
# print(s.find('o'))
# print(s.center(20,'z'))
# print('hello\thi')
# print('hello\thi'.expandtabs())

# s1='hello'
# print(s1.isalnum())
# print(s1.islower())
# print(s1.isupper())
# print(s1.isalpha())
# print(s1.isspace())
# print(s1.istitle())
# print(s1.endswith('o'))
# print(s1[-1] == 'o')
# print(s1.split('e'))

# s2='hihhihihiih'
# print(s2.split('i'))
# print(s2.partition('i'))

## sets

s3 =set()
s3.add(1)
s3.add(2)
s3.add(1)

# s3.clear()
# print(s3)

sc=s3.copy()
s3.add(4)
print(s3)
print(sc)

print(s3.difference(sc))

s1={1,2,3}
s2={1,4,5}
s4={5}

# print(s1.difference(s2))
# s1.difference_update(s2)
# print(s1)
# print(s2)

# s3.discard(5)
# print(s3)
#
# print(s1.intersection(s2))
#
# s1.intersection_update(s2)
# print(s1)



# print(s1.isdisjoint(s2))
# print(s1.isdisjoint(s4))

# print(s1.issubset(s2))
# print(s4.issubset(s2))

# print(s1.symmetric_difference(s2))
# s1.symmetric_difference_update(s2)
# print(s1)

# print(s1.union(s2))

## extend
# s1.update(s2)
# print(s1)


## dictionaries

# d={'k1':1,'k2':2}

#dict comprehension

# d1={x:x**2 for x in range(10)}
# print(d1)
#
# d2={k:v  for k,v in zip(['a','b'],range(2))}
# print(d2)


# for i in d.items():
#     print(i)
#
# for i in d.keys():
#     print(i)
#
# for i in d.values():
#     print(i)

## list

l=[1,2,3]
l.append(4)
print(l.count(3))

# l.append([4,5])
l.extend([4,5])
print(l)

print(l.index(4))

l.insert(4,7)
print(l)

l.pop()
print(l)
l.pop(3)
print(l)

l.remove(4)
l.reverse()
l.sort()
print(l)

## test

1.
print(bin(1024))
print(hex(1024))

2.

print(round(5.23222,2))

3.
s = 'hello how are you Mary, are you feeling okay?'
print(s.islower())

4.
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))

5.
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

print(set1.difference(set2))

6.
print(set1.union(set2))

7.
d={ x:x**3 for x in range(5)}
print(d)

8.
list1 = [1,2,3,4]
list1.reverse()
print(list1)
9.
list2 = [3,4,2,5,1]
list2.sort()
print(list2)