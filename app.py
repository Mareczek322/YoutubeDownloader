import tkinter as tk
from tkinter import filedialog, Text, messagebox
import os
from pytube import YouTube

root = tk.Tk()

dirname = "/home/mark/Downloads"
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        dirname = f.read()

link = tk.StringVar()



def addApp():
    global dirname
    dirname = filedialog.askdirectory(initialdir=os.path.expanduser("~")+"/Downloads/", title="Select Folder")
    currentDir.config(text=f"Current Directory: {dirname}")


def download():
    yt = YouTube(link.get())
    yd = yt.streams.get_highest_resolution()
    yd.download(dirname)
    linkEntry.delete(0, tk.END)
    messagebox.showinfo("Success!","Video Successfully Downloaded")

title = tk.Label(root, text="Youtube Downloader", font=("Arial", 25))
title.pack()

linkLabel = tk.Label(root, text="Paste Link", font=("Arial", 15)).pack()
linkEntry = tk.Entry(root,textvariable = link, font=('calibre',10,'normal'))
linkEntry.pack()

openFolder = tk.Button(root, text="Open Folder", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFolder.pack()

currentDir = tk.Label(root, text=f"Current Directory: {dirname}")
currentDir.pack()

downloadBtn = tk.Button(root, text="Download", padx=10, pady=5, fg="white", bg="#263D42", command=download)
downloadBtn.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    f.write(dirname)