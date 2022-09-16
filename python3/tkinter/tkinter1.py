import tkinter as tk

window = tk.Tk()
window.title('窗口')
window.geometry('500x500')

text1 = tk.StringVar()
a = tk.Label(window, textvariable=text1, width=100, height=2, bg='green')
a.pack()

hit_status = False
def submit():
    global hit_status
    if hit_status == False:
        hit_status = True
        text1.set('弄啥嘞')
    else:
        hit_status = False
        text1.set('')


b = tk.Button(window, text='按钮', bg='blue',
              width=150, height=50, command=submit)
b.pack()

window.mainloop()
