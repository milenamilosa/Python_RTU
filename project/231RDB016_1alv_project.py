import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from tabulate import tabulate

item = input("Ievadiet meklējamo preci: ")                      # meklējamās preces ievade no klaviatūras (rekomendējamā ievade: lego)
# item = "lego"                                                 # atkomentēt, ja negrib vadīt preci no klaviatūras

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.1a.lv"
driver.get(url)
driver.maximize_window()                                        # atver mājaslapu "fullscreen" režīmā

driver.find_element(By.CLASS_NAME,"c-button-inverse").click()   # akceptē cookie failus

find=driver.find_element(By.ID, "q")                            # atrod meklēšanas logu
find.send_keys(item)                                            # ieraksta preces nosaukumu logā
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
time.sleep(2)

nosaukumi = []                  # saraksts ar mājaslapas preču nosaukumiem
cenas = []                      # saraksts ar mājaslapas preču cenām

preces_nosaukumi = driver.find_elements(By.CLASS_NAME, "catalog-taxons-product__name")              # meklē visus elementu nosaukumus pēc klases un veido sarakstu no tiem
for preces_nosakums in preces_nosaukumi:
    nosaukumi.append((preces_nosakums.get_attribute('innerHTML')).strip())

preces_cenas = driver.find_elements(By.CLASS_NAME, "catalog-taxons-product-price__item-price")      # meklē visus elementu cenas pēc klases un veido sarakstu no tiem

for preces_cena in driver.find_elements(By.XPATH, '//span[@class = "catalog-taxons-product-price__item-price"]'):   # savāc tekstu no 'span'-a cenas klases elementiem
    cena = preces_cena.text.replace(" ", "")
    cena = cena.replace("€/gab.", "")
    cena = cena.replace(",", ".")
    cena = float(cena)
    cena = float(("{:.2f}".format(cena)))
    cenas.append(cena)          # pievieno cenu sarakstam


table = zip(cenas, nosaukumi)
print(tabulate(sorted(table), headers=["Preces nosaukums", "Preces cena"], tablefmt="github"))      # izvada pirmo 48 populārāko preču sarakstu filtrējot no zemākās cenas līdz augstākai