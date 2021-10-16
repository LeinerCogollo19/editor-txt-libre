from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
 
 
def load():
    with open(filename.get()) as file:
        contents.delete('1.0', END)
        contents.insert(INSERT, file.read())
 
 
def save():
    with open(filename.get(), 'w') as file:
        file.write(contents.get('1.0', END))


 
 
top = Tk()
top.title("editor de texto libre")
top.geometry('800x600')
 
contents = ScrolledText()
contents.pack(side=BOTTOM, expand=True, fill=BOTH)
filename = Entry(top)
filename.pack(side=LEFT)
Button(text='Abrir', command=load).pack(side=LEFT)
Button(text='Guardar', command=save).pack(side=LEFT)
 
top.mainloop()