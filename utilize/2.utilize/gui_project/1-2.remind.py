# 리스트에서 revers()함수와 reversed

lst = [1,2,3,4,5]
print(lst)
lst.reverse()   # 원본에 영향 있음(O) : 원본 데이터의 순서를 바꿔버림
print(lst)

lst2 = [1,2,3,4,5]
print("리스트2 뒤집기 전: ", lst2)

lst3 = reversed(lst2) # 원본에 영향 없음(x) : 원본 데이터엔 영향이 없고 출력시 바뀐 값만 lst3에 넣어줌
print("리스트2 뒤집은 후: ", lst2)
print("리스트3: ", list(lst3))

# zip 사용법(같은 열끼리 붂어준다.)
kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banana", "orange"]

print(list(zip(kor, eng)))

# unzip 사용법(zip 앞에 *를 넣어줘 값들을 분리시킨다.)
mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(*mixed)))

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)