import random
import turtle


# 클릭을 했을 때, 두 가지 그림을 그리는 함수를 만들기
# 아무거나 둘 선택
# color, size가 변하게!
def click(x, y):
    print(x, y)
    my_turtle.speed(0)
    pen_size = random.randint(1, 30)
    color_list = ['green', 'blue', 'red', 'purple', 'pink']
    color_choice = random.choice(color_list)
    my_turtle.pencolor(color_choice)
    my_turtle.pensize(pen_size)
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()

    size = random.randint(10, 200)
    n = random.randint(1, 2)
    if n == 1:
        for _ in range(5):
            my_turtle.forward(size)
            my_turtle.right(144)
    else :
        for _ in range(4):
            my_turtle.left(90)
            my_turtle.forward(size)


# 거북이 화면 가운데에 보이게 해주는 처리
my_turtle = turtle.Turtle('turtle')
turtle.onscreenclick(click, 1)

turtle.done()
