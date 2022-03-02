savedId = 'root' #회원 가입시 id
savedPw = '1234' #회원 가입시 pw

id = input('id입력>> ')
pw = input('pw입력>> ')

# 논리연산자: and, or
# and: 조건이 여러개 다 true인 경우
# or: 조건이 여러개 중 한개만 true인 경우
if savedId == id and savedPw == pw:
    print('로그인 ok..')
else:
    print('로그인 not..')
