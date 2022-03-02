# 터미널에서 입력
# 1. 숫자1 : 333
# 2. 숫자2 : 222
# 사직연산을 수행하고 프린트

n1 = int(input("숫자 : "))
n2 = int(input("숫자 : "))

print("두 수의 합 :", n1 + n2)
print("두 수의 빼기 :", n1 - n2)
print("두 수의 곱하기 :", n1 * n2)
print("두 수의 나누기 :", n1 / n2)
print("두 수의 나누기(소수점x) :", n1 // n2)
print("두 수의 나머지 :", n1 % n2)

a = input("이름 : ")
b = int(input("나이 : "))

print(a, "은", b, "세 입니다.")
if b >100 :
    print("나이가 많으시군요")
else:
    print("아직 어리시군요")

hobby = input("hobby : ")
time = int(input("time : "))
print(hobby, "를", time, ("시간했습니다."))
if hobby == '달리기' and time >= 10 :
    print("오늘", hobby, "는 충분")
elif hobby == '달리기' or time <= 10 :
    print("어떤 운동이든 시작하세요")

