import pandas as pd
import selenium
from selenium import webdriver
#from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from tabulate import tabulate

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.rigassatiksme.lv/lv/"
driver.get(url)
time.sleep(2)



# veido sarakstu ar visiem elementiem, kuru klases nosaukums ir "title"
elements = driver.find_elements(By.CLASS_NAME,"title") 

# akceptē cookies
elements[14].click()


time.sleep(5)