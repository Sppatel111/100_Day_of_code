import smtplib
from bs4 import BeautifulSoup
import requests
from mail_config import EMAIL,PASSWORD
my_email = EMAIL
password = PASSWORD

practice_url="https://appbrewery.github.io/instant_pot/"
live_url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

response=requests.get(practice_url)

soup =BeautifulSoup(response.text,"html.parser")
# print(soup.prettify())

price =soup.find(class_="a-offscreen").getText()
print(price)

price_without_currency=price.split("$")[1]
print(price_without_currency)

price_as_float =float(price_without_currency)
print(price_as_float)


title=soup.find(id="productTitle").getText().strip()
print(title)

BUY_PRICE =100

if price_as_float <BUY_PRICE:
    message =f"{title} on sale for {price}!"

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject:Amazon Price Alert! \n\n{message}\n{practice_url}".encode('utf-8'))


