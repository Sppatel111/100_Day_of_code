from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options= Options()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(chrome_options)
driver.get('https://rcdb.com/')


def scrape():
    soup=BeautifulSoup(driver.page_source,'html.parser')


    roller_coaster_info=soup.find('div',id='rrc_text')
    list1=[]
    if roller_coaster_info:

        list1.append(roller_coaster_info.find('span', string='Roller Coaster').find_next('a').text.strip())
        list1.append(roller_coaster_info.find('span', string='Park').find_next('a').text.strip())
        list1.append(', '.join([a.text.strip() for a in roller_coaster_info.find('span', string='Location').find_all_next('a',limit=3)]))

        if roller_coaster_info.find('span', string='Status'):
            if roller_coaster_info.find('span', string='Status').find_parent('p'):
                list1.append(roller_coaster_info.find('span', string='Status').find_parent('p').text.replace('Status', '').strip())
            else:
                list1.append(None)

        if roller_coaster_info.find('span', string='Inversions'):
            list1.append(roller_coaster_info.find('span', string='Inversions').find_next('span').text.strip())
        else:
            list1.append(None)

        if roller_coaster_info.find('span', string='Speed'):
            list1.append(roller_coaster_info.find('span', string='Speed').find_next('span',class_='float').text.strip())
        else:
            list1.append(None)

        if roller_coaster_info.find('span', string='Height'):
            list1.append(roller_coaster_info.find('span', string='Height').find_next('span').text.strip())
        else:
            list1.append(None)

        if roller_coaster_info.find('span', string='Length'):
            list1.append(roller_coaster_info.find('span', string='Length').find_next('span').text.strip())
        else:
            list1.append(None)

        if roller_coaster_info.find('span',string='G-Force'):
            list1.append(roller_coaster_info.find('span', string='G-Force').find_next('span',class_='float').text.strip())
        else:
            list1.append(None)

        if roller_coaster_info.find('span', string='Manufacturer'):
            list1.append(roller_coaster_info.find('span', string='Manufacturer').find_next('a').text.strip())
        else:
            list1.append(None)
    print(list1)
    return list1





with open('random.csv','a',newline='', encoding='utf-8') as f:
    writer=csv.writer(f)

    if f.tell() == 0:
        writer.writerow(['coaster','park','location','status','inversions', 'speed','height','length','G-Force','manufacturer'])

    for _ in range(5):
        list1=scrape()
        writer.writerow(list1)
        driver.refresh()
        time.sleep(2)

driver.quit()