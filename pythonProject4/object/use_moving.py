import pythonProject4.object.moving as m # module까지

if __name__ == '__main__':
    # class의 instance인 object
    c1 = m.Car('네모', 'red') #new Car()
    # 객체 생성시 자동으로 멤버변수값을 초기화 해주는 함수
    # (생성자 메서드, 초기화해주는것,
    # initializer(이니셜라이저)
    # c1.shape = '네모'
    # c1.color = 'red'
    c2 = m.Car('세모', 'green')
    # c2.shape = '세모'
    # c2.color = 'green'
    print(c1)
    print(c2)
    # c1.speed_up()
    # c2.speed_down()

    b1 = m.Bike('red', 10, '네모')
    # b1.speed = 10
    # b1.color = 'red'
    # b1.shape = '네모'
    print(b1)
    b1.speed_up()