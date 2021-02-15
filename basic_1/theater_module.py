# 모듈
# 함수정의 또는 클래스 등의 파이썬 문장을 담고있는 파일을 의미 (모듈의 확장자는 .py 임.)

# 사람 수에 따른 극장 표 가격 산출 모듈 작성
# 일반 가격
def price(people):
    print("{0}명 가격은 {1}원 입니다.".format(people, people * 10000))

# 조조 할인 가격
def price_mornig(people):
    print("{0}명 조조 할인 가격은 {1}원 입니다.".format(people, people * 6000))

# 군인 할인 가격
def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1}원 입니다.".format(people, people * 4000))

