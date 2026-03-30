#Задачка 4
from tkinter import *
root = Tk( )

win1 = Frame(root, bg = '#555555')

win1.pack(expand = YES, fill = BOTH)

Label(win1, text = "TOP 1", width=10, height=4, bg='yellow').pack(side=TOP)
Label(win1, text = "LEFT 2", width=10, height=4, bg='red').pack(side=LEFT)
Label(win1, text = "BOTTOM 3", width=10, height=4, bg='green').pack(side=BOTTOM)
Label(win1, text = "RIGHT 4", width=10, height=4, bg='white').pack(side=RIGHT)

win2 = Frame(root, bg='#770077')

win2.pack(expand = YES, fill = X)

Label(win2, text = "x =").pack(side = LEFT, padx = 10, pady = 10)

Entry(win2).pack(side = LEFT, padx = 10, pady = 10, expand = YES, fill = X)
root.mainloop( )
