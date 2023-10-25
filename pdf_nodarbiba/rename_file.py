import os

folder="invoices"   # izmantojama mape

for count, filename in enumerate(os.listdir(folder)):   #atrast mapi sistemaa
    dst=f"invoice_{str(count)}.pdf"     # jauns nosaukums
    src=f"{folder}/{filename}"          # atrast failu ar vecu nosaukumu
    dst=f"{folder}/{dst}"               # jauns nosaukums tiek integrets vecā vietā
    os.rename(src,dst)