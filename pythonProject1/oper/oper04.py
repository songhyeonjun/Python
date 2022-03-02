# 내일 우산을 가지고 갈지 판단
# 조건 : 비가 올까(0: 비가온다. 1: 비가 안온다)
#       날이 흐린가(0: 날이 흐림. 1:날이 안흐림)

# 비가 오거나, 날이 흐리면 우산을 가지고 가고, 빨리 퇴근!
# 아니면, 운동!

# print("비가 올까? ")
# a = input("0 : 비가온다  1 : 비가안온다")
# print("날이 흐린가? ")
# b = input("0 : 흐림  1 : 맑음")
#
# if a or b == 0 :
#     print("우산을 챙기고 빠른퇴근")
# else:
#     print("운동")

rain, day = input(question).split()
if rain == 0 or day == 0 :
    print("우산을 가지고 간다")
    print("퇴근을 빨리 하자")
else:
    print("우산을 안가져간다.")
    c = input("그럼 뭐할까?")
    print(c + "하러가자")