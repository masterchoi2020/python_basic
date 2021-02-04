# pickle 프로그램상에서 사용하고 있는 데이터를 파일 형태로 저장

import pickle

# 1.pickle로 데이터 쓰기
# pickle을 쓰기 위해서는 항상 binary 타입으로 정의 해줘야 한다.
# pickle에서는 인코딩을 별도로 설정할 필요 없음
profile_file = open("profile.pickle", "wb")  # profile.pickle 로 데이터 쓰기
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)

pickle.dump(profile, profile_file)  # pickle 파일에 data 쓰기 (profile에 있는 정보를 file에 저정)
profile_file.close()

# 2. pickle로 데이터 읽어 오기
profile_file = open("profile.pickle", "rb")  # profile.pickle 의 데이터 읽기
profile = pickle.load(profile_file)   # file에 있는 데이터를 그대로 profile에 불러와 준다.
print(profile)
profile_file.close()


