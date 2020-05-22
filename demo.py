from tkinter import *
from PIL import ImageTk
import PIL.Image
from tkinter import filedialog
import subprocess
from SRC.sql_functions import *
import pyautogui

df=get_all_data()

'''HEIGHT = 1000
WIDTH = 1000'''
TK_SILENCE_DEPRECATION=1
window = Tk()
window.title("Faces-detector app")
window.configure(bg='black')
window.geometry('900x1000')

# background
image = PIL.Image.open("INPUT/camera.jpg")
background_image = ImageTk.PhotoImage(image)
background_label = Label(window, image=background_image,bg='#000000')
background_label.place(relwidth=1, relheight=1.3)

# title
label = Label(window, text="Faces-detector",bg='#000000',fg="white", width=100, font="Helvetica 60")#'#073143'
label.place(relx=0.5, rely=0.03, relwidth=1, relheight=0.15, anchor='n')

#subtitle
lbl = Label(window, text="Hello, welcome to the Faces-detector app!!!\n Webcam or youtube video?",bg='#000000',fg="white",justify=LEFT,font="Helvetica 30")
lbl.place(x=10,y=120)

def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])

def clicked():
    lbl = Label(window, text="You chose the Webcam! Please, wait few seconds...",bg='#000000',fg="white")
    lbl.place(x=300,y=350)
    choice='0'
    cmd = f"python3 main1.py --url '{choice}'"
    bash_command(cmd)

def clicked1():
    choice=txt.get()
    print('this is the chosen youtube video url: ',choice)
    cmd = f"python3 main1.py --url '{choice}'"
    bash_command(cmd)

def clicked2():
    cmd = "python3 display_images.py"
    bash_command(cmd)

#def clicked3():
    #pyautogui.press('q')

#enter youtube url
lbl = Label(window, text="Enter your youtube url and press \'start youtube video\'",bg='#000000',fg="white")
lbl.place(x=10,y=230)
txt = Entry(window,width=42,bg='#000000',fg="white")
txt.place(x=10,y=250)

#buttons to select the youtube video
btn = Button(window, text="Start youtube video" ,command=clicked1,  width = 40)
btn.place(x=10,y=300)
btn.configure(foreground='black', relief='groove')

#buttons to select te webcam
btn = Button(window, text="Start webcam",command=clicked, width = 40,bg='#000000',fg="white")
btn.configure(foreground='black', relief='groove')
btn.place(x=10,y=350)

#buttons to get the report 
btn = Button(window, text="Get the report" ,command=clicked2,  width = 40)
btn.place(x=10,y=590)
btn.configure(foreground='black', relief='groove')

#buttons to esc
btn = Button(window, text="Stop" ,command=window.quit,  width = 40)
btn.place(x=10,y=400)
btn.configure(foreground='black', relief='groove')


window.mainloop()
window.attributes("-topmost", True)
window.after_idle(window.attributes,'-topmost',False)

#https://www.youtube.com/watch?v=tCCx9vEvOHs