from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas     # strādā kā otrs caurspīdīgs slānis, kur var darīt visu
import io
from reportlab.pdfbase.ttfonts import TTFont    # lai teksts būtu salasāms
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(TTFont('DejaVu_Lv','fonts/DejaVuSans.ttf'))

input_pdf=PdfReader(open("path", "rb"))
buffer = io.BytesIO()
c = canvas.Canvas(buffer)
c.setFont("DejaVu_Lv", 16) # setColor, drawString, setFillColor...

text_pdf=PdfReader(buffer)  # veido to slāni par pdf
output_pdf=PdWriter()
for i in range(len(input_pdf.pages)):
    ...
