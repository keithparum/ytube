from tkinter import Tk, Button, Label, StringVar, Entry
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from pytube import YouTube

root = Tk()

root.title('Youtube downloader')
root.configure(background="#FF10F0")
root.minsize(width=420, height=100)
root.resizable(width=False, height=False)

# video url https://youtu.be/N_Maw56tLCI

def open_file():
    global directory
    directory = askdirectory()
    print(directory)

def download():
    if len(link.get()) == 0:
        messagebox.showerror("😱 Oh-Oh! 🤨 Link is empty??!", "🙄 Link cannot be empty...tsk tsk")
    else:
        YouTube(link.get()).streams.get_highest_resolution().download(directory)
        messagebox.showinfo("🎉 Done! 😎 You're now a KP💖P Snatcher!", "🥰 Exiting!!! 🤫 But shush! It's totally illegal.")
        link_entry.delete(0, 'end')

title_lbl = Label(root, text="Ytube - Your Fav KP💖P Snatcher!", bg="#98FF98", fg="#FF10F0", font='Helvetica 20')
title_lbl.grid(row=1, column=1)

link_lbl = Label(root, text="Enter link", bg="#98FF98", fg="#FF10F0", font='Helvetica 15')
link_lbl.grid(row=4, column=0)

link = StringVar()
link_entry = Entry(root, textvariable=link, width=50, borderwidth=4)
link_entry.grid(row=4, column=1)

select_dir = Button(root, text="Choose Directory", width=15, bg="#98FF98", fg="#FF10F0", font='Helvetica 15', command=open_file)
select_dir.grid(row=4, column=2)

download_btn = Button(root, text="Download", width=10, bg="#98FF98", fg="#FF10F0", font='Helvetica 15', command=download)
download_btn.grid(row=5, column=1)

root.mainloop()
