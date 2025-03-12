from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name =driver.find_element(By.NAME,value="fName")
f_name.send_keys("abcdef")
l_name =driver.find_element(By.NAME,value="lName")
l_name.send_keys("ghij")
email =driver.find_element(By.NAME,value="email")
email.send_keys("abc@gmail.com")


xpath="/html/body/form/button"
submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()

# search1.send_keys("python",Keys.ENTER)
driver.quit()