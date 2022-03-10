# 북마크 테이블에 대한 crud기능 처리를 하고 싶음
# from db import dao
# from 패키지 import 모듈
# >>> 모듈.함수(), 모듈.클래스명()
import sys
from tkinter import messagebox

from db.dao import *

# from 패키지명.모듈명 import 함수명, 클래스명, *
# >>> 함수()

if __name__ == '__main__':
    choice = int(input("cud중 선택>>1)c, 2)u, 3)d, 4)r, 5)(all)>> "))
    # 모든 입력은 string
    if choice == 1:
        id = input("id 입력>>>")
        name = input("name 입력>>>")
        url = input("url 입력>>>")
        img = input("img 입력>>>")
        vo = (id, name, url, img)
        # create(id, name, url, img)
        create(vo)
    elif choice == 2:
        # id가 1이면, name은 naver2로 변경
        id = input("변경하고 싶은 id 입력>>")
        name = input("변경할 name 입력>>")
        vo = (name, id)
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
        all = all()
        print("id       name        url                    img")
        print("-" * 50)
        for one in all :
            print("%s       %s       %s           %s" %one)
    else:
        sys.exit(0)
