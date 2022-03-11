import random
import turtle



def click(x, y):
    print(x, y)
    x2 = random.randint(-400, 400)
    y2 = random.randint(-400, 400)
    pen_size = random.randint(1, 30)
    color_list = ['green', 'blue', 'red', 'purple', 'pink']
    # color_choice = color_list[random.randint(0, 6)]
    color_choice = random.choice(color_list)
    my_turtle.pencolor(color_choice)
    my_turtle.pensize(pen_size)
    # my_turtle.pendown()
    my_turtle.goto(x2, y2)
    my_turtle.goto(x, y)


# 거북이 화면 가운데에 보이게 해주는 처리
my_turtle = turtle.Turtle('turtle')
turtle.onscreenclick(click, 1)
# my_turtle.pensize(20)
# my_turtle.pencolor('red')
turtle.done()
