from tkinter import *
from PIL import ImageTk,Image
from SRC.sql_functions import *
import io
import numpy as np
from PIL import Image

root = Tk()
root.title('Image Viewer')
root.geometry('500x500')
#fetch all the images from my dataframe
df=get_all_data()

def get_image(path):
    img=ImageTk.PhotoImage(Image.open(path))
    return img

image_list = [get_image(path) for path in df['face_path']]

my_label = Label(image = image_list[0])
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number+1])
	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))
	

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)

def back(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))

	if image_number == 1:
		button_back = Button(root, text="<<", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)



button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(0))


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
root.attributes("-topmost", True)
root.after_idle(root.attributes,'-topmost',False)