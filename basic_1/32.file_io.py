# 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8") # score.txt 파일을 쓰기(w) 모드로 열어줌
# print("수학: 0", file=score_file)  # 수학: 0 이라는 내용을 score_file 이라는 곳에 입력
# print("영어: 50", file=score_file)  # 영어: 50 이라는 내용을 score_file 이라는 곳에 입력
# score_file.close()  # 파일에 값들을 다 입력하고 나면 열었던 파일을 닫아줘야함 

# write를 이용해 입력
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학: 80")
# score_file.write("\n코디: 100") #score_file.write() 이용시 자동 줄바꿈 안되므로 \n을 사용해 줄바꿈 처리함
# score_file.close()

# 파일에서 data읽어 오기
# 한번에 전체 데이터 읽어 오기
# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.read())  # 한번에 파일의 내용을 모두 읽어오는 방법(단점: 부하가 많이 발생함)
# score_file.close()

# 파일에서 data읽어 한 줄씩 읽어오기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) # 한 줄씩 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline()) # 한 줄씩 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline()) # 한 줄씩 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline()) # 한 줄씩 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# score_file.close()


# while 문을 이용해 파일에서 data읽어 한 줄씩 읽어오기
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# 리스트에 담아서 파일의 data 출력하기
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # readlines() 를 이용하면 list 형대로 저장됨
for line in lines:              # list의 내용을 한 줄씩 읽어서 출력해줌
    print(line, end="")
score_file.close()