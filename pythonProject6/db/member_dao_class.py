# data access module
# crud 기능
# def 4개 필요@
import pymysql


class DAO:
    # 인스턴스 변수
    conn = None  # 변수 생성 위치가 중요
    # 클래스 바로 아래에 생긴 클래스 안 전체에서 사용 가능
    # 전역변수(글로벌 변수)

    cur = None

    def __init__(self):
        # 함수 내에서 처음으로 만들어진 변수(지역변수, 잠는
        # 함수밖에서는 인식 불가
        # 변수가 위치가 중요!
        # 파이썬에서 변수는 언제 들어어질까>
        # 변수명 = 초가값
        try:
            self.conn = pymysql.connect(
                host='localhost',
                port=3366,
                user='root',
                password='1234',
                db='big',
                charset='utf8'
            )
            print('1. 연결 성공!!@', self.conn.host_info)

            # 연결된 통로(stream)을 통해, SQL문 보내기
            # 2. 연결된 통로를 지정(접근할 수 있는) 커서 객체를 획득
            self.cur = self.conn.cursor()
        except Exception as e:
            print('db연결 중 에러 발생!@!@')
            print("에러정보 >>", e)

    def create(self, vo):

        # 3. sql문 보내기
        sql = "insert into member values(%s, %s, %s, %s)"
        print(vo)
        # 커서로 sql문을 보낸다.
        result = self.cur.execute(sql, vo)
        print("sql문 전송 결과", result)

        self.conn.commit()  # insert한 것을 반영
        self.conn.close()

        return result

    def read(self, id):

        # 3. sql문 보내기
        sql = "select * from member where id = %s"

        # 커서로 sql문을 보낸다.
        result = self.cur.execute(sql, (id))
        print("sql문 전송 결과", result)

        # read인 경우, 커서로 연결통로(스트림)에 있는 검색 결과를 꺼내주어야 한다.
        row = self.cur.fetchone()
        print(row)
        # conn.commit()  # select는 commit할 필요 X
        self.conn.close()
        return row  # 검색 결과를 return

    def update(self, vo):

        # 3. sql문 보내기
        sql = "update member set name = %s, tel = %s where id = %s"

        # 커서로 sql문을 보낸다.
        result = self.cur.execute(sql, (vo))
        print("sql문 전송 결과", result)

        self.conn.commit()  # update한 것을 반영
        self.conn.close()

    def delete(self, id):

        # 3. sql문 보내기
        sql = "delete from member where id = %s"

        # 커서로 sql문을 보낸다.
        result = self.cur.execute(sql, (id))
        print("sql문 전송 결과", result)

        self.conn.commit()  # delete한 것을 반영
        self.conn.close()

    def all(self):

        # 3. sql문 보내기
        sql = "select * from member"

        # 커서로 sql문을 보낸다.
        result = self.cur.execute(sql)
        print("sql문 전송 결과", result)

        # read인 경우, 커서로 연결통로(스트림)에 있는 검색 결과를 꺼내주어야 한다.
        # row = cur.fetchone() # row하나만 꺼낸다
        row = self.cur.fetchall()  # row 모두를 꺼낸다
        # row = cur.fetchmany(5) # row 개수를 정해서 꺼낸다ㅣ
        # conn.commit()  # select는 commit할 필요 X
        self.conn.close()
        print(row)
        return row  # 검색 결과를 return

    def login(self, vo):

        # 3. sql문 보내기
        sql = "select * from member where id = %s and pw = %s"

        # 커서로 sql문을 보낸다.
        result = self.cur.execute(sql, (vo))
        print("sql문 전송 결과", result)
        # read인 경우, 커서로 연결통로(스트림)에 있는 검색 결과를 꺼내주어야 한다.
        row = self.cur.fetchone()  # row하나만 꺼낸다
        # row = cur.fetchall()  # row 모두를 꺼낸다
        # row = cur.fetchmany(5) # row 개수를 정해서 꺼낸다ㅣ
        # conn.commit()  # select는 commit할 필요 X
        print(row)
        self.conn.close()
        if row is None:
            return "로그인 실패"  # 검색 결과를 return
        else:
            return "로그인 성공"
