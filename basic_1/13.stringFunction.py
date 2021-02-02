#문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))

print(python.replace("Python", "Java")) # replace("찾을 문자", "바꿀 문자")

index = python.index("n")  # python 에서 n 문자가 몇번째 위치에 있는지 확인
print(index)

index = python.index("n", index + 1)  # python 에서 n 문자를 찾은 이후 부터 두번째 n 찾기
print(index)

print(python.find("n")) # python 에서 n 문자가 몇번째 위치에 있는지 확인 (index와 동일 기능)

print(python.find("Java")) # 원하는 값이 없으면 -1 값 반환 
# print(python.index("Java")) # 원하는 값이 없으면 오류 발생

print(python.count("n")) # n이 몇번 등장하는지 계산