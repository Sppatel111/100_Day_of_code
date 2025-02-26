# from collections import Counter
#
# mylist=[1,1,1,1,2,3,4,5,6,7,3,4,5,6,]
#
# print(Counter(mylist))
#
# mylist2=[1,'a','a',1,4,11]
# print(Counter(mylist2))
#
# c=Counter('aaaaaagfffffggddgx')
# print(c)
# print(c.most_common())
# print(list(c))
# se=" How many Time Words are shown!!"
# y=Counter(se)
#
# print(y)
# x=Counter(se.lower().split())
# print(x)

# from collections import defaultdict
#
# d=defaultdict(lambda :0)
# d['correct']=100
# print(d['correct'])
# print(d["wrong key"])
#
# from collections import namedtuple
#
# Dog=namedtuple('Dog',['name','age'])
#
# sam=Dog(age=5,name='sammy')
#
# print(sam)
# print(sam[0])
# print(sam.age)

import os
#
# print(os.getcwd())
# print(os.listdir('D:/SNEHA1/100_Day_of_code'))

# import shutil
# shutil.move('text_file.txt','D:/SNEHA1/100_Day_of_code/exmp')
# shutil.move('tex2.txt','D:/SNEHA1/100_Day_of_code/exmp')

# for folder,sub_folder,file in os.walk('D:/SNEHA1/100_Day_of_code/2_26_DAY_39'):
#     print(f"folder:{folder}")
#     for sub_fol in sub_folder:
#         print(f"sub folder: {sub_fol}")
#
#     for f in file:
#         print(f"files:{f}")

# import send2trash
#
# send2trash.send2trash("trash.txt")
#

# import random
#
# mylist=[i for i in range(0,20)]
# print(mylist)
#
# #with replacement
# print(random.choices(population=mylist,k=10))
#
# #without replacement
# print(random.sample(population=mylist,k=10))


# import pdb
#
# x = [1, 2, 3]
# y = 2
# z = 8
# result1 = y + z
#
# pdb.set_trace()
#
# result2 = x + y


# import re
# text="my phone number is phone:408-335-4347"
#
# phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
# phone2 = re.search(r"\d{3}-\d{3}-\d{4}",text)
# print(phone.group())
# print(phone2.group())
#
# phone_pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
# phone3=re.search(phone_pattern,text)
# print(phone3.group(3))
#
# find=re.findall("phone",text)
# print(find)
#
# cd=re.search(r'cat|dog','the cat is here')
# print(cd)
#
# f1=re.findall(r'.at','the cat in the hat sat there.')
# print(f1)
#
# f1=re.findall(r'\s+at','the cat in the hat sat there.')
# print(f1)
#
# phrase = "there are 3 numbers 34 inside 5 this sentence."
# x=re.findall(r'[^\d]+',phrase)
# print(x)
#
# test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
# y=re.findall('[^!.? ]+',test_phrase)
# print(y)
#
# text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
# z=re.findall(r'[\w]+-[\w]+',text)
# print(z)

# text = 'Hello, would you like some catfish?'
# texttwo = "Hello, would you like to take a catnap?"
# textthree = "Hello, have you seen this caterpillar?"
#
# x=re.search(r'cat(fish|nap|erpillar)',textthree)
# print(x.group())


# def func_one(n):
#     return [str(num) for num in range(n)]
#
# import time
# start_time = time.time()
# result = func_one(1000000)
# end_time=time.time()
# e_time = end_time - start_time
#
# print(e_time)

# def func_two(n):
#     return list(map(str,range(n)))
#
# import time
# start_time = time.time()
# result2 = func_two(1000000)
# end_time=time.time()
# e2_time = end_time- start_time
#
# print(f"two: {e2_time}")


# f1=open("text2.txt","w+")
# f1.write("One file")
# f1.close()

# import zipfile
#
# comp_file=zipfile.ZipFile('comp_zip_file.zip','w')
# comp_file.write('text2.txt',compress_type=zipfile.ZIP_DEFLATED)
# comp_file.close()
#
# zip_obj=zipfile.ZipFile('comp_zip_file.zip','r')
# zip_obj.extractall('exmp')

import shutil

shutil.make_archive("example","zip","D:/SNEHA1/100_Day_of_code/2_26_DAY_39/exmp")

shutil.unpack_archive('example.zip','finalunzip',)