import os

from pdf2docx import Converter
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# print("Current working directory: " + os.getcwd())
# strCWD = "c:\\temp"
# print("Setting CWD to : " + strCWD)
# os.chdir(strCWD)

# pdf_file = input("Please provide the PDF (source) Filename/Filenames : ")
print("Please provide the PDF (source) Filename/Filenames")
#pdf_file = filedialog.askopenfilename()
pdf_files = filedialog.askopenfilenames()

# doc_file = input("Please provide the DOC (target) folder : ")
print("Please provide the DOC (target) folder")
doc_file_folder = filedialog.askdirectory()
counter_var = 1

for pdf_file in pdf_files:
    filename, file_extension = os.path.splitext(pdf_file)
    if file_extension.upper() != ".PDF":
        print("File : " +  pdf_file + " is not a PDF File, bypassing the file...")
        continue
    doc_file = doc_file_folder + "/result" + str(counter_var) + ".docx"
    counter_var += 1
    pdf_filecntrl = open(pdf_file, "r+")
    if not pdf_filecntrl.readable():
        print("PDF File is not readable. Quitting")
        exit(-1)
    else:
        pdf_filecntrl.close()

    doc_filecntrl = open(doc_file, "w")
    if not doc_filecntrl.writable():
        print("DOC File is not writable. Quitting")
        exit(-1)
    else:
        doc_filecntrl.close()

    convPDFtoDoc = Converter(pdf_file)
    convPDFtoDoc.convert(doc_file)
    convPDFtoDoc.close()
