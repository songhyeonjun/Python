# 프로그래밍 순서

# 데이터를 입력
name = input("이름을 입력 : ")
age = input("나이를 입력 : ")

# 데이터를 처리
print(type(name))
print(type(age)) # 모든 입력은 str
age2 = int(age) + 1 # 파이썬에서는 +연산자는 타입이 동일해야 가능

# 데이터를 출력
print("입력한 이름 : " + name)
print("입력한 나이 : " + age) # 결합연산자
print("입력한 내년 나이 : " + str(age2) + "세")