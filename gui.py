from tkinter import *
import os
from PIL import ImageTk, Image
import requests
import tw as tww

pic=["happy.resized.png","negativ.resized.png","neutral.resized.png"]

def get_weather(entry):
	
	label['text'] = tww.treat(entry)
	get_picture(tww.treat(entry))

def get_picture(text):
	if text=="positive" or text=="wpositive" or text=="spositve" :
		str1=pic[0]
	if text=="neutral":
		str1=pic[2]
	else:
		str1=pic[1]
	img = ImageTk.PhotoImage(Image.open(str1))
	weather_icon.create_image(0,0, anchor='nw', image=img)
	weather_icon.image = img
	

root = Tk()


canvas=Canvas(root, height = 600, width = 700)
canvas.pack()

frame = Frame(root,bg='#601700',bd=5)
frame.place(relwidth = 0.65, relheight=1)

text = Entry(frame, font=40)
text.place(relwidth=1, relheight=0.1,relx=0,rely=0.2)



submit = Button(frame, text='Get the sentiment', font=40, command=lambda: get_weather(text.get()))
submit.place(relx=0.3, relheight=0.1, relwidth=0.4,rely=0.3)

weather_icon = Canvas(root)
weather_icon.place(relx=.72, rely=0.27)

label = Label(root)
label.place(relx=0.76,rely=0.45)

root.mainloop()
