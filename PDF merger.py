import PyPDF2

Pdffiles = ['1st pdf.pdf','2nd pdf.pdf']
merger = PyPDF2.PdfMerger()
for filename in Pdffiles:
    Pdffiles = open(filename,'rb')
    pdfReader = PyPDF2.PdfReader(Pdffiles)
    merger.append(pdfReader)
    Pdffiles.close()
    merger.write('merged.pdf')
    