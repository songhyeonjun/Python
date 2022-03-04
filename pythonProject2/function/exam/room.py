class TV:
    color = None
    size = 0
    price = 0

    def on(self):
        print("TV를 킵니다")

    def off(self):
        print("TV를 끕니다")

    def down(self):
        print("TV 소리를 줄입니다.")

    def __str__(self):
        return "색상은 : " + str(self.color) + ", 사이즈는 : " + str(self.size) \
               + "인치이고, 가격은 " + str(self.price) + "원입니다."
