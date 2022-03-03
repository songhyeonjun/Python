food = []
food.append(input("입력1 : "))
food.append(input("입력2 : "))
food.append(input("입력3 : "))
print(food)
print(food[0], food[1])
print(food[1], food[2])
food[0] = '라면'
print(food)

# food = [] #감자, 고구마, 양파
# for _ in range(3):
#     data = input('입력>> ')
#     food.append(data)
#
# print(food[1])
# print(food[0:2])
# print(food[1:])
# food[0] = '라면'
# print(food)