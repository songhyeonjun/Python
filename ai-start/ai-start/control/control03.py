# 정리문제3
# ---------
# 연간 총수입: 3500
income = int(input('연간 총수입: '))

# 소득 공제액: 500
minus = int(input('소득 공제액: '))

# 소득세는 600입니다. ->계산은 (총수입-공제액)*0.02
tax = (income - minus) * 0.02
print('소득세는 ', int(tax), '입니다.')

# 세금을 제외한 순수입은 2400입니다.
#     ->계산은 총수입-공제액-소득세
pure = income - minus - tax
print('세금을 제외한 순수입은 ', int(pure), '입니다.')
