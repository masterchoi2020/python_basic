# 지역변수와 전역변수
# 지역변수: 함수내에서만 사용할 수 있는 변수
# (즉, 함수 호출시 변수가 만들어지고 함수 종료시 변수가 사라짐)
# 전역변수: 프로그램 어디에서든 불러 사용할 수 있는 변수

gun = 10  # 전역변수 초기화

def checkpoint(soldiers): # 경계근무시 총 들고 나감
    # gun = 20   # 지역변수gun 초기화 (이거 설정 안 하면 에러 발생함)

    global gun  # 전역 공간에 있는 gun을 checkpoint함수의 변수로 사용하겠다.
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

# global로 변수 선언하지 않고 전역변수 사용
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun

print("전체 총: {0}".format(gun))
# checkpoint(2)  # 2명이 경계근무를 나가면서 총 2자루 들고 나감

# 인자로 전역변수에 설정된 gun=10을 사용하여 checkpoint_ret()함수 호출 후 retun gun 으로 반환된 값을 gun에 저장
gun = checkpoint_ret(gun, 2)  
print("남은 총: {0}".format(gun))

