# 스레드 문제 (3개)
# -------
# 1부터 100까지 증가
# 증가 >> 1
# 증가 >> 2
#
# 100부터 1까지 감소
# 감소 >> 100
# 감소 >> 99
#
# 특수문자를 100번 프린트(@,#,$,\) #text = [@]
# random.ch

import random
import threading


def a1(x, y):
    for i in range(x, y + 1):
        print("증가 >>", i)


def a2(x, y):
    for i in range(x, y - 1, -1):
        print("감소 >>", i)


def a3():
    text = ['@', '#', '$', '%']
    for i in range(100):
        a = random.choice(text)
        print(i, "특수>>", a)


# 스레드 객체로 만들기
thread1 = threading.Thread(target=a1, args=(1, 100))
thread2 = threading.Thread(target=a2, args=(100, 1))
thread3 = threading.Thread(target=a3)

# cpu의 스케쥴러에 등록
thread1.start()
thread2.start()
thread3.start()
