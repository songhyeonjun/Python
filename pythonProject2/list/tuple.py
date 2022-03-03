# tuple은 read_only한 리스트를 만들고 싶을 때

food_list = ['coffee', 'water', 'orange']
food_list2 = tuple(food_list)
print(food_list2)
# food_list2[0] = 'icecream'

def yes():
    x = 100
    y = 200
    return (x, y)

result = yes()
print(result)
result2 = list(result)