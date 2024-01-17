import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from tabulate import tabulate


service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

# item = input("Enter item to search:")
item = "lego"

url = "https://www.1a.lv"
driver.get(url)
driver.maximize_window()    # atver mājaslapu "fullscreen" ērtam webskrepingam

driver.find_element(By.CLASS_NAME,"c-button-inverse").click()   # pieņem cookie failus
# time.sleep(1)

find=driver.find_element(By.ID, "q")    # atrod meklēšanas logu
find.send_keys(item)                    # ieraksta preces nosaukumu logā
time.sleep(1)

driver.find_element(By.CLASS_NAME,"main-search-submit").click() # spiež uz meklēšanas pogu

driver.execute_script("window.scrollTo(0, 1400)")               # tin mājaslapu uz vajadzīgo vietu uz leju
time.sleep(1)                                                   # nepieciešamais laiks ielādei
price=driver.find_element(By.ID, "attr-to-price")               # atrod gala cenas logu
action = ActionChains(driver)                                   # nodrošina dubultklikšķa funkcijas izpildi
action.double_click(on_element = price)                         # dubultklikšķa apraksts (kur tam jānotiek)
action.perform()                                                # dubultklikšķa izpilde
time.sleep(1)

price.send_keys(200)                                            # ievada lietotāja budžetu (cenas augstāko robežu)
price.send_keys(Keys.ENTER)
time.sleep(5)

# saraksti ar mājaslapas precēm
nosaukumi = []
cenas = []

# prece = driver.find_element(By.CLASS_NAME, "catalog-taxons-product__name")                # savāc visus cenas elementus pēc klases
# print(prece.get_attribute('outerHTML'))

preces_nosaukumi = driver.find_elements(By.CLASS_NAME, "catalog-taxons-product__name")      # savāc visus elementu nosaukumus pēc klases
for preces_nosakums in preces_nosaukumi:
    nosaukumi.append((preces_nosakums.get_attribute('innerHTML')).strip())
    # print((preces_nosakums.get_attribute('innerHTML')))                                     # izvada preces nosaukumu
# print(nosaukumi)                                                                          # preču nosaukumu saraksts

preces_cenas = driver.find_elements(By.CLASS_NAME, "catalog-taxons-product-price__item-price")      # savāc visus elementu nosaukumus pēc klases

for preces_cena in driver.find_elements(By.XPATH, '//span[@class = "catalog-taxons-product-price__item-price"]'):   # savāc tekstu no 'span'a konkrētās klases elementiem
    # print (preces_cena.text)
    cena = preces_cena.text.replace(" ", "")
    cena = cena.replace("€/gab.", "")
    cena = cena.replace(",", ".")
    cena = float(cena)
    cena = float(("{:.2f}".format(cena)))
    # cena = (format(cena, '.2f'))
    cenas.append(cena)                                                                # pievieno cenu sarakstam

# for preces_cena in preces_cenas:
#     cenas.append((preces_cena.get_attribute('innerHTML')).strip())
    # print((preces_cena.get_attribute('innerHTML')))                                     # izvada preces nosaukumu
# print(cenas)                                                                      # preču nosaukumu saraksts

count = 0
for i in nosaukumi:
    count+=1
# print(count)

count = 0
for i in cenas:
    count+=1
# print(count)
# for i in preces:
#     prece = driver.find_element(By.CLASS_NAME, "catalog-taxons-product__name")
#     prece.get_attribute('innerHTML')
#     print(prece)

table = zip(cenas, nosaukumi)
print(tabulate(sorted(table), headers=["Preces nosaukums", "Preces cena"], tablefmt="github"))