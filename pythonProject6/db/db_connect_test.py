import pymysql

try:
    conn = pymysql.connect(
        host='localhost',
        port=3366,
        user='root',
        password='1234',
        db='big',
        charset='utf8'
    )
    print('1. 연결 성공!!@', conn.host_info)

    # 연결된 통로(stream)을 통해, SQL문 보내기
    # 2. 연결된 통로를 지정(접근할 수 있는) 커서 객체를 획득
    cur = conn.cursor()

    # 3. sql문 보내기
    sql = "insert into book values('6', 'hi', 'http://www.himedia.com', 'img')"

    # 커서로 sql문을 보낸다.
    result = cur.execute(sql)
    print("sql문 전송 결과", result)

    conn.commit() # insert한 것을 반영
    conn.close()

except Exception as e:
    print('db연결 중 에러 발생!@!@')
    print("에러정보 >>", e)
