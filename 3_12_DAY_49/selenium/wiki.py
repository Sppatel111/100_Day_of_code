from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver= webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count=driver.find_element(By.XPATH,value='//*[@id="articlecount"]/ul/li[1]/a')
print(article_count.text)

# all_portals=driver.find_element(By.LINK_TEXT,value="Content portals")
# all_portals.click()

search1 =driver.find_element(By.NAME,value="search")

search1.send_keys("python",Keys.ENTER)
driver.implicitly_wait(10)
driver.quit()