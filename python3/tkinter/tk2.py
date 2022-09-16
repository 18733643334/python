import tkinter as tk

window = tk.Tk()
window.title('这是一个窗口')
window.geometry('500x500')

e = tk.Entry(window, show=None)
e.pack()


def insert_point():
    var = e.get()
    t.insert('insert', var)


def insert_end():
    var = e.get()
    t.insert('end', var)


b1 = tk.Button(window, text='制定位置追加', width=15, bg='blue', command=insert_point)
b1.pack()

b2 = tk.Button(window, text='尾部追加', width=15, command=insert_end)
b2.pack()
t = tk.Text(window)
t.pack()

window.mainloop()
