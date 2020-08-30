from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = Path(r'C:\Users\harsh\OneDrive\Desktop\Books\hp5.pdf')

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

output_path = Path(r'C:\Users\harsh\OneDrive\Desktop\hp5_cropped.pdf')

print ('Starting...')

for n in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(n)
    if n > 13 and n < 667:
        page.mediaBox.lowerLeft = (28, 60)
        page.mediaBox.upperRight = (414, 621)
    pdf_writer.addPage(page)
    print('Page' + str(n) + 'added')

with output_path.open(mode="wb") as output_file:
    pdf_writer.write(output_file)
print('Done')
