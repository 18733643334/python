from tkinter import *

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry('500x300')
        self.root.title('这是登录窗口')
        self.create_page()


    def create_page(self):
        self.page = Frame(self.root)
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)

