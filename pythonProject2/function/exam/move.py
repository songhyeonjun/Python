# function 패키지내에 exam패키지내에
# tour.py를 만들어서 spring(), summer()함수 정의
# -------------------------------------------------
# 호출은 move.py에서
# spring(3, '제주도')
# => 3월에 제주도에 가요 프린트
# summer('울릉도', 8) default값 10000
# => 8월에 울릉도를 가는 비용은 10000원입니다.
# => 조건처리 6이면 비용이 -2000할인해서 8000원이 되도록
#            7이면 비용이 -1000할인해서 9000원이 되도록
#            나미지 월이면 +2000해서 12000원이 되도록

import function.exam.tour as t

t.spring(3, '제주도')

t.summer('울릉도', 7)