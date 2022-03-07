from tkinter import *
from tkinter import  messagebox

# 버튼 1개당 함수 1개를 연결
def login():
    # 입력값 가지고 오고, 일치하는지 확인
    id2 = id_entry.get()
    pw2 = pw_entry.get()
    print("id는", id2, "pw는", pw2)
    if id2 == 'root' and pw2 == '1234' :
        messagebox.showinfo('제목', '로그인 성공')
    else:
        messagebox.showinfo('제목', '로그인 실패')

w = Tk()
w.geometry("500x250")
# 라벨을 하나 만들기
id = Label(w,
           text='아이디',
           font=('궁서', 30)
           )  # id라는 라벨을 w에 넣어줌
id.pack()

id_entry = Entry(w,
                 font=('궁서', 30),
                 bg='blue',
                 fg='white'
                 )
id_entry.pack()

pw = Label(w,
           text='패스워드',
           font=('궁서', 30)
           )
pw.pack()

pw_entry = Entry(w,
                 font=('궁서', 30),
                 bg='blue',
                 fg='white'
                 )
pw_entry.pack()

b = Button(w,
           text='로그인처리',
           font=('궁서', 30),
           bg='yellow',
           command=login
           )
b.pack()

w.mainloop()
