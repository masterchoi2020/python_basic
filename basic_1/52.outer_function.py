# 외장 함수
# 구글링 : list of python modules 로 조회 (외장 함수 목록 확인 가능)

# glob : 경로 내의 폴더/ 파일 목록 조회(윈도우의 dir 과 같은 역할)
# import glob
# print(glob.glob("*.py"))  # 경로내 확장자가 py인 모든 파일 검색

'''
# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) #현재 디렉토리 확인

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더 입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제 하였습니다.")
else:
    os.makedirs(folder)  # 폴더 생성
    print(folder, "폴더를 생성 하였습니다.")


print(os.listdir())
'''

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
