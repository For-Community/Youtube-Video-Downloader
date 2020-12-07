#Importing Modules 
from logging import root
import tkinter as tk 
from tkinter import *
from pytube import YouTube 
from tkinter import messagebox, filedialog 

root=tk.Tk()

#tittle bro
root.title("Youtube video Downloader")

#Geometry 
root.geometry("600x150")
root.resizable(False, False)
root.configure(bg='#856ff8')



#widgets
def widgets():
    
    head_label =Label(root,text="Youtube Video Downloader",bg='white')
    head_label.grid(row=0,column=1,padx=5,pady=5)
    head_label.config(font=("Aerial", 20))

    link_label = Label(root,text="YT Video Link ",bg='white')
    link_label.grid(row=1,column=0,pady=5,padx=5)

    root.linkText = Entry(root,  width=55, textvariable=video_Link) 
    root.linkText.grid(row=1, column=1, pady=5,  padx=5, columnspan = 2)

    location_label = Label(root,text="Location",bg="White")
    location_label.grid(row=2,column=0,padx=5,pady=5)
  
    root.LocationText = Entry(root, width=40,textvariable=download_Path) 
    root.LocationText.grid(row=2, column=1,pady=5,padx=5) 
   
    browse_B = Button(root,text="Select Folder", command=Browse , width=10, bg='white') 
    browse_B.grid(row=2,  column=2, pady=1,  padx=1) 
   
    Download_B = Button(root, text="Download",command=Download,width=20, bg='white') 
    Download_B.grid(row=3, column=1, pady=3, padx=3) 

def Browse():
    download_Directory=filedialog.askdirectory(initialdir = "YOUR DIRECTORY PATH")
    download_Path.set(download_Directory)
  
def Download():
    
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    getVideo = YouTube(Youtube_link) 
   
     
    videoStream = getVideo.streams.first()  
    videoStream.download(download_Folder) 
   
    
    messagebox.showinfo("SUCCESSFULLY","DOWNLOADED AND SAVED IN\n" + download_Folder) 

video_Link = StringVar() 
download_Path = StringVar() 
  
widgets() 




#loop
root.mainloop()







##Author - Kiran Sethumadhavan