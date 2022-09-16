import tkinter as tk
import tkinter.messagebox
from PIL import Image, ImageTk

window = tk.Tk()
window.title('登录窗口')
window.geometry('450x400')

# 加载图片
canvas = tk.Canvas(window, height=170, width=500)
photo = ImageTk.PhotoImage(Image.open('/Users/shihongxiao/www/python3/tkinter/1596616898432.jpg'))
image = canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.pack(side='top')
var_user_name = tk.StringVar()
var_user_name.set('请输入账号')
var_user_pwd = tk.StringVar()
tk.Label(window, text='账号：').place(x=50, y=230)
tk.Entry(window, textvariable=var_user_name).place(x=100, y=230)
tk.Label(window, text='密码：').place(x=50, y=270)
tk.Entry(window, textvariable=var_user_pwd, show='*').place(x=100, y=270)


def login():
    user_name = var_user_name.get()
    print(user_name)
    if not user_name:
        tk.messagebox.showwarning(message='账号未填写')
        return
    password = var_user_pwd.get()
    print(password)
    if not password:
        tk.messagebox.showwarning(message='密码未填写')
        return
    if not user_name.islower():
        tk.messagebox.showwarning(message='账号格式有误')
        return
    

def register():
    tk.messagebox.showinfo(message='注册成功')


tk.Button(window, text='登录', command=login).place(x=50, y=310)
tk.Button(window, text='注册', command=register).place(x=210, y=310)

window.mainloop()
