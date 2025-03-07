from bs4 import BeautifulSoup
import lxml
import requests

response=requests.get("https://appbrewery.github.io/news.ycombinator.com/")
content=response.text
# print(content)

soup=BeautifulSoup(content,"html.parser")
# print(soup.title)

articals=soup.find_all(name="a",class_="storylink")
article_texts=[]
article_links=[]
for article_tag in articals:
    text=article_tag.getText()
    article_texts.append(text)
    link=article_tag.get("href")
    article_links.append(link)

article_upvote=[int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]


largest_number=max(article_upvote)
largest_index=article_upvote.index(largest_number)
print(largest_index)
print(article_links[largest_index])
print(article_texts[largest_index])
# print(article_texts)
# print(article_links)
# print(article_upvote)
# print(article_upvote[0].split()[0])






# with open("website.html") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.a)
# # print(soup.p)
# # print(soup)
# # for indent
# # print(soup.prettify())
#
# x=soup.find_all("a")
# # print(x)
#
# # for tag in x:
#     # print(tag)
#     # print(tag.getText())
#     # print(tag.get("href"))
#
# #showing first
# # heading=soup.find(name="h1",id="name")
# # print(heading)
#
# # section_heading=soup.find(name="h3",class_="heading")
# # print(section_heading)
#
# name =soup.select_one(selector="#name")
# print(name)
#
# heading=soup.select(selector=".heading")
# print(heading)