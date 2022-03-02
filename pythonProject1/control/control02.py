#유한루프
for i in range(0, 5, 1) :#0 1 2 3 4
    print(i+1)


for i in [0, 1, 2, 3, 4] :#0 1 2 3 4
    print(i, "돌아간다")

#범위를 100부터 시작해서 100씩 점프, 999까지 생성
for i in range(100, 1000, 100) :
    print(i)


count = 0
while True :
    if count == 5:
        print(count, "반복문 중지")
        break #반복문이 중지
    print(count, "@@@@@@@@@")
    count = count + 1

for x in range(0, 3, 1) :
   print("*")