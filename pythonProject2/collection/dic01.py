food = {'아침': '토스트', '점심': '한정식', '저녁': '스프'}
print(food['아침'])  # 값을 확일할 때 : 딕셔너리이름[키]

food['아침'] = '커피'  # 값을 수정할 때
print(food)

food['간식'] = '쿠키'  # 값을 추가
print(food)

del food['간식']  # 값을 삭제
print(food)

# dic를 for-each문으로 돌렸을때는 key만 가지고 온다.
for key in food:
    print(key, ":", food[key])  # 키와 값을 가지고 온다.

dict1 = {100: 'hong', 200: 'kim'}
print(dict1[100])

for key in dict1:
    print(key, ':', dict1[key])

key_list = dict1.keys()  # 키를 dick_key([100, 200])으로 출력
print(key_list)
key_list2 = list(key_list)  # [100, 200]으로 변환
print(key_list2)

value_list = dict1.values()  # 값을 dick_values(['hong', 'kim'])으로 출력
print(value_list)

# print(dict1[100])
print(dict1.get(100))

print(100 in dict1)  # 키 중에 100이 있냐?
# 회원명단 중에서 500이 있나요?
if 500 in dict1:
    print("500회원이 존재")
else:
    print("500회원 존재 x")

# 키는 여러개 x 값은 여러개 o
hobby = {10: ['game', 'picture'], 20: ['tour', 'run', 'coding']}
# 10대의 취미 목록을 프린트
s10 = hobby[10]
print(s10)
# 20대의 취미 목록을 프린트
s20 = hobby[20]
print(s20)
# 20대의 취미 목록을 카운트

hobby2 = {10: {'아침': 'game', '저녁': 'picture'}, 20: ['tour', 'run', 'coding']}
s100 = hobby2[10]
print(s10) # ['game', 'picture']
s1000 = s100['저녁']
print(s1000) # picture

hobby3 = [
    {10: {'아침': 'game', '저녁': 'picture'}},
    {20: {'아침': 'coffee', '저녁': 'tour'}}
]
hobby30 = hobby3[1]
print(hobby30) # {20: {'아침': 'coffee', '저녁': 'tour'}}
hobby300 = hobby30[20]
print(hobby300) # {'아침': 'coffee', '저녁': 'tour'}
hobby3000 = hobby300['저녁']
print(hobby3000) # tour