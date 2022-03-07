from pythonProject4.object.worker import Worker

if __name__ == '__main__':
    a = Worker('홍길동', 25, '남')
    print("직원채용", Worker.count)
    b = Worker('김길동', 23, '여')
    print("직원채용", Worker.count)
    c = Worker('박길동', 28, '남')
    print("직원채용", Worker.count)
    d = Worker('이길동', 21, '남')
    print("직원채용", Worker.count)
    e = Worker('장길동', 29, '여')
    print("직원채용", Worker.count)

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

    print("직원수 :", Worker.count)
    print("평균나이:", Worker.ave)
    print('남자 직원수 : ', Worker.m)
    print('여자 직원수 : ', Worker.f)
