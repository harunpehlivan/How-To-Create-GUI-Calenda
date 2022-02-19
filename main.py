#required module 

import calendar

#required module -pip install tkintertable

from tkinter import *

#Getting calendar of 2020

cal = calendar.calendar(2022)

#initializing window 

root = Tk()


#setting window title

root.title("2022 calendar")


#Adding label to window which contain calendar

c = Label(root, text=cal,font='times 12 bold',bg='red')

c.pack()

#mainloop

root.mainloop()