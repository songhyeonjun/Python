try:
    file = open("member.txt", "r")
    lines = file.readlines()
    print("이름 \t나이 \t연락처")
    print("-" * 22)
    for line in lines:
        one = line.split(',')
        print(one[0].strip() + "\t" +
              one[1].strip() + " \t" +
              one[2].strip())
except:
    print("오류발생")
finally:
    file.close()

