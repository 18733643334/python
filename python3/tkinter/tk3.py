import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('这是一个窗口')
window.geometry('500x500')


def hit_me():
    tk.messagebox.showinfo(title='提示', message='我草')
    tk.messagebox.showwarning(title='提示', message='我靠')
    tk.messagebox.showerror(title='提示', message='我日')
    res = tk.messagebox.askyesno(title='提示',message='我刺')
    print(res)


b1 = tk.Button(window, text='按钮', command=hit_me).pack()

window.mainloop()
