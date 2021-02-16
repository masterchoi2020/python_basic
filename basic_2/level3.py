# 신조어 퀴즈 프로그램
'''
Quiz) 신조어 퀴즈 클래스를 만드시오.

 - Word 클래스 작성 (신조어 퀴즈를 내는 클래스 작성)
 __init__(...) : 신조어, 보기1, 보기2, 정답을 받아서 멤버 변수 설정
 show_question(...) : 질문 내용 표시
 check_answer(...) : 입력값이 정답인지 확인하여 "정답입니다." 또는 "틀렸습니다." 출력

 - 주어진 프로그램 예제
 word = Word("얼죽아", "얼어 죽어도 아메리카노", "얼굴만은 죽어도 아기피부", 1)
 word.show_question()
 word.check_answer(int(input("=>")))

 - 출력 결과
 "얼죽아"의 뜻은?
 1.얼어 죽어도 아메리카노
 2.얼굴만은 죽어도 아기피부
 =>

 정답입니다.
'''

class Word:
    def __init__(self, word, ex1, ex2, answer):
        self.word = word # 멤버변수 설정 
        self.ex1 = ex1   # (사용자가 입력하는 매개변수(word, ex1, ex2) 값으로 초기화)
        self.ex2 = ex2
        self.answer = answer

    def show_question(self):
        print(f"\"{self.word}\"의 뜻은?")
        print("1." + self.ex1)
        print("2." + self.ex2)

    def check_answer(self, user_input):
        if user_input == self.answer:
            print("정답입니다.")
        else:
            print("틀렸습니다.")


# word = Word("얼죽아", "얼어 죽어도 아메리카노", "얼굴만은 죽어도 아기피부", 1)
# word = Word("혼코노", "혼자서는 코딩 노노", "혼자 코인 노래방", 2)
word = Word("애빼시", "애교 빼면 시체", "애들은 빼빼로 시시해", 1)
word.show_question()
word.check_answer(int(input("=>")))