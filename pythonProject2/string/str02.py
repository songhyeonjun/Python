# 주민번호 13자리를 입력을 받아서 나이와 성별을 판별
import datetime
today = datetime.datetime.today()

sn = input("주민번호 13자리 입력")

year = sn[:2]
gender = sn[6]


if gender == '1' or gender == '3':
    print("성별은 : 남자")
elif gender in ('2', '4') :
    print("성별은 : 여자")
else :
    print("번호를 제대로 입력하세요!!@@")

print("---------------------")

year2 = int(year) + 1900
age = today.year - year2 +1

print("나이는 :", age)