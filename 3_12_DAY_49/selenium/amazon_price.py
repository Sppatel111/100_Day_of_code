from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# for keeping open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# print(f"The Price is {price_dollar.text}.{price_cent.text}")

# driver.implicitly_wait(60)
# # driver.close()
# driver.quit()

try:
    # Wait for the element to be present
    price_dollar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"a-price-whole")),

    )
    price_cent = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "a-price-fraction"))
    )
    print(f"The Price is {price_dollar.text}.{price_cent.text}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()

