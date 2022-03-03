# 시작값, 끝값을 입력받아 시작과 끝 사이의 개수를 구하고, 합계를 구하고, 평균을 구하

a = int(input("시작값 : "))
b = int(input("끝값 : "))
sum = 0
age = 0
for i in range(a, b) :
    sum = sum + i
age = sum / (b-a)
print(b - a)
print(sum)
print(age)

# start, end = input('시작, 끝값 입력>>').split(',')
# start2 = int(start)
# end2 = int(end)
# print(start2)
# print(end2)
#
# length = len(list(range(start2, end2 + 1)))
# print('개수는 ', length)
#
# sum = 0
# for x in range(start2, end2 + 1):
#     sum += x
# print('sum: %d점' % sum )
# print('avg: %0.1f' % (sum / length))
#
# print('--------')
#
# sum = 0
# for n in range(10, 21):
#     sum += n
# print(sum)