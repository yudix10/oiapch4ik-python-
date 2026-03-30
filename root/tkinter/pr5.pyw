# #Задачка 5
from tkinter import *
from tkinter.messagebox import *
root = Tk( )

root.minsize(width = 350, height = 150)
root.maxsize(width = 500, height = 300)
root.title("Калькулятор") # заголовок окна

fr_xy = Frame(root)
fr_xy.pack(side = TOP, expand = YES, fill = X)
lx = Label(fr_xy, text = "x = ")
lx.pack(side = LEFT, padx = 10, pady = 10)
entX = Entry(fr_xy)
entX.insert(0, 0)
entX.pack(side = LEFT, padx=10, pady=10)
entX.focus( )
ly = Label(fr_xy, text = "y = ")
ly.pack(side=LEFT, padx=10, pady=10)
entY = Entry(fr_xy)
entY.insert(0, 0)
entY.pack(side = LEFT, padx=10, pady=10)

fr_op = LabelFrame(root, text = "Операция:")
fr_op.pack(side = TOP, expand=YES, fill=X)

oper = ['+', '-', '*', '/'] # – список операций

varOper = StringVar( )

for op in oper:
 Radiobutton(fr_op, text = op, variable = varOper, value = op).pack(side = LEFT,
 padx = 20, pady = 10)
varOper.set(oper[0]) # Устанавливаем текущее значение ‘+’

fr_res = Frame(root)
fr_res.pack(side = TOP, expand = YES, fill = BOTH)

def OnButtunResult( ):

 try:
    x = float(entX.get())
 except ValueError:
    showerror("Ошибка заполнения", "Переменная x не является числом")
    return

 try:
    y = float(entY.get())
 except ValueError:
    showerror("Ошибка заполнения", "Переменная y не является числом")
    return

 op = varOper.get( )

 if op == '+': res = x + y
 elif op == '-': res = x - y
 elif op == '*': res = x * y
 elif op == '/':
    if y != 0: res = x / y
    else: res = 'NAN'
 else:
    res = 'операция выбрана неправильно'

 lres['text'] = res


Button(fr_res, text = "=", width = 10, command = OnButtunResult).pack(side = LEFT,
 padx = 30, pady = 20)
lres = Label(fr_res, text = "")
lres.pack(side = LEFT, padx = 30, pady = 20)

root.mainloop( )