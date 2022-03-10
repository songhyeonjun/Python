# data access module
# crud 기능
# def 4개 필요@
import pymysql


# def create(id, name, url, img):
def create(vo):
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
        sql = "insert into book values(%s, %s, %s, %s)"

        # 커서로 sql문을 보낸다.
        # result = cur.execute(sql, (id, name, url, img))
        result = cur.execute(sql, (vo))
        print("sql문 전송 결과", result)

        conn.commit()  # insert한 것을 반영
        conn.close()

    except Exception as e:
        print('db연결 중 에러 발생!@!@')
        print("에러정보 >>", e)


def read(id):
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
        sql = "select * from book where id = %s"

        # 커서로 sql문을 보낸다.
        # result = cur.execute(sql, (id, name, url, img))
        result = cur.execute(sql, (id))
        print("sql문 전송 결과", result)

        # read인 경우, 커서로 연결통로(스트림)에 있는 검색 결과를 꺼내주어야 한다.
        row = cur.fetchone()
        print(row)
        # conn.commit()  # select는 commit할 필요 X
        conn.close()
        return row # 검색 결과를 return

    except Exception as e:
        print('db연결 중 에러 발생!@!@')
        print("에러정보 >>", e)


def update(vo):
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
        sql = "update book set name = %s where id = %s"

        # 커서로 sql문을 보낸다.
        # result = cur.execute(sql, (id, name, url, img))
        result = cur.execute(sql, (vo))
        print("sql문 전송 결과", result)

        conn.commit()  # update한 것을 반영
        print()
        conn.close()

    except Exception as e:
        print('db연결 중 에러 발생!@!@')
        print("에러정보 >>", e)


def delete(id):
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
        sql = "delete from book where id = %s"

        # 커서로 sql문을 보낸다.
        # result = cur.execute(sql, (id, name, url, img))
        result = cur.execute(sql, (id))
        print("sql문 전송 결과", result)

        conn.commit()  # delete한 것을 반영
        conn.close()

    except Exception as e:
        print('db연결 중 에러 발생!@!@')
        print("에러정보 >>", e)

def all():
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
        sql = "select * from book"

        # 커서로 sql문을 보낸다.
        # result = cur.execute(sql, (id, name, url, img))
        result = cur.execute(sql)
        print("sql문 전송 결과", result)

        # read인 경우, 커서로 연결통로(스트림)에 있는 검색 결과를 꺼내주어야 한다.
        # row = cur.fetchone() # row하나만 꺼낸다
        row = cur.fetchall() # row 모두를 꺼낸다
        # row = cur.fetchmany(5) # row 개수를 정해서 꺼낸다ㅣ
        print(row)
        # conn.commit()  # select는 commit할 필요 X
        conn.close()
        return row  # 검색 결과를 return

    except Exception as e:
        print('db연결 중 에러 발생!@!@')
        print("에러정보 >>", e)
