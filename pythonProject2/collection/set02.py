# 기본형복사 (=), 변수에 값이 들어가 있음
x = 100
y = x
y = 200
print(x)
print(y)
# 참조형복사 (함수를 사용), 주소가 들어가 있다.
# 얕은 복사, 깊은 복사
jumsu_1 = [10, 20, 30]
jumsu_2 = jumsu_1
print(jumsu_1)
print(jumsu_2)
print("====얕은 복사===")
jumsu_2[0] = 99
print(jumsu_1)
print(jumsu_2)
print("===깊은 복사===")
jumsu_3 = jumsu_1.copy()
jumsu_3[0] = 55
print(jumsu_1)
print(jumsu_3)