# with를 이용해 파일로 데이터를 읽고, 쓰기
# import pickle

# pickle을 사용해 일반 파일을 읽고, 쓰기
# with open("profile.pickle", "rb") as profile_file:   # profile.pickle 파일을 바이너리로 읽어 들인 후 profile_file 변수로 저장
#     print(pickle.load(profile_file))    # pickle.load()로 불러와서 출력 (파일을 close() 할 필요가 없음)


# pickle을 사용하지 않고 일반 파일을 읽고, 쓰기
# with open("study.txt", "w", encoding="utf8") as study_file:  # study.txt 파일을 쓰기모드로 연 후 study_file 변수로 저장
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with로 파일 읽어 들이기
with open("study.txt", "r", encoding="utf8") as study_file:   # study.txt 파일을 읽어들여 study_file 변수로 저장
    print(study_file.read())  # read(): 파일의 모든 내용 한번이 읽어 들이기

