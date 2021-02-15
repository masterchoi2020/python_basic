# 패키지 : 모듈들을 모아 놓은 집합(하나의 디렉토리 안에 여러 모듈 파일들을 모아 놓은 것)

# 1.여행 패키지 생성 (travel 이라는 패키지 생성)
# 2.tavel 디렉토리 내부에 vietnam.py, thailand.py, __init__.py  3개의 파일 생성
# 3.vietnam.py 에는 베트남 여행관련 class 내용 입력, thailand.py 에는 태국 여행관련 class 내용 입력, 
# __init__.py  에는 일단 비워둔채 49.package.py 로 이동


'''
# 생성해 둔 모듈 사용하기
import travel.thailand # 주의!: import 시 맨 뒤(thailand) 부분은 모듈 또는 패키지만 가능(클래스 또는 함수는 직접 import 할 수 없다.)
# import travel.thailand.ThailandPackage()  # 사용불가

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
'''

# travel 안에 있는 thailand 모듈에서 ThailandPackage 라는 클래스를 import 함
# from ~ import 구문에서는 모듈이나 패키지, 클래스 또는 함수를 import 할 수 있다.
# from travel.thailand import ThailandPackage  
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.vietnamPackage()
# trip_to.detail()

'''
# __all__
from travel import *  # travel 패키지에서 모든 것(*)을 사용하겠다(오류 발생 함)
trip_to = vietnam.vietnamPackage()
trip_to.detail()
'''
# 오류발생 이유: import 에 *을 쓰는것은 travel 패키지에서 모든 것을 가져 오겠다는 의미 이지만
# 개발자가 공개 범위를 설정해 줘야 사용가능, 즉 패키지 내에서 import 되기를 원하는 것은 공개하고
# import 되기를 원하지 않는 것은 비공개로 설정 가능하다

# -> travel 디렉터리내에 만들어 둔 __init__.py 파일에 __all__ = ["vietnam"] 내용 입력
# 위 코드 다시 실행

from travel import *  # (정상 실행됨)
trip_to = vietnam.vietnamPackage()
trip_to.detail()

# -> travel 디렉터리내에 만들어 둔 __init__.py 파일에 __all__ = ["vietnam", "thailand"] 내용 입력
# 위 코드 다시 실행
from travel import *  # (정상 실행됨)
trip_to = vietnam.vietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()

# 모듈 직접 실행
# 모듈에 if __name__ == "__main__": 를 이용해 내부에서 모듈 호출 또는 외부에서 모듈 호출 확인


# 패키지, 모듈의 위치
# 현재 패키지 및 모듈은 동일 경로 또는 디렉토리에 존재 했음
# 모듈이 어느 경로에 있는 지 확인 (inspect.getfile(모듈명) 이용해 경로 확인)
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand)) # 우리가 만든 모듈 위치 확인

# travel 디렉토리에 있는 모듈을 random이 모듈이 있는 곳으로 이동한 후 실행 되는지 확인

