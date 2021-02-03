# 딕셔너리(사전) : key와 value 로 구성

# 중괄호{key:value}를 이용해 딕셔너리 생성 (참고:세트에소도 {}를 이용하나 중괄호{값}안에 값만 들어간다)
cabinet = {3:"유재석", 100:"김태호"}

#대괄호[] 를 이용해 딕셔너리 값 가져오기
print(cabinet[3])   # 리스트의 인덱스값을 쓰듯이 [key]를 이용해 value 값 가져오기
print(cabinet[100])  # key가 100인 것의 value 값(김태호) 가져옴

# get() 메서드를 이용해 dictionary 값 가져오기
print(cabinet.get(3))  # get() 메서드를 이용해 key가 3인 것의 value 값 가져오기

# 주의 사항
# print(cabinet[5])  #cbinet에 5라는 키가 존재하지 않으면 오류 발생하고 뒤의 코드 실행하지 않음
print("실행안됨")

print(cabinet.get(5))  #cbinet에 5라는 키가 존재하지 않으면 none 을 반환하고 뒤 코드 실행
print("good_실해됨")
print(cabinet.get(5, "사용가능"))  # 키가 존재하지 않을경우 디폴트 값으로 "사용가능"글자 넣어주는 방법

# key가 존재하는 in을 이용해 확인 
print(3 in cabinet)  # True
print(5 in cabinet)  # False

# String을 key 값으로 사용해도 됨
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])


# 딕션너리에 새로운 key:value 추가
# 새 손님
print(cabinet)
# cabinet에 "C-20"이라는 key를 추가하고, value는 "조세호"로 입력,
# 만약 "C-20"이라는 키가 사용 중이면 새로운 value로 업데이트가 된다.
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"  
print(cabinet)

# 딕션너리 key:value 삭제
# 간 손님
del cabinet["A-3"]
print(cabinet)


# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 딕셔너리 비우기
# 목욕탕 종료
cabinet.clear()
print(cabinet)
