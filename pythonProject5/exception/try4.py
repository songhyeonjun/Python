# test_file = open('test.txt', 'r')
# test_file.close()
# 램에 만들어진 connection을 담당하는 stream객체를
# 메모리에서 지우는 역할을 수행
# close함수를 호출하지 않으면 메모리에 계속 남아 있어서
# 반드시 메모리에서 지워주어야 한다.

# 파일 읽기
try:
    test_file2 = open('test2.txt', 'r')
    lines = test_file2.readlines()
    # print(lines)
    for line in lines:
        print(line)
except FileNotFoundError:
    print("해당 파일을 찾을 수 없음")
except IOError:
    print("읽고 쓰는데 문제가 생겼음")
except NameError:
    print("해당 이름의 파일을 찾을 수 없음")
except:
    print("파일을 처리하는데 문제가 생겼음")
finally:
    try:
        test_file2.close()
    except:
        print('파일을 닫는데 문제가 생김')
