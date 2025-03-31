import csv

import PyPDF2
import re

# f=open('Working_Business_Proposal.pdf','rb')
#
# pdf_reader=PyPDF2.PdfReader(f)
#
# print(len(pdf_reader.pages))
#
# page_one=pdf_reader.pages[0]
#
# page_one_text=page_one.extract_text()
#
# print(page_one_text)
#
# f.close()


### write into another file pf first page of above file .
# f=open('Working_Business_Proposal.pdf','rb')
#
# pdf_reader=PyPDF2.PdfReader(f)
#
# first_page=pdf_reader.pages[0]
#
# pdf_writer=PyPDF2.PdfWriter()
#
# pdf_writer.add_page(first_page)
#
# pdf_output=open('Some_BrandNew_Doc.pdf','wb')
#
# pdf_writer.write(pdf_output)
#
# f.close()
#
# pdf_output.close()


###
# f=open('Working_Business_Proposal.pdf','rb')
#
# pdf_text=[]
#
# pdf_reader=PyPDF2.PdfReader(f)
#
# for num in range(len(pdf_reader.pages)):
#     page = pdf_reader.pages[num]
#     pdf_text.append(page.extract_text())
#
# print(pdf_text)
# f.close()

### find link

# data = open('find_the_link.csv',encoding='utf-8')
# csv_data = csv.reader(data)
#
# data_lines =list(csv_data)
#
# print(data_lines)
#
# link_str = ''
#
# for row_num, data in enumerate(data_lines):
#     link_str += data[row_num]
#
# print(link_str)


### find number

f = open('Find_the_Phone_Number.pdf', 'rb')

pdf = PyPDF2.PdfReader(f)

print(len(pdf.pages))

pattern = r'\d{3}.\d{3}.\d{4}'

all_text = ''

for n in range(len(pdf.pages)):
    page = pdf.pages[n]
    page_text = page.extract_text()
    all_text += all_text + ' ' + page_text

x=re.findall(pattern, all_text)
print(x)

for match in re.finditer(pattern,all_text):
    print(match)

# num = all_text[389610982 : 389610986+20]
# print(num)

##after find out pattern change in the pattern according