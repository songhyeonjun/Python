import tkinter
from functools import partial
from tkinter import *

from pythonProject4.cal.cal import Cal

pre_num = ''  # '12'
oper = ''  # '+'
post_num = ''  # '10'
pre_post = True

cal = Cal()

def num(n):
    global pre_num, post_num
    if pre_post:
        pre_num += str(n)
        equation.set(pre_num)
        print(pre_num)
    else:
        post_num += str(n)
        equation.set(post_num)
        print(post_num)


def equal():
    global pre_post, pre_num, post_num, oper
    # 뒤에값 가져다가 정수로 변환
    # 계산하고, 결과값 프린트
    int_pre = int(pre_num)
    int_post = int(post_num)
    if oper == '+':
        # result = int_pre + int_post
        result = cal.plus(int_pre + int_post)
        equation.set(result)
        print(result)
    elif oper == '-':
        result = int_pre - int_post
        equation.set(result)
    elif oper == '*':
        result = int_pre * int_post
        equation.set(result)
    elif oper == '/':
        result = int_pre / int_post
        equation.set(result)
    # else:

    pre_post = True
    pre_num = reset
    post_num = ""
    oper = ""

def reset():
    global pre_num, post_num, oper, pre_post
    pre_num = ""
    post_num = ""
    pre_post = True
    oper = ""
    equation.set("")


def oper(op):
    global oper, pre_post
    oper = op
    equation.set(oper)
    pre_post = False


w = Tk()
w.geometry("340x500")

equation = tkinter.StringVar()

calculation = tkinter.Label(w, textvariable=equation)
equation.set("계산식을 입력하세요 : ")
calculation.grid(row=2, columnspan=8)

b0 = Button(w,
            text='0',
            font=('궁서', 30),
            bg='yellow',
            command=partial(num, 0)
            )
b0.grid(row=6, column=2, padx=10, pady=10)

b1 = Button(w,
            text='1',
            font=('궁서', 30),
            bg='yellow',
            command=partial(num, 1)
            )
b1.grid(row=3, column=1, padx=10, pady=10)

b2 = Button(w,
            text='2',
            font=('궁서', 30),
            bg='yellow',
            command=partial(num, 2)
            )
b2.grid(row=3, column=2, padx=10, pady=10)

b3 = Button(w,
            text='3',
            font=('궁서', 30),
            bg='yellow',
            command=partial(num, 3)
            )
b3.grid(row=3, column=3, padx=10, pady=10)

b4 = Button(w,
            text='4',
            font=('궁서', 30),
            bg='yellow',
            command=partial(num, 4)
            )
b4.grid(row=4, column=1, padx=10, pady=10)

b5 = Button(w,
            text='5',
            font=('궁서', 30),
            bg='yellow',
            command=partial(num, 5)
            )
b5.grid(row=4, column=2, padx=10, pady=10)

b6 = Button(w,
            text='6',
            font=('궁서', 30),
            bg='yellow',
            command=partial(num, 6)
            )
b6.grid(row=4, column=3, padx=10, pady=10)

b7 = Button(w,
            text='7',
            font=('궁서', 30),
            bg='yellow',
            command=partial(num, 7)
            )
b7.grid(row=5, column=1, padx=10, pady=10)

b8 = Button(w,
            text='8',
            font=('궁서', 30),
            bg='yellow',
            command=partial(num, 8)
            )
b8.grid(row=5, column=2, padx=10, pady=10)

b9 = Button(w,
            text='9',
            font=('궁서', 30),
            bg='yellow',
            command=partial(num, 9)
            )
b9.grid(row=5, column=3, padx=10, pady=10)

plus = Button(w,
              text='+',
              font=('궁서', 30),
              bg='yellow',
              command=partial(oper, '+')
              )
plus.grid(row=3, column=4, padx=10, pady=10)

minus = Button(w,
               text='-',
               font=('궁서', 30),
               bg='yellow',
               command=partial(oper, '-')
               )
minus.grid(row=4, column=4, padx=10, pady=10)

multiply = Button(w,
                  text='*',
                  font=('궁서', 30),
                  bg='yellow',
                  command=partial(oper, '*')
                  )
multiply.grid(row=5, column=4, padx=10, pady=10)

divide = Button(w,
                text='/',
                font=('궁서', 30),
                bg='yellow',
                command=partial(oper, '/')
                )
divide.grid(row=6, column=4, padx=10, pady=10)

equal = Button(w,
               text='=',
               font=('궁서', 30),
               bg='yellow',
               command=equal
               )
equal.grid(row=6, column=3, padx=10, pady=10)

clear = Button(w,
               text='c',
               font=('궁서', 30),
               bg='yellow',
               command=reset
               )

clear.grid(row=6, column=1, padx=10, pady=10)

w.mainloop()
