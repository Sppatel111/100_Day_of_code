from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie=driver.find_element(By.ID,value="cookie")
cookie.click()

store = driver.find_elements(By.CSS_SELECTOR, value="#store .grayed b")
price_list = [int(price.text.split('-')[1].strip().replace(",", "")) for price in store if price.text]

store_dict = {
    0: "Cursor",
    1: "Grandma",
    2: "Factory",
    3: "Mine",
    4: "Shipment",
    5: "Alchemy lab",
    6: "Portal",
    7: "Time machine",
}


def cookie_clicker():
    check = time.time() + 5
    while True:
        cookie.click()
        if time.time() > check:
            purchase()
            break


def purchase():
    my_points = driver.find_element(by=By.XPATH, value='//*[@id="money"]')
    my_points = int(my_points.text.replace(",", ""))
    purchase_item = store_dict[price_list.index([item for item in price_list if my_points > item][-1])]
    driver.find_element(by=By.CSS_SELECTOR, value=f"#store #buy{purchase_item}").click()
    cookie_clicker()


cookie_clicker()