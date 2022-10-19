"""Application to download YouTube video and convert it into Mp3"""
# importing packages
import ctypes
import ntpath
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog

from pytube import YouTube


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


# Main function to download YouTube Video.
def download_you_vid_in_mp3():
    """Function to download YouTube video in MP3 format."""
    root = tk.Tk()
    root.withdraw()

    # opens a simple file dialog to enter YouTube URL.
    youtube_url = simpledialog.askstring(title="YouTubeVideoMp3",
                                         prompt="Please input a valid YouTube URL:")

    # Check if the URL exists or not.
    if len(youtube_url) <= 0:
        popup_msg("YouTubeVideoMp3", "Provided YouTube URL is empty!", 0)
        return False, "Youtube file"

    popup_msg("YouTubeVideoMp3", "Please provide the target folder to save the MP3 file", 0)

    # opens folder dialog to select target folder path.
    mp3_file_folder = filedialog.askdirectory()

    # Check if the URL exists or not.
    if len(mp3_file_folder) <= 0:
        popup_msg("YouTubeVideoMp3", "Provided destination directory is empty!", 0)
        return False, "Youtube file"

    # url input from user
    youtube_obj = YouTube(youtube_url)

    # extract only audio
    video = youtube_obj.streams.filter(only_audio=True).first()

    # download the file
    out_file = video.download(output_path=mp3_file_folder)

    # save the file
    # Get the filename as step 1
    base_file_name_with_ext = retrieve_filename(out_file)

    # split the filename from extension as step 2.
    filename = os.path.splitext(base_file_name_with_ext)

    # Ready the Target MP3 filename.
    new_file = filename[0] + '.mp3'

    # Rename the original file to Mp3.
    os.rename(out_file, mp3_file_folder + "/" + new_file)
    return True, youtube_obj.title


# Call main module to download YouTube Video and convert it into Mp3 format.
is_successful, destination_file_title = download_you_vid_in_mp3()
if is_successful:
    popup_msg("YouTubeVideoMp3", "Converting " + destination_file_title + " was successful", 0)
else:
    popup_msg("YouTubeVideoMp3", "Converting " + destination_file_title + " was Unsuccessful", 0)
