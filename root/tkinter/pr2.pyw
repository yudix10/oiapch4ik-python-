#Задачка 2

root = Tk( )
root.geometry("400x200+150+100")
root.title("Hello world!!!")
w = Label(root, text = "Hello config world", bg = 'red')
w['fg'] = 'black'
w.config(height=3, width=20,bd=8,relief="raised")
w.config(cursor = "cross")
w.pack(side = TOP, expand = YES, fill = BOTH)

root.mainloop( )