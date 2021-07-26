#!/usr/bin/env python3
"""
	User chooses level, that is number of titles.
"""

from tkinter import *
from PIL import Image, ImageTk
import re
__author__ = "Hailey Johnson, Krikor Herlopian, Charitha Sree Jayaramireddy , Syrina Haldiman and Tatiyana Bramwell"
__copyright__ = "Copyright 2021, University of New Haven Final Project"

"""
	This page to allow the user to choose the level of the game.
	Level 1 means 2*2
	Level 2 means 5*5
	Level 3 means 6*6
	Level 4 means 8*8
	Level 5 means 10*10
"""

def center_window(width=250, height=100):
	"""
		center screen on window
	"""
		
	# get screen width and height
	screen_width = master.winfo_screenwidth()
	screen_height = master.winfo_screenheight()	
	# calculate position x and y coordinates
	x = (screen_width/2) - (width/2)
	y = (screen_height/2) - (height/2)
	master.geometry('%dx%d+%d+%d' % (width, height, x, y))



master = Tk()
master.title("Set - Level")
center_window(407,85)


def onClick(i):
    #update lev.txt file with new level number.
    with open("lev.txt", "w") as f:
        f.write(str(i))
    print(str(i))#this returns value to caller
    master.destroy()
    return



u = 10
level = [1,2,3,4,5]
l = 0

for i in range(1,6):
    level_button = Button(master,compound = "center",text = level[l], width = 3, height = 1,font=('arial 15 bold'),highlightbackground = "light blue",bg = "light blue", fg = 'midnight blue', command=lambda i=i: onClick(i))
    level_button.place(x = u, y = 10)
    l = l + 1
    u = u + 90


mainloop()
