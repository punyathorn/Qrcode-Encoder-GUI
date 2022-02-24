import qrcode
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
from tkinter import messagebox
import sys
GUI = Tk()
GUI.title("QR Encoder")
GUI.geometry("1000x500")
GUI.iconbitmap('Qr.ico')
menubar = Menu(GUI)
GUI.config(menu=menubar)

def EX():
    exit = messagebox.askyesno('Exit', 'Do you want to exit the program?')
    if exit == True:
        sys.exit()

def Info():
    messagebox.showinfo(title="Information", message=" My Github: https://github.com/punyathorn\n")

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command= EX)
info_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Info", menu=info_menu)
info_menu.add_command(label="Info", command= Info)

Big = (None,25)
Medium = (None, 20)
small = (None, 12)

Title = Label(GUI, text="QR Encoder", font=Big)
Title.pack(pady=30)

Content = StringVar()
Content_Label = Label(GUI, text="Content to Encode:", font=Medium)
Content_Label.place(x= 25, y= 100)
Content_Entry = ttk.Entry(GUI, textvariable= Content, font= Medium, width= 28)
Content_Entry.place(x= 275, y=100)
Output_QR = Label(GUI, text="Output QRCode", font=Medium)
Output_QR.place(x= 750, y = 100)

file_options = [
    "Select file type",
    "JPG             ",
    "JPEG            ",
    "PNG             ",
]

file_select = tkinter.StringVar()
drop = ttk.OptionMenu( GUI , file_select , *file_options )
drop.place(x= 35, y= 250)
File_Name = StringVar()
File_Name_Label = Label(GUI, text="File Name :", font=Medium)
File_Name_Label.place(x= 25, y= 200)
File_Name_Entry = ttk.Entry(GUI, textvariable= File_Name, font= Medium, width= 34)
File_Name_Entry.place(x= 175, y=200)

def Gen():
    file_type= file_select.get()
    content_encode = Content.get()
    file = File_Name.get()
    if content_encode== "" or file == "" or file_type=="Select file type":
        messagebox.showwarning(title="Warning", message="Please fill in all the required fields!")
    else:
        if file_type == "JPG             ":
            file_type= ".jpg"
        elif file_type == "JPEG            ":
            file_type= ".jpeg"
        elif file_type == "PNG             ":
            file_type= ".png"
        filename_encode = file+file_type
        img = qrcode.make(content_encode)
        img.save(filename_encode)
        Name = filename_encode
        image1 = Image.open(Name)
        image1= image1.resize((250,250), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image1)
        global label1
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x= 725, y= 145)
def cancel():
    Content.set(" ")
    File_Name.set(" ")
    label1.destroy()

Version = Label(GUI, text="Version 2.0.7", font=small)
Developedby = Label(GUI, text="Developed by: punyathorn", font= small)
Version.place(x= 570, y= 325)
Developedby.place(x= 400, y= 325)

Generate = Button(GUI, text="Generate", command= Gen)
Generate.place(x= 31, y= 300, width= 150, height= 75)

Cancel = Button(GUI, text="Cancel", command= cancel)
Cancel.place(x= 200, y= 300, width= 150, height= 75) 

GUI.mainloop()