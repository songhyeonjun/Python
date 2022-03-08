import datetime as dt
# 현재 시각을 찍는 쓰레드 100번
import threading
import time
print(dt.datetime.now())
now = dt.datetime
def dt():
    for _ in range(100):
        time.sleep(1)
        print("현재시간>>", now.now())


# 리스트에 있는 먹고 싶은 음식 목록 10개를 찍는 스레드
def food():
    food_list = ['사과', '배', '무', '배추', '된장', '고추장', '커피',
                 '물', '주스', '오이']
    for one in food_list:
        time.sleep(0.1)
        print("과일>>", one)


# 1부터 500까지 카운트하는 스레드
def plus():
    for x in range(500):
        time.sleep(0.1)
        print("카운트>>", x)


dt = threading.Thread(target=dt)
food = threading.Thread(target=food)
plus = threading.Thread(target=plus)

dt.start()
food.start()
plus.start()
