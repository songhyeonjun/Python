import turtle

t = turtle.Pen()

while True:
    방향 = input("왼쪽: 1, 오른쪽 : 2")
    각도 = int(input("각도 입력"))
    if 방향 == '1':
        t.left(각도)
        t.forward(150)
    if 방향 == '1':
        t.right(각도)
        t.forward(150)

