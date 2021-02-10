# 예외처리
'''
try:
    실행할 문장

except Exception as err:
    print(err)

finally:
    print("예외 구문에서 무조건 실행되는 문장")    
'''

'''
try:
    nums = []
    print("나누기 전용 계산기 입니다.")
    nums.append(int(input("첫 번째 숫자를 입력하세요: ")))
    nums.append(int(input("두 번째 숫자를 입력하세요: ")))
    nums.append(int(nums[0] /nums[1]))

    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")

except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("err")



# 의도적으로 에러 발생시키기
try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))

    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
'''

# 사용자 정의 예외 처리

class BingNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg


try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))

    if num1 >= 10 or num2 >= 10:
        raise BingNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))


except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

except BingNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)

# finally : 예외처리 구문에서 정상처리/에러처리에 상관없이 무조건 실행되는 구문
finally:
    print("계산기를 이용해 주셔서 감사합니다.")

