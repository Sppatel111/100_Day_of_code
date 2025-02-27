import zipfile

# comp_file=zipfile.ZipFile("unzip_me_for_instructions.zip","r")
# comp_file.extractall()

import re

# pattern= r'\d{3}-\d{3}-\d{4}'

def search(file,pattern=r'\d{3}-\d{3}-\d{4}'):
    f=open(file,'r')
    text=f.read()

    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return ''

import os

result=[]
print(os.getcwd()+'\\extracted_content')

for folder,sub_folder,files in os.walk(os.getcwd()+'\\extracted_content'):
    for f in files:
        full_path=folder+'//'+f
        result.append(search(full_path))

print(result)
for  r in result:
    if r != '':
        print(r.group())
