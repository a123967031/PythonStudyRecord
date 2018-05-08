#!/usr/bin/env python

from Tkinter import *

def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get())

top = Tk()
top.geometry('250x250')

label = Label(top, text='Hello World!', font='Helvetica -12 bold')
label.pack(fill=Y, expand=1)

scale = Scale(top, from_=10, to=40, orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=12)

quit = Button(top, text='QUIT', command=top.quit, activeforeground='blue', activebackground='red')
quit.pack()
mainloop()
