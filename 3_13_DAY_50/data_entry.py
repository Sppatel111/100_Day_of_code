import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

form_link="https://docs.google.com/forms/d/e/1FAIpQLScIevo4zEO4FPZbNh_qaufL3pBmARbkrrZ19WDAVxforppfUg/viewform?usp=header"
zillow="https://appbrewery.github.io/Zillow-Clone/"
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
}

response=requests.get(url=zillow,headers=header)

soup=BeautifulSoup(response.text,"html.parser")

# price=soup.find(class_=).getText()
# print(price)
# address=soup.find(class_="StyledPropertyCardDataArea-anchor" )

search_results=soup.find("div",{"id":"grid-search-results"})

def get_links():
    links_list = [a["href"] for a in search_results.find_all("a", tabindex="0")]
    for index in range(len(links_list)):
        if not links_list[index].startswith("http"):
            links_list[index] = 'https://www.zillow.com' + links_list[index]
    #print(links_list)
    return links_list

get_links()


def get_addresses():
    address_list = [address.getText() for address in search_results.find_all("a", tabindex="0") if address.getText()]
    #print(address_list)
    return address_list

get_addresses()

#StyledPropertyCardDataWrapper
def get_price():
    price_list = [price.getText()[:7] for price in soup.find_all("div", class_="PropertyCardWrapper")]
    print(price_list)
    return price_list

get_price()

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(form_link)
time.sleep(3)

print(len(get_addresses()))
for fill_out in range(len(get_addresses())):
    property_address=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_price=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_link=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_address.send_keys(get_addresses()[fill_out])
    property_price.send_keys(get_price()[fill_out])
    property_link.send_keys((get_links()[fill_out]))

    submit_button=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    another_response=driver.find_element(By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()

driver.quit()

# price=driver.find_element(By.CLASS_NAME,value="PropertyCardWrapper__StyledPriceLine")
# print(price.text)
#
# address=driver.find_element(By.CSS_SELECTOR,value=".StyledPropertyCardDataArea-anchor address")
# print(address.text)
#
# link=driver.find_element(By.CLASS_NAME,value="property-card-link")
# print(link.text)

#driver.quit()


