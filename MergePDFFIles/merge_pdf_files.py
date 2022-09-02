"""Application to merge multiple PDFs to one PDF document"""
import os
import ntpath
import ctypes
import sys
import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfFileMerger


# function to retrieve filename from absolute path.
def retrieve_filename(path_and_filename):
    """Splits filename and path"""
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
    """Creates a popup window for messaging"""
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def merge_multiple_pdfs_into_one():
    """Function to handle merging multiple PDFs to one"""
    root = tk.Tk()
    root.withdraw()

    popup_msg("MergePDFFiles", "Please select multiple PDF(source) Filenames", 0)

    # opens file dialog to select multiple PDF files.
    pdf_files = filedialog.askopenfilenames()

    popup_msg("MergePDFFiles", "Please provide the target folder to save the merged PDF", 0)

    # opens folder dialog to select target folder path.
    doc_file_folder = filedialog.askdirectory()

    # get the target filename
    target_filename = "MergedPDF.pdf"
    doc_file = doc_file_folder + "/" + target_filename

    # check to see if the target file is writable or not.
    with open(doc_file, "w", encoding="utf-8") as doc_file_id:
        if not doc_file_id.writable():
            popup_msg("MergePDFFiles", "Target PDF File is not writable. bypassing the file...", 0)
            doc_file_id.close()
            sys.exit(99)
        doc_file_id.close()

    # Create an instance of PdfFileMerger() class
    merger = PdfFileMerger()

    # declare return value placeholder to identify if there was
    # at the least one successful PDF merge.
    ret_val = False

    # Iterate through list of PDF files selected and convert the same to docx.
    for pdf_file in pdf_files:
        # check to make sure the files selected are indeed PDF files.
        filename, file_extension = os.path.splitext(pdf_file)
        if file_extension.upper() != ".PDF":
            popup_msg("MergePDFFiles", "File : " + filename + file_extension +
                      " is not a PDF File, bypassing the file...", 0)
            continue

        # check to see if the PDF file is readable or not.
        with open(pdf_file, "r", encoding="utf-8") as pdf_file_id:
            if not pdf_file_id.readable():
                popup_msg("MergePDFFiles", "PDF File is not readable. bypassing the file...", 0)
                pdf_file_id.close()
                continue
            pdf_file_id.close()

        # Append PDF files
        merger.append(pdf_file)
        ret_val = True

    if ret_val:
        # Write out the merged PDF
        merger.write(doc_file)
        merger.close()

    # return the flag to indicate successful/unsuccessful merger
    return ret_val


IS_MERGE_SUCCESSFUL = merge_multiple_pdfs_into_one()

if IS_MERGE_SUCCESSFUL:
    popup_msg("MergePDFFiles", "Merging Multiple PDF File was Successful.", 0)
else:
    popup_msg("MergePDFFiles", "Merging Multiple PDF File was Unsuccessful.", 0)
