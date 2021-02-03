'''
Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시요.

조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
조건2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3: random 모듈의 shuffle과 sample을 활용

(출력 예제)
--- 담첨자 발표 ---
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
  -- 축하 합니다. --

(활용 예제)
from random import *

lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst)  # shuffle()함수: lst안의 요소들을 무작위로 섞어 놓음
print(lst)
print(sample(lst, 1)) # sample(리스트, 뽑을 개수)함수는 lst에서 무작위로 1개를 뽑겠다
'''

from random import *

users = range(1, 21) # 1부터 20까지 숫자를 생성
# print(type(users))
users = list(users)  # range 타입의 users를 list타입으로 변경
# print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) #4명 중에서 1명은 치킨, 3명은 커피

print("--- 당첨자 발표 ---")
print("치킨 당첨자: {0}".format(winners[0]))
print("커피 당첨자: {0}".format(winners[1:]))
print("--- 축하합니다. ---")








