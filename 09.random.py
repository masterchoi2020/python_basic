#랜덤 함수
from random import *

print(random())  # 0.0 ~ 0.1 미만의 임의의 값 생성
print(random() * 10)  # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))  # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10))  # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10))  # 0 ~ 10 미만의 임의의 값 생성

#1부터 10 이하의 값 생성
print(int(random() * 10) + 1) 

#로또 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1, 45)) # 양 끝값을 모두 포함해서 출력 (1 ~ 45 이하의 값 생성)