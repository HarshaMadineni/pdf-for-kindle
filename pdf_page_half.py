from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter
import copy

pdf_path = Path(r'C:\Users\harsh\OneDrive\Desktop\hp5_cropped.pdf')

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

output_path = Path(r'C:\Users\harsh\OneDrive\Desktop\hp5_halved.pdf')

print ('Starting...')

for n in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(n)
    if n >= 0:
        top_side = copy.deepcopy(page)
        bottom_side = copy.deepcopy(page)

        ur_coords = page.mediaBox.upperRight
        ll_coords = page.mediaBox.lowerLeft

        new_coords = (ur_coords[0], (ur_coords[1] + ll_coords[1])/2 + 2)

        top_side.mediaBox.lowerRight = new_coords
        bottom_side.mediaBox.upperRight = new_coords

    pdf_writer.addPage(top_side)
    pdf_writer.addPage(bottom_side)
    print('Page' + str(n) + 'added')

with output_path.open(mode="wb") as output_file:
    pdf_writer.write(output_file)
print('Done')
