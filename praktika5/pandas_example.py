import pandas
import openpyxl
fails = pandas.read_excel("salary.xlsx", sheet_name="Sheet2") # if no pages are specified, then the last one saved is open
info_list = fails.values.tolist()
print(info_list)
count = 0
age_list = []
for line in info_list:
    if line[2] == "Accounting": # if line[0] in codes:
        age_list.append(line[4])
max(age_list)
print(sorted(age_list))
print(max(age_list))