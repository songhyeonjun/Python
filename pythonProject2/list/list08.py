# movie 예매 사이트
seat = [0] * 10
sum = 0
while True:
    print('\n영화예매 사이트입니다.')
    print('-----------------------------')
    print(' ', end='')
    for x in range(0, 10):
        print(x, end='  ')
    print()
    print('-----------------------------')
    print(seat)
    print('-----------------------------')
    no = int(input('예매 좌석번호 선택(종료 -1)>> '))

    if no == -1:
        # 몇 좌석 예매가 되었는지 프린트
        # 결제금액 한 자리당 1만원해서 프린트
        for i in range(10):
            if seat[i] == 1 :
                sum += seat[i]
        print(sum, "좌석이 예매되어있습니다.")
        print(sum * 10000, "원입니다." )

        #좌석 번호 프린트
        seat_list = []
        for i in range(len(seat)) :
            if(seat[i] == 1) :
                seat_list.append(i)
        print("예매한 좌석은 %s " % seat_list)
        break # break를 포함하고 있는 반복문(while)문이 더이상 실행되지 않음
    else:
        #예매가 이미 된 자리라면 재입력하라고 해주세요.!
        if seat[no] == 0 :
            #예매처리
            seat[no] = 1
            print("예매가 완료되었습니다.")
        else :
            print("이미 에매된 자리입니다.")
            print("다시 예매해주세요")
