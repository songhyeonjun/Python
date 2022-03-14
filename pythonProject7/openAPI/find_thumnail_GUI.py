from tkinter import *
from tkinter import ttk

from multitag_API import *
from product_API import *

def find():
    product_list = []
    for i in range(1, 128, 10):
        path = './KoreanEnglishman/scene (' + str(i) + ').png'
        detection_result = detect_product(path)
        product_list.append(detection_result)
        pb_update()

    p_count_list = []
    for x in product_list:
        count = 0
        for y in x['result']['objects']:
            print(y['class'])
            count += 1
        p_count_list.append(count)
        pb_update()
        print('----------')

    print(p_count_list)

    multitag_list = []
    for i in range(1, 128, 10):
        path = './KoreanEnglishman/scene (' + str(i) + ').png'
        label_result = multi_tag(path)
        multitag_list.append(label_result)
        pb_update()

    m_count_list = []
    for x in multitag_list:
        count = 0
        for y in x['result']['label_kr']:
            print(y)
            count += 1
        m_count_list.append(count)
        pb_update()
        print('---------')

    print(m_count_list)

    t_count_list = []
    for i in range(len(p_count_list)):
        t_count_list.append(p_count_list[i] + m_count_list[i])

    print('------------------------')
    print(t_count_list)
    max_index = t_count_list.index(max(t_count_list))
    print(max_index)

    p_g.set(100)
    pb.config(variable=p_g)
    lb.config(text=p_g.get())
    pb.update()

    img = PhotoImage(file='./KoreanEnglishman/scene ('+str(max_index)+').png')
    result2.configure(image=img)
    result2.image = img

    print(len(t_count_list))

def pb_update():  # 함수 btnpress() 정의
    p_g.set(p_g.get() + 0.5)
    pb.config(variable=p_g)
    lb.config(text=p_g.get())
    pb.update()


if __name__ == '__main__':
    w = Tk()
    w.geometry("1366x768")
    w.config(bg='lightgreen')

    p_g = DoubleVar()  # double형으로 변수 저장
    p_g.set(1)
    pb = ttk.Progressbar(w)  # root라는 창에 프로그래스 바 생성
    pb.config(maximum=100)  # 최대값 설정
    pb.config(length=200)  # 길이 설정
    pb.config(variable=p_g)  # 값 변수 지정
    pb.pack()  # 프로그래스 바 배치

    lb = Label(w)  # root라는 창에 레이블 생성
    lb.pack()  # 레이블 배치


    b1=Button(w, text='최적 썸네일 분석', font=('맑은 고딕', 10), bg='silver', command=find)
    b1.pack()

    img = PhotoImage(file='./KoreanEnglishman/scene (1).png')
    result2 = Label(w, image=img, width=1280, height=720)
    result2.pack()

    w.mainloop()