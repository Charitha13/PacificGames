#!/usr/bin/env python3
"""
	When user wins this game, this page will be displayed. Congratulations Image.
	It wil close by itself after four seconds.
"""
from tkinter import *
from PIL import ImageTk, Image

__author__ = "Charitha Sree Jayaramireddy ,Hailey Johnson, Krikor Herlopian,  Syrina Haldiman and Tatiyana Bramwell"
__copyright__ = "Copyright 2021, University of New Haven Final Project"

def center_window(width=800, height=800):
	"""
		this will center the screen on window
	"""
	# get screen width and height
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	# calculate position x and y coordinates
	x = (screen_width/2) - (width/2)
	y = (screen_height/2) - (height/2)
	root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
root = Tk()
root.title("Jigsaw - Congratulations")

center_window()
back_img = Image.open('congrats1.png')
back_img = back_img.resize((770, 770), Image.ANTIALIAS)
back_img1 = ImageTk.PhotoImage(back_img)
background_label = Label(root, image=back_img1, compound = "left", bg = "white", fg = None)
background_label.pack(side = "top", fill ="both")
background_label.place(x=0, y=0, relwidth = 1, relheight = 1)
i = 0
#this will close the page
def destroy():
    root.destroy()

#after four seconds call destroy
root.after(4000, destroy)

root.mainloop()
