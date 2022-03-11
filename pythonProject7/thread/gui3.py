import turtle

t = turtle.Pen()

while True:
    a = int(input("1)네모 2)별"))
    if a == 1 :
        while True:
            for _ in range(4):
                t.left(90)
                t.forward(150)
    elif a == 2 :
        while True:
            t.left(10)
            t.forward(10)
    else:
        break