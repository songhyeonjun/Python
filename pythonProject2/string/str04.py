# 신문기사 카테고리 중 국제 타이틀 10개를 가지고 와서
# 하나의 string으로 만드시오
# 그 중 '러시아'라는 단어가 몇 번 나오는지 카운트
# 단어의 개수?
# 단어 중 러시아라는 단어의 위치는 몇번째인지 모두 프린트]
# 침략으로 시작하는 단어를 모두 하나의 리스트로 모아서 몇 개인지 세보고, 프린트

news = '''
동영상기사	
[단독] "키에프→키이우…정부, 우크라 지명 현지식 표기 방침"공격하는 등 점점 더 무차별 공격을 증대하는 모양새다. 이에 국제사회의 규탄도 더욱 커지고 있다．
우크라, 러 '헤르손 함락' 주장 반박‥"전투 계속"(종합)
"러시아 전투기 4대, 스웨덴 영공 침범"(종합)
[속보] “EU 외교관들, 러 침공 도운 벨라루스 신규 제재 승인”
"EU 외교관들, 벨라루스 신규 제재 승인"
러시아 비판 수위 높이는 정부 "러시아 침략 강력 규탄"
중국, 러시아 규탄 결의안 반대 대신 기권…러시아에 등 돌리나
남부도시 헤르손 시장 "러군, 거리·시의회 진입"[우크라 침공]
"러가 도시 행정 장악"…우크라 남부 헤르손 사실상 함락
남부 도시 헤르손 시장 "러군, 거리 · 시의회 진입"
'''

print(len(news))

news2 = news.split()
print(news2)

count = 0
ru_list = []
for i in range(0, len(news2), 1):
    if(news2[i].endswith('러시아') or news2[i].startswith('러')):
        ru_list.append(i)
        count += 1
print("러시아 개수는", count)
print("최종 러시아 위치는", ru_list)

news2 = news.replace("러시아", "소련")
print(news2)

news2 = news.split()
print(news2)
count2 = 0
for i in range(0, len(news2), 1) :
    if(news2[i].startswith('침략')) :
        count2 += 1
print("침략 개수 :", count2)
