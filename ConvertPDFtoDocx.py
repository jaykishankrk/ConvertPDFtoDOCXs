import os
import ntpath
from pdf2docx import Converter
import tkinter as tk
from tkinter import filedialog


# function to retrieve filename from absolute path.
def retrieve_filename(path_and_filename):
    # Split the filename and pathname
    path_name, file_name = ntpath.split(path_and_filename)
    # return filename if it exists or else the whole path as is.
    return file_name or ntpath.basename(path_name)


root = tk.Tk()
root.withdraw()

print("Please provide the PDF (source) Filename/Filenames")

# opens file dialog to select multiple PDF files.
pdf_files = filedialog.askopenfilenames()

print("Please provide the DOC (target) folder")

# opens folder dialog to select target folder path.
doc_file_folder = filedialog.askdirectory()

# Iterate through list of PDF files selected and convert the same to docx.
for pdf_file in pdf_files:
    # check to make sure the files selected are indeed PDF files.
    filename, file_extension = os.path.splitext(pdf_file)
    if file_extension.upper() != ".PDF":
        print("File : " + pdf_file + " is not a PDF File, bypassing the file...")
        continue

    # get the target filename
    target_filename = retrieve_filename(filename)
    doc_file = doc_file_folder + "/" + target_filename + ".docx"

    # check to see if the PDF file is readable or not.
    pdf_filecntrl = open(pdf_file, "r")
    if not pdf_filecntrl.readable():
        print("PDF File is not readable. Quitting")
        exit(-1)
    else:
        pdf_filecntrl.close()

    # check to see if the target file is writable or not.
    doc_filecntrl = open(doc_file, "w")
    if not doc_filecntrl.writable():
        print("DOC File is not writable. Quitting")
        exit(-1)
    else:
        doc_filecntrl.close()

    # Steps below are used to convert PDF to DOCX one file at a time.
    convPDFtoDoc = Converter(pdf_file)
    convPDFtoDoc.convert(doc_file)
    convPDFtoDoc.close()

# End of program.
