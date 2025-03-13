from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

time_out = time.time() + 5
five_min = time.time() + 5 * 60

while True:
    cookie.click()
    if time.time() > time_out:
        all_price = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        item_price = []

        for price in all_price:
            try:
                element_text = price.text
                if element_text != "":
                    cost = int(element_text.split('-')[1].strip().replace(',', ''))
                    item_price.append(cost)

            except Exception as e:
                print(e)

            # if element_text != "":
            #     cost = int(element_text.split('-')[1].strip().replace(',', ''))
            #     item_price.append(cost)
                # print(cost)

        cookie_upgrade = {}
        for n in range(len(item_price)):
            cookie_upgrade[item_price[n]] = item_ids[n]

        money = driver.find_element(By.ID, value="money").text
        if "," in money:
            money = money.replace(",", "")

        cookie_count = int(money)
        print(cookie_upgrade)

        affordable_upgrade = {}
        for cost, id in cookie_upgrade.items():
            if cookie_count >= cost:
                affordable_upgrade[cost] = id
        print(affordable_upgrade,"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

        try:
            max(affordable_upgrade)
        except ValueError as e:
            print(e)
            break
        highest_price = max(affordable_upgrade)
        print(highest_price)
        to_purchase_id = affordable_upgrade[highest_price]
        print(to_purchase_id)
        try:
            driver.find_element(By.ID, value=to_purchase_id).click()
        except Exception as e:
            print(to_purchase_id)
            print(e)

        time_out = time.time() + 5

    if time.time() >= five_min:
        cookie_per_sec = driver.find_element(By.ID, value="cps")
        print(cookie_per_sec.text)
        driver.quit()
        break
