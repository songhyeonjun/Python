# 한 학생의 과목이름과 점수 각각 5개를 입력받고
#     점수      학점
#     99~95-> a+ 4.5
#     94~90-> A  4.0
#     89~85-> b+ 3.5
#     84~80 ->B  3.0
#       ~75 c+   2.5
#       ~70 C    2.0
#       ~65 d+   1.5
#       ~60 d    1.0
#       ~0 f     0
# 가장 점수가 높은과목의 이름, 학점 출력(동점일시 가장 마지막 과목을 출력) ex) 파이썬 A+
# 평균 학점 출력(만약 f가 2개 이상이면 평균 학점 대신 낙제! 출력)
#  ex) 3.8   ex2) 낙제!

subject_list=[]
score_list=[]
score2_list=[]
score3_list=[]

for i in range(5):
   subject_list.append(input('{0}번 과목의 이름입력'.format(i+1)))
   score_list.append(int(input('점수입력')))

for i in range(5):
   if score_list[i]>=95:
      score3_list.append(4.5)
      score2_list.append('A+')
   elif score_list[i]>=90:
      score3_list.append(4.0)
      score2_list.append('A')
   elif score_list[i]>=85:
      score3_list.append(3.5)
      score2_list.append('B+')
   elif score_list[i]>=80:
      score3_list.append(3.0)
      score2_list.append('B')
   elif score_list[i]>=75:
      score3_list.append(2.5)
      score2_list.append('C+')
   elif score_list[i]>=70:
      score3_list.append(2.0)
      score2_list.append('C')
   elif score_list[i]>=65:
      score3_list.append(1.5)
      score2_list.append('D+')
   elif score_list[i]>=70:
      score3_list.append(1.0)
      score2_list.append('D')
   else:
      score3_list.append(0)
      score2_list.append('F')
print(subject_list,score_list,score2_list)

high_index=0
for i in range(1,5):
   if score3_list[high_index]<=score3_list[i]:
      high_index=i
print('가장 점수가 높은 과목은 {0}, 학점은 {1}입니다.'.format(subject_list[high_index],score2_list[high_index]))

average=0
fail=0
for i in  range(5):
   average+=score3_list[i]
   if score3_list[i]==0:
      fail+=1
average=average/5
if fail<2:
   print('평균 학점은 {0}점 입니다.'.format(average))
else:
   print('낙제!')