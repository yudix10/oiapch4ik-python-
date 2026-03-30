#Задачка 3
from tkinter import *
root = Tk( )
root.title("Привет мир!!!")

lab1 = Label(root, text = "Текст на метке", bg = '#F5F5F5', fg = '#0000FF',
 font = ('times', 20, 'bold'))

lab1.pack(side = TOP, expand = YES, fill = BOTH)

def oncommand(x):
 print("Нажали на кнопку", x)

def onclick(event):

 print("Нажали на кнопку %s X = %s Y = %s" % (event.widget, event.x, event.y))

 x = int(str(but3["padx"]))
 x += 1
 but3.config(padx = x, pady = x)

but1 = Button(root, text = "кнопка 1", command = (lambda: oncommand(1)))
but1.pack( )
but2 = Button(root, text = "кнопка 2", command = (lambda: oncommand(2)))
but2.pack( )

but3 = Button(root)
but3.config(text = "кнопка 3")

but3.bind("<Button-1>", onclick)
but3.pack( )
root.mainloop( )
