#continue와 break
absent = [2, 5]  # 결석
no_book = [7] # 책을 안 가져온 학생번호
for student in range(1, 11):    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    if student in absent:
        continue        # continue를 만나면 다음 문장을 건너뛰고(skip) 다음 반복을 계속 실행
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))    
        break           # 반복문 탈출(이후 반복문 실행 안하고 탈출)
    print("{0}, 책을 읽어봐".format(student))





