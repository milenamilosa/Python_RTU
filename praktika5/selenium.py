import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service #sakam datoram ka mes stradasim ar hromu
from selenium.webdriver.common.by import By

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option) # tieši hroms
# šeit beidzas iepriekš definētas rindas. jebkuram pārlūkam būs tas pats kods
url = "https://www.ebay.com"
driver.get(url) # izsaukt pārlūks
input() # lai programma neaizvērtu uzreiz tīmekļa vietni kamēr nav uzspiest enter


