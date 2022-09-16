from tkinter import *
root = Tk()
root.geometry('450x500')
root.title('计算器')
frame_show = Frame(width=300,height=150,bg='#dddddd')

#顶部区域

v = StringVar()
v.set('0')
show_label = Label(frame_show,textvariable =v, bg = 'white',width=12,height=1,font=("黑体", 20, "bold"),justify=LEFT,anchor='e')
show_label.pack(padx = 10,pady = 10)
frame_show.pack()

#是否按下了运算符
isopear = False

#操作序列
calc = []
def change(num):
    global isopear
    if isopear == False:
        if v.get() == '0':
            v.set('')
            v.set(num)
        else:
            v.set(v.get()+num)
    else:
        v.set(num)
        isopear = False

#运算
def operation(sign):
    global isopear
    global calc
    isopear = True
    calc.append(v.get())
    if sign == '+':
        calc.append('+')
    elif sign == '-':
        calc.append('-')
    elif sign == '*':
        calc.append('*')
    elif sign == '/':
        calc.append('/')
    print(calc)

def equal():
    global calc
    #获取当前界面的数值准备运算
    calc.append(v.get())
    print(calc)
    #组成运算字符串
    calcstr = ''.join(calc)
    #检测最后一位是否是运算符，是就删除
    if calcstr[-1] in '+-*/':
        calcstr = calcstr[0:-1]
    #print(calcstr)
    #运算操作
    result = eval(calcstr)
    #显示结果
    v.set(result)
    calc.clear()

#删除操作
def delete():
    if v.get() == '' or v.get() == '0':
        v.set('0')
        return
    else:
        num = len(v.get())
        if num > 1:
            strnum = v.get()
            strnum = strnum[0:num-1]
            v.set(strnum)
        else:
            v.set('0')

#清空操作
def clear():
    global calc
    calc = []
    v.set('0')
    isopear = False

#正负操作
def fan():
    strnum = v.get()
    if strnum[0] == '-':
        v.set(strnum[1:])
    elif strnum[0] != '-' and strnum != '0' :
        v.set('-'+strnum)

#按键区域
frame_bord = Frame(width=400,height=350,bg='#cccccc')
button_del = Button(frame_bord,text = '←',width = 5,height =1,command = delete).grid(row = 0,column = 0)
button_clear = Button(frame_bord,text = 'C',width = 5,height =1,command = clear).grid(row = 0,column = 1)
button_fan = Button(frame_bord,text = '±',width = 5,height =1,command = fan).grid(row = 0,column = 2)
button_ce = Button(frame_bord,text = 'CE',width = 5,height =1,command = clear).grid(row = 0,column = 3)
button_1 = Button(frame_bord,text = '1',width = 5,height =2,command = lambda:change('1')).grid(row = 1,column = 0)
button_2 = Button(frame_bord,text = '2',width = 5,height =2,command = lambda:change('2')).grid(row = 1,column = 1)
button_3 = Button(frame_bord,text = '3',width = 5,height =2,command = lambda:change('3')).grid(row = 1,column = 2)
button_jia = Button(frame_bord,text = '+',width = 5,height =2,command = lambda:operation('+')).grid(row = 1,column = 3)
button_4 = Button(frame_bord,text = '4',width = 5,height =2,command = lambda:change('4')).grid(row = 2,column = 0)
button_5 = Button(frame_bord,text = '5',width = 5,height =2,command = lambda:change('5')).grid(row = 2,column = 1)
button_6 = Button(frame_bord,text = '6',width = 5,height =2,command = lambda:change('6')).grid(row = 2,column = 2)
button_jian = Button(frame_bord,text = '-',width = 5,height =2,command = lambda:operation('-')).grid(row = 2,column = 3)
button_7 = Button(frame_bord,text = '7',width = 5,height =2,command = lambda:change('7')).grid(row = 3,column = 0)
button_8 = Button(frame_bord,text = '8',width = 5,height =2,command = lambda:change('8')).grid(row = 3,column = 1)
button_9 = Button(frame_bord,text = '9',width = 5,height =2,command = lambda:change('9')).grid(row = 3,column = 2)
button_cheng = Button(frame_bord,text = 'x',width = 5,height =2,command = lambda:operation('*')).grid(row = 3,column = 3)
button_0 = Button(frame_bord,text = '0',width = 5,height =2,command = lambda:change('0')).grid(row = 4,column = 0)
button_dian = Button(frame_bord,text = '.',width = 5,height =2,command = lambda:change('.')).grid(row = 4,column = 1)
button_deng = Button(frame_bord,text = '=',width = 5,height =2,command = equal).grid(row = 4,column = 2)
button_chu = Button(frame_bord,text = '/',width = 5,height =2,command = lambda:operation('/')).grid(row = 4,column = 3)
frame_bord.pack(padx = 10,pady = 10)

root.mainloop()