# 반복문 while
'''
customer = "토르"
index = 5
while index >=1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았습니다.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기 처분 되었습니다.")
'''


#무한 루프
'''
customer = "아이언맨"
index = 1
while True:
    print("{0}, 커피가 준비 되었습니다. 호출{1}회".format(customer, index))
    index += 1
'''

customer = "토르"
person = "Unkown"

while person !=customer:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")