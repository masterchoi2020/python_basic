# 함수
'''
#함수 정의

def 함수명():
    실행될 명령문
'''
def open_account():
    print("새로운 계좌가 생성되었습니다. ")

#함수 호출 : 함수명()을 불러주면 함수가 호출된다.
open_account()


# 전달값과 반환값
def deposit(balance, money):   # 입금 함수에는 전달값 balance와 money를 전달받아 사용
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money


#출금
def withdraw(balance, moeny): # 출금
    if balance >= moeny:   # 잔액이 출금액보다 크다면
        print("출금이 완료 되었습니다. 잔액은 {0}원 입니다.".format(balance - moeny))
        return balance - moeny
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

#출금시 수수료
def withdraw_night(balance, moeny): #저녁에 출금
    commission = 100 #출금 수수료 100원
    return (commission, balance - moeny -commission)

balance = 0 # 초기 잔액 0
balance = deposit(balance, 1000)  # 잔액(balance)와 입금액(1000)을 deposit()의 전달값으로 입력
print(balance)
# balance = withdraw(balance, 2000)
balance = withdraw(balance, 300)
print(balance)
commission, balance = withdraw_night(balance, 200)
print("수수료 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))


print("-" * 50)
# 함수의 기본값(defalt) 설정
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")


print("-" * 50)
# 같은 학교 같은 학년 같은 반 같은 수업
# 프로파일에 전달값의 기본값 설정
# 함수인자에 기본값이 설정되어 있을 경우, 함수 호출시 인자값을 넣지 않으면 기본값을 사용하게 된다.
def profile(name, age=17, main_lang="파이썬"): 
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))

profile("유재석") # age와 main_lang을 입력하지 않았으므로 기본값을 적용하게 된다.
profile("김태호")


# 키워드 값을 이용한 함수 호출
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바",age=20 ,name="유재석")

# 가변인자를 이용한 함수 호출
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    # end=" "  프린트문이 끝날때 줄바꿈하지 않고 " "으로 밑에 출력문장을 연결해서 출력
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")  
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "python", "java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")
print("-" * 50)

#가변인자 사용(함수에 다양한 인자값이 들어 가야 할 때 사용)
def profile(name, age, *language): # *language 로 설정하면 넣고 싶은 개수만큼 값을 넣어 사용가능
    # end=" "  프린트문이 끝날때 줄바꿈하지 않고 " "으로 밑에 출력문장을 연결해서 출력
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")  
    for lang in language:
        print(lang, end=" ")
    print()  # 줄 바꿈용 

profile("유재석", 20, "python", "java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift")