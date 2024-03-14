# programma, kas ver vaļā pdf failu un pievieno tās lapas klāt, beigās saglabā
from PyPDF2 import PdfReader, PdfWriter

def merge_pdf(input_file, output_file):
    result=PdfWriter()
    for file in input_file:
        reader=PdfReader(file)

# meklēt ortusā