rate = 0.25 #이자율
money = input('대출금액: ')

#숫자로 변환하는 처리
money2 = int(money)
result = rate * money2
print('이자는 ', result)
