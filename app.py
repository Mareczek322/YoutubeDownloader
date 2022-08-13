import tkinter as tk
from tkinter import ACTIVE, DISABLED, filedialog, Text, messagebox
import os
from pytube import YouTube

root = tk.Tk()

dirname = "/home/mark/Downloads"
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        dirname = f.read()

link = tk.StringVar()
download_type = "Video"



def addApp():
    global dirname
    dirname = filedialog.askdirectory(initialdir=os.path.expanduser("~")+"/Downloads/", title="Select Folder")
    currentDir.config(text=f"Current Directory: {dirname}")


def download():
    print(download_type)
    yt = YouTube(link.get())
    if download_type == "Video":
        yd = yt.streams.get_highest_resolution()
    else:
        yd = yt.streams.filter(only_audio=True).first()
    out_file = yd.download(dirname)
    if download_type == "Audio":
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
    linkEntry.delete(0, tk.END)
    messagebox.showinfo("Success!",f"{download_type} Successfully Downloaded")

def setType(type):
    global download_type
    download_type = type
    if type == "Video":
        videoBtn.configure(state=DISABLED)
        audioBtn.configure(state=ACTIVE)
    else:
        videoBtn.configure(state=ACTIVE)
        audioBtn.configure(state=DISABLED)


title = tk.Label(root, text="Youtube Downloader", font=("Arial", 25))
title.pack()

linkLabel = tk.Label(root, text="Paste Link", font=("Arial", 15)).pack()
linkEntry = tk.Entry(root,textvariable = link, font=('calibre',10,'normal'))
linkEntry.pack()

openFolder = tk.Button(root, text="Open Folder", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFolder.pack()

currentDir = tk.Label(root, text=f"Current Directory: {dirname}")
currentDir.pack()

videoBtn = tk.Button(root, text="Video", padx=10, pady=5, fg="white", bg="#263D42", state=DISABLED, command=lambda:setType("Video"))
videoBtn.pack()

audioBtn = tk.Button(root, text="Audio", padx=10, pady=5, fg="white", bg="#263D42", command=lambda:setType("Audio"))
audioBtn.pack()

downloadBtn = tk.Button(root, text="Download", padx=10, pady=5, fg="white", bg="#263D42", font=("Arial", 25), command=download)
downloadBtn.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    f.write(dirname)
