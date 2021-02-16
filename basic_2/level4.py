# 공포의 행맨 게임 프로그램
'''
Quiz) 행맨 게임(영어 단어 퀴즈) 프로그램을 만드시오

 - 리스트에 3개 이상의 단어를 추가
 예) apple, banana, orange

 - 위 리스트에서 랜덤으로 1개의 단어를 선택

 - 단어의 길이에 맞게 밑줄 출력
 예) apple의 경우 _ _ _ _ _

 - 사용자로 부터 1글자씩 입력을 받되, 단어에 입력값이 포함되면 'Correct'출력, 아니면 'Wrong'출력

 - 매번 입력을 받을 때마다 현재까지 맞힌 글자들 표시 (맞히지 못한 글자는 밑줄 출력)
 예) a 입력시 : a_ _ _ _ 
     p 입력시 : a p p _ _
     c 입력시 : a p p _ _

 - 정답을 맞히면 Success 출력 후 프로그램 종료(단, 횟수 제한은 없음)

'''
from random import *
words = ["apple", "banana", "orange"]
word = choice(words)  # choice()함수 : 리스트에서 있는 요소 중 하나를 랜덤으로 가져온다.
print("answer : " + word)

letters = "" # 사용자로 부터 지금까지 입력받은 모든 알파벳

while True:
    succeed = True
    print()
    for w in word:  # a p p l e
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succeed = False
    print()
    
    if succeed:
        print("Success")
        break
    
    letter = input("Input letter > ") # 사용자 입력 받기
    if letter not in letters:
        letters += letter

    if letter in word:
        print("Correct")
    else:
        print("Wrong")