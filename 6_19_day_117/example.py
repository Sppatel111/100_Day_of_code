#
#
# list1=[1,2,3,4,1,3]
# seen=set()
# list2=[ i for i in list1 if not (i  in seen or seen.add(i))]
# print(list2)
#
# d1={'a':1,'b':2}
# d2={'c':3,'d':0}
#
# d1.update(d2)
# print(d1)
#
# d3=dict(sorted(d1.items(),key=lambda item:item[1],reverse=True))
# print(d3)

import pickle

# Example Python object (a dictionary)
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Pickling the object
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)  # Serialize and save to file

with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)  # Deserialize from file

print(loaded_data)