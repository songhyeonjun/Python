price = 3700
# count = 5
count = int(input('몇 잔을 사실 건가요? ')) #5,8,..
total = price * count
print('당신이 지불한 금액: ', total)

# 20000원이 넘으면, 5000을 할인
# 20000원이 넘지 않으면 total금액을 다 냄.
#비교 연산자: > >= < <= ==(같은지) !=(다른지)
if total >= 20000 : #비교연산자의 결과는 True, False
    print('할인받은 금액: ', total - 5000)
else: #False
    print('최종 지불금액: ', total)

print(total >= 20000)