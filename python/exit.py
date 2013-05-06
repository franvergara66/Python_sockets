#! /python25/python.exe
#! -*- coding: utf-8 -*-

"""Minimal Tkinter example for showing how to connect a button
to an event and using multiple ways of terminating the program."""

import Tkinter
import sys

def on_button1_click():
    sys.exit(0)
    
def on_button2_click():
    root.destroy()
    
def on_button3_click():
    root.quit()

root = Tkinter.Tk()
frame = Tkinter.Frame(root)
frame.pack()

button1 = Tkinter.Button(frame, text="use sys.exit()", command=on_button1_click)
button1.pack()

button2 = Tkinter.Button(frame, text="use self.destroy()", command=on_button2_click)
button2.pack()

button3 = Tkinter.Button(frame, text="use self.quit()", command=on_button3_click)
button3.pack()

root.mainloop()