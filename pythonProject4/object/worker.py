class Worker :
    name = None
    age = 0
    gender = None
    count = 0
    ave = 0
    m = 0 # 성별 누적
    f = 0 # 성별 누적

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Worker.count += 1
        Worker.age += self.age
        Worker.ave = Worker.age / Worker.count
        if gender == '남':
            Worker.m += 1
        else:
            Worker.f += 1

    def works(self):
        return "열심히 뽑습니다."

    def __str__(self):
        return self.name + ", " + str(self.age) + ", " + self.gender
