#Write a Python program to read an entire text file.
# f=open("text_file.txt","r")
# data=f.read()
# print(data)
# f.close()

#Write a Python program to append text to a file and display the text
# f=open("text_file.txt","a")
# f.write("\ni am writing")
# f.close()
# f=open("text_file.txt","r")
# data=f.read()
# print(data)
# f.close()

#Write a Python program to copy the contents of a file to another file.
# f=open("text_file.txt","r")
# data=f.read()
# f.close()
# f1=open("tex2.txt","w")
# f1.write(data)
# f1.close()

#Write a Python program that takes a text file as input and returns the number of words of a given text file.

# f=open("text_file.txt","r")
# data=f.read()
# print(data)
# words=data.split()
# print(len(words))

#. Write a Python program to get the file size of a plain file.

import os
file="text_file.txt"
x=os.path.getsize(file)
print(x)