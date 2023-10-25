#_file_read_to_list


name=[]
with open("name.txt", "r") as file:
    for line in sorted(file, reverse=True):
        name.append(line.rstrip())

for n in sorted(name):
    print(n)

print(name[1])
    #     print(line.strip())


#_text_split

row=[]

with open("sample.log") as file:
    for line in file:
        row=line.rstrip().split(" ") 
        if len(row)>4:
            print(row[3]+" "+row[0])


#_file_read

with open("name.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello", line.rstrip())

#_file _write

name=input("What is your name? ")
f=open("name.txt","a")
f.write(name+"\n")
f.close


# list

# input information from keyboar and save it to list

names =[]     
# ask to enter 3 names in loop
for _ in range(3):
    name=input("What is your name? ")
    names.append(name)

# output sortet information in terminal

for name in sorted(names):
    print("hello, {name}")