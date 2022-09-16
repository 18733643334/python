# coding:utf-8
import tkinter as Tk
import tkMessageBox as message


def create_excel():
    message.showinfo('通知', '开始生成')


def create_window():
    window = Tk.Tk()
    window.minsize(800, 600)
    window.maxsize(1200, 1000)

    Tk.Label(window, text='项目名称：').place(x=50, y=15)
    project_name = Tk.StringVar()
    project_name.set('请输入项目')
    Tk.Entry(window, textvariable=project_name).place(x=120, y=15)

    Tk.Label(window, text='选择类型：').place(x=50, y=50)
    Tk.Radiobutton(window, text='镜头', value=1).place(x=120, y=50)
    Tk.Radiobutton(window, text='资产', value=2).place(x=200, y=50)

    b1 = Tk.Button(window, text='生成EXCEL', command='create_excel', bg='#00FFFF')

    window.mainloop()


if __name__ == '__main__':

    create_window()

