from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = Path(r'C:\Users\harsh\OneDrive\Desktop\hp5_halved.pdf')
output_path = Path(r'C:\Users\harsh\OneDrive\Desktop\hp5_final.pdf')

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

'''
page_no = input('Enter Page No:')
page = pdf_reader.getPage(int(page_no))
text = page.extractText()
splits = text.split("\n")
first_line = splits[0].split("  ")
first_line[0] = first_line[0].replace(" ", "")
first_line[1] = first_line[1].replace(" ", "")
first_line[3] = first_line[3].replace("™", "'")
title = first_line[0] + " " + first_line[1] + " " + first_line[3]
title = title[:-1]
print(title)
'''

'''C H A P T E R  O N E   1  THE OTHER MINISTER'''
'''C H A P T E R  T W O   19  SPINNER™S END'''
'''C H A P T E R  T H R E E   38  WILL AND WON™T'''

bms = 0
bookmarks = []
with output_path.open(mode="wb") as output_file:
    for n in range(pdf_reader.getNumPages()):
        try:
            page = pdf_reader.getPage(int(n))
            pdf_writer.addPage(page)
            text = page.extractText()
            if text.startswith("C H A P T E R  "):
                splits = text.split("\n")
                first_line = splits[0].split("  ")
                first_line[0] = first_line[0].replace(" ", "")
                first_line[1] = first_line[1].replace(" ", "")
                try:
                    first_line[3] = first_line[3].replace("™", "'")
                    title = first_line[0] + " " + first_line[1] + ": " + first_line[3]
                except:
                    title = first_line[0] + " " + first_line[1] + ": " + "THE WHITE TOMB "
                title = title[:-1]
                if title in bookmarks:
                    pdf_writer.addBookmark(title, n-1)
                    bms += 1
                    print(str(bms) + ". Added "+ "'" + title + "'" + " for page " + str(n))
                else:
                    bookmarks.append(title)
        except Exception as e:
            print(e)
            break
    pdf_writer.write(output_file)
    print("Done")
