name=[]
vertibas=[]

with open("data.csv", "r") as file:
    for line in file:
        row=line.rstrip().split(",")
        name.append(row)
        
for row in name:
    if (row[1 == "Agriculture"]):
        vertibas.append(row[5])
        
        
print(row)