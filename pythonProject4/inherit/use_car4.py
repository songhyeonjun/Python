# 새로운 클래스를 만들때
# 기존의 있던 클래스를 "재사용!" 해서
# 만드는 것을 상속이라고 한다.
from pythonProject4.object.moving import Car


class Sedan(Car):
    preson = 0

    def tour(self):
        print("편안하게 여행을 가다.")

class Truck(Car):
    #멤버변수 2개, 멤버함수 2개
    weight = 0 # 멤버변수 3개

    def move(self): #멤버함수 3개
        print("짐을 싣고 가다.")
