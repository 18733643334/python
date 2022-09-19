# from .pages.LoginPage import LoginPage as lp
from tk_project.project.pages.LoginPage import LoginPage
from tk_project.project.pages.MovPage import MovPage
import tkinter as tk

root = tk.Tk()
MovPage(root)
root.mainloop()
