import os
import ntpath
import ctypes
from pdf2docx import Converter
import tkinter as tk


# function to retrieve filename from absolute path.
def retrieve_filename(path_and_filename):
    # Split the filename and pathname
    path_name, file_name = ntpath.split(path_and_filename)
    # return filename if it exists or else the whole path as is.
    return file_name or ntpath.basename(path_name)


# Styles:
# 0 : OK
# 1 : OK | Cancel
# 2 : Abort | Retry | Ignore
# 3 : Yes | No | Cancel
# 4 : Yes | No
# 5 : Retry | Cancel
# 6 : Cancel | Try Again | Continue
def popup_msg(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


# Steps below are used to convert PDF to DOCX one file at a time.
def call_external_convert(pdf_file, doc_file):
    conv_PDF_to_Doc = Converter(pdf_file)
    conv_PDF_to_Doc.convert(doc_file)
    conv_PDF_to_Doc.close()
    return True


def convert_pdf_to_docx():
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()

    popup_msg("ConvertPDF2Docx", "Please provide the PDF (source) Filename/Filenames", 0)

    # opens file dialog to select multiple PDF files.
    pdf_files = filedialog.askopenfilenames()

    popup_msg("ConvertPDF2Docx", "Please provide the DOC (target) folder", 0)

    # opens folder dialog to select target folder path.
    doc_file_folder = filedialog.askdirectory()

    # declare return value placeholder to identify if there was
    # at the least one successful conversion.
    ret_val = False

    # Iterate through list of PDF files selected and convert the same to docx.
    for pdf_file in pdf_files:
        # check to make sure the files selected are indeed PDF files.
        filename, file_extension = os.path.splitext(pdf_file)
        if file_extension.upper() != ".PDF":
            popup_msg("ConvertPDF2Docx", "File : " + pdf_file +
                      " is not a PDF File, bypassing the file...", 0)
            continue

        # get the target filename
        target_filename = retrieve_filename(filename)
        doc_file = doc_file_folder + "/" + target_filename + ".docx"

        # check to see if the PDF file is readable or not.
        pdf_file_id = open(pdf_file, "r")
        if not pdf_file_id.readable():
            popup_msg("ConvertPDF2Docx", "PDF File is not readable. bypassing the file...", 0)
            pdf_file_id.close()
            continue
        pdf_file_id.close()

        # check to see if the target file is writable or not.
        doc_file_id = open(doc_file, "w")
        if not doc_file_id.writable():
            popup_msg("ConvertPDF2Docx", "DOC File is not writable. bypassing the file...", 0)
            doc_file_id.close()
            continue
        doc_file_id.close()

        # Call CovertPDF2Docx function
        ret_val = call_external_convert(pdf_file, doc_file)

    return ret_val


# run main program
if convert_pdf_to_docx():
    popup_msg("ConvertPDF2Docx", "PDF/PDFs were converted successfully to Microsoft documents", 0)
else:
    popup_msg("ConvertPDF2Docx", "Conversion of PDF/PDFs to Microsoft documents FAILED!!!", 0)

# End of program.
