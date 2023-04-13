import customtkinter as ctk
import tkinter as tk
from pytube import YouTube as yt


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()

btn_text = "Download"
url_var = tk.StringVar()

def start_download():
    try:
        video_url = textBox.get()
        video = yt(video_url, on_progress_callback=on_progress)
        video_res =  video.streams.get_highest_resolution()
        if video_res.exists_at_path('./downloads/'):
            finish_label.configure(text="Video already exsists", text_color="blue")
        else:
            title.configure(text=video.title, text_color="white")
            finish_label.configure(text="")
            video_res.download('./downloads/')
    except:
         finish_label.configure(text="Downloaded Unsuccessfull...Invalid URL" ,text_color="red")
         title.configure(text="Youtube Video Downloader", text_color="white")

    finish_label.configure(text="Downloaded Successfully...", text_color="yellowgreen")
    title.configure(text="Youtube Video Downloader", text_color="white")



def on_progress(stream, shuck, bytes_remaining):
    total_size = stream.filesize
    bytes_download = total_size - bytes_remaining
    perc = bytes_download / total_size * 100
    per = str(int(perc))
    prec_txt.configure(text=per+'%')
    prec_txt.update()
    prec_bar.set(float(perc)/100)



app.title("Clerov Downloader")
app.geometry("720x480")

logo = ctk.CTkLabel(master=app, text="CLEROV", text_color="blue", font=('monospace', 30))
logo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

title = ctk.CTkLabel(master=app, text="Youtube Video Downloader", text_color="white", font=('', 20))
title.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

textBox = ctk.CTkEntry(master=app,placeholder_text="Paste video URL here...",textvariable=url_var, width=400, height=40)
textBox.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

button = ctk.CTkButton(master=app, text=btn_text , width=160, command=start_download,height=40, fg_color='blue', hover_color='darkblue')
button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)


finish_label = ctk.CTkLabel(master=app, text="")
finish_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

prec_txt = ctk.CTkLabel(master=app, text="0%")
prec_bar = ctk.CTkProgressBar(master=app, width=400, progress_color="blue")
prec_bar.set(0)
prec_txt.place(relx=0.8, rely=0.3, anchor=tk.CENTER)
prec_bar.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

app.mainloop()

