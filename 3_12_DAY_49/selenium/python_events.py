from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.python.org/")
# print(driver.page_source)
# event_times=driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
try:
    event_times = WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".event-widget time"))
    )
    event_name = WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".event-widget li a"))
    )
    events={}
    for n in range(len(event_times)):
        events[n]={
            "time":event_times[n].text,
            "name":event_name[n].text,
        }

    print(events)
    # for name in event_name:
    #     print(name.text)
    #
    # for time in event_times:
    #     time1=time.text.strip()
    #     print(time1)


except Exception as e:
    print(e)
finally:
    driver.quit()

 # year = WebDriverWait(driver,10).until(
        #     EC.presence_of_element_located((By.CLASS_NAME,'say-no-more'))
        # ).text.strip()
        # # time.find_element(By.CLASS_NAME, 'say-no-more')
        # print(year)
        # month_day=time.text.strip()
        # full_date =f"......{year}{month_day}"
        # print(full_date)