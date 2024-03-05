import requests
import pandas as pd
import time
import base64
from datetime import datetime
from datetime import date
from seleniumbase import Driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import csv

# driver = Driver(uc=True, headless2=True)
driver = Driver(uc=True)
driver.maximize_window()

driver.get('https://eur.vevor.com/restaurant-food-service-c_10015')
bigmore = '//*[@id="siteWrap"]/div[1]/div[3]/div[2]/div[1]/div[2]/div/ul/div'
smallmore = '//*[@id="siteWrap"]/div[1]/div[4]/div[2]/div[1]/div[2]/div/ul/div'
bigxpath = '//*[@id="siteWrap"]/div[1]/div[3]/div[2]/div[1]/div[2]/div/ul/li/ul/li'
smallxpath = '//*[@id="siteWrap"]/div[1]/div[4]/div[2]/div[1]/div[2]/div/ul/li[2]/ul/li'
categoryxpath = '//*[@id="siteWrap"]/div[1]/div[3]/div[2]/div[2]/div[1]/div/div'
imagexpath = '//*[@id="js-panelThumbList"]/div/div/span'
filename = 'result.csv'

# previous_url1 = driver.current_url
bigcounts = range(len(driver.find_elements(By.XPATH, bigxpath)))
for bigcount in bigcounts:
    bigname = driver.find_elements(By.XPATH, bigxpath)[bigcount].find_element(By.XPATH, './/a/span').text
    if bigname == '':
        driver.find_element(By.XPATH, bigmore).click()
    bigname = driver.find_elements(By.XPATH, bigxpath)[bigcount].find_element(By.XPATH, './/a/span').text
    print ("***",bigname)

    # data = [
    #     [bigname, '', '', '', '']
    # ]

    # with open(filename, 'a', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerows(data)

    element = driver.find_elements(By.XPATH, bigxpath)[bigcount]
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, bigxpath + f"[{bigcount + 1}]")))
    element = driver.find_elements(By.XPATH, bigxpath)[bigcount]
    element.click()

    # driver.find_elements(By.XPATH, bigxpath)[bigcount].click()
    # ---------- small loop start ---------------
    
    smallcounts = range(len(driver.find_elements(By.XPATH, smallxpath)))
    for smallcount in smallcounts:
        smallname = driver.find_elements(By.XPATH, smallxpath)[smallcount].find_element(By.XPATH, './/a/span').text

        # smallmore scrollview
        if smallname == '':
            driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, smallmore))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, smallmore))).click()
        
        smallname = driver.find_elements(By.XPATH, smallxpath)[smallcount].find_element(By.XPATH, './/a/span').text
        print ("********",smallname)

        # data = [
        #     ['', smallname, '', '', '']
        # ]

        # with open(filename, 'a', newline='') as file:
        #     writer = csv.writer(file)
        #     writer.writerows(data)

        element = driver.find_elements(By.XPATH, smallxpath)[smallcount]
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, smallxpath)))
        element = driver.find_elements(By.XPATH, smallxpath)[smallcount]
        element.click()

        # ---------  main loop start  ------------------
        categorys = range(len(driver.find_elements(By.XPATH, categoryxpath)))
        for category in categorys:

            element = driver.find_elements(By.XPATH, categoryxpath)[category]
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, categoryxpath)))
            element = driver.find_elements(By.XPATH, categoryxpath)[category]
            element.click()

            description = driver.find_elements(By.CLASS_NAME, "detailInfo_title")[0].text
            print ("##################",description)
            price = driver.find_elements(By.CLASS_NAME,'shopPrice')[0].get_attribute('data-currency')
            print ("##################", price)

            # data = [
            #         ['', '', description, price, '']
            #     ]

            # with open(filename, 'a', newline='') as file:
            #     writer = csv.writer(file)
            #     writer.writerows(data)

            imagecounts = range(len(driver.find_elements(By.XPATH, imagexpath)))
            for imagecount in imagecounts:
                image = driver.find_elements(By.XPATH, imagexpath)[imagecount]
                try:
                    image_url = image.find_elements(By.CLASS_NAME,'detailImg_thumbImg')[0].get_attribute('src')
                    print (image_url)

                    # data = [
                    #     ['', '', '', '', image_url]
                    # ]

                    # with open(filename, 'a', newline='') as file:
                    #     writer = csv.writer(file)
                    #     writer.writerows(data)
                except:
                    pass
            driver.back()
        # ---------  main loop end  ------------------

        driver.back()
        
    # ---------- small loop end ---------------
    driver.back()
    
while True:
    pass    





