import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from tabulate import tabulate

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

list=[]
name=[]

with open("people.csv", "r") as file:
    next(file)
    for line in file:
        row=line.rstrip().split(",") 
        list.append(row)
         
    for row in list:
        name.append(row[2] + " " + row[3])

url = "https://emn178.github.io/online-tools/crc32.html"
driver.get(url)
time.sleep(5)

codes=[]
for element in range (len(name)):
    find=driver.find_element(By.ID, "input")    # find type-in place
    find.send_keys(name[element])               # type in name
    find=driver.find_element(By.ID, "output")   # find result
    temp=find.get_attribute("value")            # save result in a parameter
    codes.append(temp)                          # add coded names to list
    find=driver.find_element(By.ID, "input")    # find type-in place again
    find.clear()                                # clear window
    time.sleep(1)

excel_data=[]
salary = 0

fails = pd.read_excel("salary.xlsx", sheet_name="Sheet2") 
excel_data = fails.values.tolist()
count = 0
salary = 0
list_sal = []

for code in codes:               
    for row in excel_data:
        if code == row[0]:
            salary+=int(row[1])
    list_sal.append(salary)
    salary = 0

table = zip(name, list_sal)
print(tabulate(table, headers=["Name", "Salary"], tablefmt="github"))