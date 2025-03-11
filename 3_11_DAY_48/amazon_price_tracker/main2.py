import smtplib
from bs4 import BeautifulSoup
import requests
from mail_config import EMAIL,PASSWORD
my_email = EMAIL
password = PASSWORD

practice_url="https://appbrewery.github.io/instant_pot/"
live_url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
    "Dnt": "1",
    "Priority": "u=0, i",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
}
response=requests.get(url=live_url,headers=header)

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
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject:Amazon Price Alert! \n\n{message}\n{live_url}".encode('utf-8'))
        print("send")


