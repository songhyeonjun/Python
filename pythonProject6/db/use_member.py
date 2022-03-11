# 북마크 테이블에 대한 crud기능 처리를 하고 싶음
# from db import dao
# from 패키지 import 모듈
# >>> 모듈.함수(), 모듈.클래스명()
import sys
from tkinter import messagebox

from db.member_dao import *

# from 패키지명.모듈명 import 함수명, 클래스명, *
# >>> 함수()

if __name__ == '__main__':
    while True:
        choice = int(input("1)회원가입, 2)회원정보수정, 3)회원삭제, 4)회원1명정보, 5)모든 회원정보, 6)로그인>>, 7)그만하자 "))
        # 모든 입력은 string
        if choice == 1:
            id = input("id 입력>>>")
            pw = input("pw 입력>>>")
            name = input("name 입력>>>")
            tel = input("tel 입력>>>")
            vo = (id, pw, name, tel)
            create(vo)
        elif choice == 2:
            id = input("변경하고 싶은 id 입력>>")
            name = input("변경할 name 입력>>")
            tel = input("변경할 tel 입력>>")
            vo = (name, tel, id)
            update(vo)
            print("변경 완료~!!")
        elif choice == 3:
            # id가 1이면 삭제
            id = input("삭제할 id값 입력:")
            delete(id)
        elif choice == 4:
            # id가 1이면 검색
            id = input("검색할 id값 입력:")
            print("id :", id)
            row = read(id) # id를 주면서 검색
            messagebox.showinfo("결과", "검색 결과는 " + row[0] + ", " +
                                row[1] + ", " + row[2] + ", " + row[3])
        elif choice == 5:
                result = all()
                print("id       name        url                    img")
                print("-" * 50)
                for one in result:
                    print("%s       %s       %s           %s" %one)
        elif choice == 6:
            id = input("id 입력>>>")
            pw = input("pw 입력>>>")
            vo = (id, pw)
            row = login(vo)
            print(row)
        elif choice == 7:
            break
        else:
            sys.exit(0)
