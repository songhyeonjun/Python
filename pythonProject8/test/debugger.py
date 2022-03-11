# debugger : 중지점을 만들어 단계별로 실행하면서 에러를 수정할 수 있다.

b = 10
a = b + 1
print(a) # 중지점(breakpoint) : 여러곳 설정 가능

# 한단계씩 실행 : step over(f8)
a = 200
b = 30
print(a + 100)

for x in range(3):
    a = 333 + x
    print(a, b)