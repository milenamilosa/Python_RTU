import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

# Read data using Pandas from people.csv
file_path = 'C:/Users/milos/Downloads/people.csv'
data = pd.read_csv(file_path)
name = (data['First Name'] + ' ' + data['Last Name']).tolist()

# Function to encode names using the CRC32 tool
def get_encoded_name(full_name):
    driver.get("https://emn178.github.io/online-tools/crc32.html")
   
    find = driver.find_element(By.ID, "input")
    find.send_keys(full_name)
    output = driver.find_element(By.ID, "output").get_attribute("value")
    find.clear()
    return output

# Get encoded names for each employee
encoded_names = {}
for employee_name in name:
    encoded_name = get_encoded_name(employee_name)
    encoded_names[employee_name] = encoded_name

# Load salary data using Pandas from salary.xlsx
salary_file_path = 'C:/Users/milos/Downloads/salary.xlsx'
salary_data = pd.read_excel(salary_file_path)

# Retrieve salary information and calculate total salary for each employee
salaries = {}
for index, row in salary_data.iterrows():
    encoded_name = row['Codet name value']
    salary = row['Salary']
    for employee, encoded in encoded_names.items():
        if encoded == encoded_name:
            if employee not in salaries:
                salaries[employee] = [salary]
            else:
                salaries[employee].append(salary)

# Calculate total salary for each employee and print results
for employee, salary_list in salaries.items():
    total_salary = sum(salary_list)
    print(f"Employee: {employee}, Total Salary: {total_salary}")

# Close the WebDriver
driver.quit()