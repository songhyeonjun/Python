from tkinter import *
from multitag_API import *
from product_API import *


def find():
    img_list = []
    for a in range(1, 128, 10):
        img_list.append('img/scene (' + str(a) + ').png')
    result_list = []
    for img in img_list:
        label_result = multi_tag(img)
        result_list += label_result
    print(result_list)

    # from collections import Counter
    count_result = Counter(result_list)
    print(count_result)
    # 1
    print(count_result.most_common(1))
    # [('사람', 3)]
    print(count_result.most_common(5))
    # [('사람', 3), ('여러사람', 3), ('여성', 3), ('남성', 3), ('바지', 3)]
    order_5 = count_result.most_common(5)
    print(order_5[0])
    # ('사람', 3)
    order_1 = order_5[0]
    print("제일 빈도수가 높은 단어는", order_1[0] +
          "이고, 빈도수는", order_1[1])



w = Tk()
w.geometry("1280x720")
w.config(bg='lightgreen')

b1 = Button(w, text='최적 썸네일 분석', font=('맑은 고딕', 10), bg='silver', command=find)
b1.pack()

img = PhotoImage(file='img/scene (127).png')
result2 = Label(w, image=img, width=1280, height=720)
result2.pack()

w.mainloop()
