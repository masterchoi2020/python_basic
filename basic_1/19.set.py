# 세트(set) : 집합으로 중복이 안되고, 순서가 없다.

# set 생성방법1 : 중괄호{}를 이용
my_set = {1, 2, 3, 3, 3}  # 세트는 중괄호{}에 값만 입력하면 set 가 됨
# 주의!:딕셔너리는 중괄호{key:value}에 키와밸류가 들어감 
print(my_set) # 중복허용하지 않음

#set 생성2: set() 함수를 이용
test = set([1, 2, 3, 3, 3])
print(test)

# 개발자 세트
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java를 할 수 있거나 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# 집합에 데이터 추가
# python을 할 줄 아는 사람이 늘언남
python.add("김태호")
print(python)

# 집합에서 데이터 제거
# java를 잊었어요
java.remove("김태호")
print(java)