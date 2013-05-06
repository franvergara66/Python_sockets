from Tkinter import *

def funcion():
   v.set("Password Invalido")

frame = Frame()
button=Button(frame, text="Imprimir", command=funcion)
button.pack(side=BOTTOM)

v = StringVar()
text = Entry(frame, textvariable=v )
text.pack(side=LEFT);

frame.pack()
frame.mainloop()