import PyPDF2

import pathlib
from tabulate import tabulate   # smuks datu izvads tabulas formātā
data = []                       # datu uzglabasani pec nolasišanas no pdf faila. info jāglabā tā, lai piekļūtu pie visiem datiem
adrese = pathlib.Path("invoices")          # adrese mapei, ar ko strādājam
visi_faili=list(adrese.glob("*.pdf"))      # filtrs failiem, kas beidzas ar .pdf
for f in range(len(visi_faili)):           # darbs ar visiem failiem pēc kārtas
    row=[]                                 # vērtības no faila
    pdf_file=PyPDF2.PdfReader(open(visi_faili[f],"rb"))     # atver failu, nolasa info
    number_of_pages=len(pdf_file.pages)
    page1=pdf_file.pages[0]
    page2=pdf_file.pages[1]

    text1=page1.extract_text()
    text2=page2.extract_text()

    pos1=text1.find("Apmaksai:)")
    pos2=text1.find("Elektroenerģijas patēriņš kopā")

    summa=text1[pos1+10:pos2].rstrip()      # +10 simboli jo 10 simboli no rindiņas sākuma līdz meklējamai vērtībai
    print(summa)                            # vērtība ir teksts! ja iegūt vērtību no teksta, tad tas vienmēr būs teksts
    print(float(summa))                     # izmetīs kļūdu, jo vērtība tiek izvadīta ar komatu, lai būtu float format, replace "," -> "."
    row.append(summa)
    pos1=text2.find("Apjoms Mērv. Cena,")
    periods=text2[pos1-23:pos1]             # meklējam rēķina datumu/periodu. nepieciešama info sākas 23 simbolu pirms pos1 (noteiktās pozīcijas)
    row.append(periods)
    data.append(row)                        # datu uzglabāšana lielajā masīvā, kas sastāv no masīviem

print(tabulate(data,headers=["Summa", "Periods"], tablefmt="github"))

