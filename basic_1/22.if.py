# 분기문 if
'''
if 조건:
    실행 명령문
'''


'''

# weather = "비"
# weather = "미세먼지"
# weather = "맑아요"
weather = input("오늘 날씨는 어때요? ")  # input()은 사용자 입력을 받는 함수

if weather == "비" or weather == "눈":
    print("우산을 챙키세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없어요")

'''

temp = int(input("기온이 어때요? "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")

elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")
