from pypdf import PdfMerger
import datetime
import sys

merger = PdfMerger()
i = 0

for pdf in sys.argv:
    if pdf == "\*PdfMergeCL.py" or pdf == "\*.\\PdfMergeCL.py":
        print("fitzli")
        continue
    if i == 0:
        i = 1
        continue
    print(pdf)
    try:
        merger.append(pdf)
    except:
        print("Error")

filename = str(datetime.date.today()) + "_Result.pdf"
print(filename)
merger.write(filename)
merger.close()