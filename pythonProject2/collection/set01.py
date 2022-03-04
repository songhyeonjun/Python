jumsu_1 = {100, 99, 88, 77}
jumsu_2 = {90, 99, 88, 66}


# 두 학기 내내 동일한 성적인 점수는? 과목 수는?
a = jumsu_1 & jumsu_2
result1 = jumsu_1.intersection(jumsu_2)
print(a, len(a))
print(result1, len(result1))

# 두 학기를 비교했을 때 1학기 성적 중 2학기와 다른 성적은?
b = jumsu_1 - jumsu_2
result2 = jumsu_1.difference(jumsu_2)
print(b)
print(result2)

# 두 학기 동안 내가 획득한 전체 점수 목록은?
result3 = jumsu_1.union(jumsu_2) # | 버티컬 바
c = jumsu_1 | jumsu_2
print(c)
print(result3)

#정렬
result33 = list(result3) # list()한 결과, 비파괴형 함수
print(type(result3))
print(type(result33))
result33.sort() # void, 파괴형 함수 오름차순 정렬
print(result33)
result33.reverse() # 내림차순 정렬
print(result33)

# 1학기 성적에 음악점수 50점 추가
jumsu_1.add(50)
print(jumsu_1)

# 2학기 성적에 음악 77, 컴퓨터 100점 추가
jumsu_2.update({77, 100})
print(jumsu_2)

# 1학기 성적 모두 삭제
jumsu_1.clear()
print(jumsu_1)
