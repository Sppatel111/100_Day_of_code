import bs4
import requests

# result = requests.get("https://example.com/")
# print(result.text)
#
# soup=bs4.BeautifulSoup(result.text,"lxml")
#
# #title
# title=soup.select('title')
# ptag=soup.select('p')
# h1=soup.select('h1')
#
# print(title[0].getText())
# print(ptag[0].getText())
# print(h1[0].getText())

#class

# result = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
# soup=bs4.BeautifulSoup(result.text,"lxml")
# # print(soup)
#
# text1=soup.select('.vector-toc-text')
# # print(text1)
#
# for i in text1:
#     print(i.getText())


# first_item=text1[0].getText()
# print(first_item)

##image

# result = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
# soup=bs4.BeautifulSoup(result.text,"lxml")
#
# image=soup.select('img')[0]
# print(image)
#
# computer=soup.select('.mw-file-element')[1]
# print(computer['src'])
#
# image_link=requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/250px-Deep_Blue.jpg")
# print(image_link.content)
#
# f=open("my_computer.jpg",'wb')
# f.write(image_link.content)
# f.close()

###toscrape.com not working
# result = requests.get('https://www.quotes.toscrape.com/')
# soup=bs4.BeautifulSoup(result.text,"lxml")