# 외장 함수
# 구글링 : list of python modules 로 조회 (외장 함수 목록 확인 가능)

# glob : 경로 내의 디렉토리 / 파일 목록 조회(윈도우의 dir 과 같은 역할)
# import glob
# print(glob.glob("*.py"))  # 경로내 확장자가 py인 모든 파일 검색


# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) #현재 디렉토리 확인

# 디렉토리 생성
# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 디렉토리 입니다.")
#     os.rmdir(folder)
#     print(folder, "디렉토리를 삭제 하였습니다.")
# else:
#     os.makedirs(folder)  # 디렉토리 생성
#     print(folder, "디렉토리를 생성 하였습니다.")


# 빈파일 생성
# f = open("test.txt", 'w', encoding="UTF8")
# f.close()

# 파일에 내용 입력
# f = open("test.txt", "w", encoding="UTF8")
# f.write("파일에 내용입력합니다. \n")
# f.close


# 텍스트 파일의 내용 읽기
# f = open("test.txt", "r", encoding="UTF8")
# contents = f.read()
# print(contents)
# f.close()

# 파일 이름 변경
# os.rename(src, dst)
# os.rename("test.txt", "new_test.txt")


# 파일 삭제
os.unlink("new_test.txt")


print(os.listdir())


# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# datetime
import datetime
print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격을 알려줌
today = datetime.date.today()  # 오늘 날짜 저장
td = datetime.timedelta(days=100)  # 100일 저장
print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후 날짜 출력
