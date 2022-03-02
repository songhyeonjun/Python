good_rate = 2.5 # 값을 넣을 때 변수의 타입이 결정됨
bad_rate2 = input("좋은 이자율 입력 : ") # '11.5'
print(type(good_rate))
print(type(bad_rate2))

money = 100000
#이자 금액을 계산
print("좋은 이자율", int(money * good_rate))
print("나쁜이자율", int(money * float(bad_rate2)))


#아래의 데이터는 연산자의 대상?
tel = '01012341234' # 연산의 대상이 된다라는 표현은 4칙 연산
                    # 자리수를 고려할 수 있는 데이터가 연산의 대상
sn = '990909'

food = True
rain = False