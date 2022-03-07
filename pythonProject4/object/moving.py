class Bike :
    # 멤버변수 3개
    # 멤버함수 3개
    # 객체 1개 b1만 생성해서, 멤버변수값 넣고, 프린트
    # 멤버함수 2개 이상 호출(.리턴x 리턴o)
    color = None
    speed = 0
    shape = None

    # 이니셜라이저(멤버변수 초기화할 목적으로 만들어두는 함수)
    # 객체생성시 자동호출됨
    # 객체가 2개가 만들어지면, 2번 호출
    def __init__(self, color, speed, shape):
        self.color = color
        self.speed = speed
        self.shape = shape

    def speed_up(self):
        self.speed += 10
        print("현재속도", self.speed, "입니다.")

    def speed_down(self):
        self.speed -= 10
        print("현재속도", self.speed, "입니다.")

    def __str__(self):
        return self.color + ", " + self.shape + ", " + str(self.speed)





class Car :
    #멤버변수
    color = ''
    shape = None

    # 이니셜라이저(멤버변수 초기화할 목적으로 만들어두는 함수)
    # 객체생성시 자동호출됨
    # 객체가 2개가 만들어지면, 2번 호출
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    #멤버함수
    def speed_up(self):
        print(self.color + "색인 자동차의 속도를 up!")

    def speed_down(self):
        print("자동차의 속도를 down!")

    def __str__(self):
        return self.color + ", " + self.shape



