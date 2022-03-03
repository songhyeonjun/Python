# month = 10입니다. 계절을 프린트
import datetime

today = datetime.datetime.today()
month = today.month
if month == 12 or 1 <= month <= 2 :
    print('겨울')
elif 3 <= month <= 5:
    print("봄")
elif 6 <= month <= 8:
    print("여름")
elif 9 <= month <= 11:
    print("가을")


# a = ['봄', '여름', '가을', '겨울']
# print(a)
# if 3 <= month <= 5 :
#     print(a[0])
# elif 6 <= month <= 7:
#     print(a[1])
# elif 9 <= month <= 11:
#     print(a[1])
# elif 12 <= month <= 2:
#     print(a[1])