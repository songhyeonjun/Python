print("오늘에 대한 정보입니다.")
print("====================")

# weather = input("오늘의 날씨는? ")
# hot = input("오늘의 온도는? ")
# night = input("오늘 저녁 스케쥴은? ")
weather, hot, night = input("날씨, 온도, 스케줄 입력 : ").split(",")
hot = float(hot) - 1

print("오늘은 " + weather + "하고, " + str(hot) + "도이고, " + night + "에 머무를 예정입니다.")