# up down 게임
import random

target = random.randint(1, 100)
i = 0
while True :
    a = int(input("숫자입력 : "))
    i += 1
    if a == target :
        print(i, "번만에 정답을 맞췄습니다.!@!@!")
        break
    elif a > target :
        print("Down")
    elif a < target :
        print("up")

# target = 55
#
# cnt = 0
# while True:
#     number = int(input('숫자를 입력>>'))
#     cnt += 1
#     if number != target:
#         if(number > target):
#             print('too big')
#         else:
#             print('too small')
#     else:
#         print('correct!')
#         print('try cnt>> ', cnt)
#         break