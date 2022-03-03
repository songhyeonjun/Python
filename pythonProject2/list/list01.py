food = [] # list()
# food[0] = '커피' --> index가 아직 없음 error
food.append('커피') # 추가
food[0] = '라떼'
food.append('라면')
food.append('짜장면')
print(len(food))

food[2] = "짬뽕"
print(food)

# del food[1] # index로 삭제
# print(food)
#
# food.remove('라떼') # 값으로 삭제
# print(food)

food.reverse() # 위치 변환
print(food)

# food.pop() # 마지막에 들어온 값 삭제 del food[len(food) -1]
# print(food)
# food.pop()
# print(food)

for x in food :
    print(x, end=' ')
print()
for i in range(len(food)) :
    print(food[i], end=" ")