#Задачка 1

from tkinter import*
def hello():
    print("На кнопку нажали")
Label(text="Hello Поличка (люблю <3)").pack(side=TOP)
Button(text = "Тыкни!", command=hello).pack(side=BOTTOM)

mainloop( )