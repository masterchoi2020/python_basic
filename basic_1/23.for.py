# 반복문 for
# print("대비번호: 1")
# print("대비번호: 2")
# print("대비번호: 3")
# print("대비번호: 4")

#randrange()
for waiting_no in range(1, 6):  # 1,2,3,4,5
    print("대기번호: {0}".format(waiting_no))


# 문자열 반복
starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비 되었습니다.".format(customer))


#한줄 for 문
#출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1,2,3,4,5]
print(students)
# i에 100을 더한값을 넣을 예정
students = [i+100 for i in students]   # i는 students의 데이터를 불러 오면서 i+100한 값을 리스트의 요소로 넣겠다 
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]  # i는 students의 데이터를 불러오면서 len(i) 길이값을 리스트에 넣겠다.
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)


