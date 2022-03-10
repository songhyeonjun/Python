from tkinter import *
from tkinter import messagebox

from db.member_dao_class import DAO


def save():
    # 1) 입력한 값 가지고 와야함
    id = id_entry.get()
    pw = pw_entry.get()
    name = name_entry.get()
    tel = tel_entry.get()

    # 2) vo에 넣어준다.(tuple)
    vo = (id, pw, name, tel)

    # 3) dao객체 생성후, 해당 함수 호출!
    dao = DAO()
    print(vo)
    result = dao.create(vo)

    # 4) return값이 1ㅣ면 성공, 아니면 실패
    if result == 1:
        messagebox.showinfo("결과", "db에 저장성공")
    else:
        messagebox.showinfo("결과", "db에 저장실패")


def read():
    # id에 입력을 먼저 한 후,
    # 버튼을 누르면 해당 id의 정보를 db에서 검색해온다.
    id = id_entry.get()
    dao = DAO()
    row = dao.read(id)
    print('검색결과>> ', row)
    pw_entry.insert(0, row[1])
    name_entry.insert(0, row[2])
    tel_entry.insert(0, row[3])


window = Tk()
window.geometry('500x600')
icon = PhotoImage(file='r7.png')
top = Label(window, image=icon)
top.pack()

id_label = Label(window, text='ID입력')
id_label.pack()
id_entry = Entry(window, font=('고딕', 20), bg='yellow', fg='red')
id_entry.pack()
pw_label = Label(window, text='PW입력')
pw_label.pack()
pw_entry = Entry(window, font=('고딕', 20), bg='yellow', fg='red')
pw_entry.pack()
name_label = Label(window, text='NAME입력')
name_label.pack()
name_entry = Entry(window, font=('고딕', 20), bg='yellow', fg='red')
name_entry.pack()
tel_label = Label(window, text='TEL입력')
tel_label.pack()
tel_entry = Entry(window, font=('고딕', 20), bg='yellow', fg='red')
tel_entry.pack()
save = Button(window, width=30, height=2,
              bg='green',
              font=('고딕', 25),
              text='DB에 저장',
              command=save
              )
save.pack(side="bottom")
read = Button(window, width=30, height=2,
              bg='green',
              font=('고딕', 25),
              text='DB에서 읽기',
              command=read
              )
read.pack(side="bottom")
window.mainloop()
