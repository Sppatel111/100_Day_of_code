from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# for keeping open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

search_bar=driver.find_element(By.NAME,value="q")
print(search_bar.get_attribute("placeholder"))

button=driver.find_element(By.ID,value="submit")
print(button.size)

link=driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a")
print(link.text)

xpath=driver.find_element(By.XPATH,value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(xpath.text)


tier_1=driver.find_elements(By.CLASS_NAME,value="tier-1")
for tier in tier_1:
    print(tier.text)

driver.quit()