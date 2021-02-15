# 내장 함수 : 별도의 import 가 필요없이 바로 사용할 수 있는 함수

# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어 입니다.".format(language))


# dir : 어떤 객체를 넘겨 줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random # 외장 함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random))  # random 모듈에서 쓸 수 있는 함수를 보여준다.


# lst = [1, 2, 3]
# print(dir(lst))  # lst에서 쓸 수 있는 내용 출력

name = "Kim"
print(dir(name))

# 구글 조회 : list of python buitins 로 조회 (파이썬에서 쓸 수 있는 내장 함수 확인 가능)