# 스티커 가격 100원, 책갈피 가격 200원
sticker_price = 100
book_price = 200

# 스티커 개수: 5(**)
# 책갈피 개수: 3(**)
sticker = int(input('스티커 개수: ')) #5
book = int(input('책갈피 개수: ')) #3

# 우수회원이신가요? 맞으면=1, 아니면=2>> 1(**)
vip = input('우수회원이신가요? 맞으면=1, 아니면=2>>')

# 우수회원이면 10%를 할인해주세요.
total = sticker * sticker_price + book * book_price
sale = total - total * 0.1

# 지불 해야할 총금액을 출력
if vip == '1':
    print('당신의 지불 금액은 ', sale)
else:
    print('당신의 지불 금액은 ', total)