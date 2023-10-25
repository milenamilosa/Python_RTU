import PyPDF2
import datetime
file=input()

result=0

if file!="":        
    row=[]

    try:
        pdf_file=PyPDF2.PdfReader(open(file,"rb"))
    except OSError as e:
        print(0)
        exit()

    number_of_pages=len(pdf_file.pages)
    page1=pdf_file.pages[0]
    page2=pdf_file.pages[1]
    text1=page1.extract_text()
    text2=page2.extract_text()
    pos1 = text1.find("Apmaksai: ")
    pos2 = text1.find("Elektroenerģijas patēriņš kopā")
    pos3 = text2.find("Apjoms")
    pos4 = text2.find("kWh")

    summa = text1[pos1+10:pos2].rstrip()  
    amount = text2[pos3+57:pos4].rstrip()  
    price = text2[pos4+4:pos4+10].rstrip()
    period = text2[pos3-23:pos3].rstrip()

    periodSplit = period.strip().split(" - ")
    periodStart = datetime.datetime.strptime(periodSplit[1], "%d.%m.%Y").strftime("%Y-%m-%d")
    periodEnd = datetime.datetime.strptime(periodSplit[0], "%d.%m.%Y").strftime("%Y-%m-%d")

    all_prices = []
    nordpool_list = []
    # avg_price = 0
 
    with open("nordpool.csv","r") as f:
        next(f)
        for line in f:
            row = line.rstrip().split(",")
            nordpool_list.append(row)
            date = row[0]

        for i, element in enumerate(nordpool_list):
            if element[0] == (periodStart + " 23:00:00"):
                while element[0] != (periodEnd + " 00:00:00"):
                    all_prices.append(float(element[2]))
                    i += 1
                    element = nordpool_list[i]
                all_prices.append(float(element[2]))

        if len(all_prices) != 0:
            avg_price = sum(all_prices)/len(all_prices)
            avg_price = round(avg_price, 3)
        else:
            print("Division by 0")
            exit()

    summaFloat = float(summa.replace(",", "."))
    amountFloat = amount.replace(",", ".")
    amountFloat = float(amountFloat.replace(" ", ""))
    priceFloat = float(price.replace(",", "."))


    pdf_bill = (amountFloat * priceFloat)
    nordpool_bill = (amountFloat * avg_price)

    if amountFloat != 0.0:
        result = round((pdf_bill - nordpool_bill),1)
        #result = round((summaFloat - nordpool_bill),1)
    else:
        result = 0

    print(result)
else:
    print(0)