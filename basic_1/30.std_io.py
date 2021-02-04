# 표준 입출력
print("Python", "Java", "JavaScript", sep=" ")
print("Python", "Java", "JavaScript", sep=" vs ")
print("Python", "Java", "JavaScript", sep=",")


print("Python", "Java", sep=",", end="?") # end="?" : 문장의 끝 부분을 ? 로 바꿔 달라는 의미
print("무엇이 더 재밌을까요?")
print("-" * 50)

# 표준 출력과 표준 에러
import sys 
print("Python", "Java", file=sys.stdout) #표준 출력으로 출력
print("Python", "Java", file=sys.stderr)  #표준 에러로 출력

# 출력 표멧 (예쁘게 좌/우 정렬하기)
# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}

# 딕셔너리에서 items()메소드 사용시 key:value 쌍으로 보여 준다.
for subject, score in scores.items():
    # print(subject, score)

    #ljust(8) 의미: 총 8칸의 공간을 확보 후 왼쪽으로 정렬하라
    #rjust(4) 의미: 총 4칸의 공간을 확보 후 오른쪽으로 정렬하라
    print(subject.ljust(8), str(score).rjust(4), sep=":")  
    

# 은행 대기 순번표
# 001, 002, 003, ...
for num in range(1, 21):
    # print("대기번호 : " + str(num))
    print("대기번호 : " + str(num).zfill(3))  # zfill(3)의미: 3칸의 공간을 확보하고 값이 없는 공간은 0으로 채워라


# 표준 입력
# input()을 이용해 사용자 입력값을 받으면 항상 str (문자열)로 인식하게 된다.
answer = input("아무 값이나 입력하세요 : ")  
print(type(answer))
print("입력하신 값은" + answer + "입니다.")
