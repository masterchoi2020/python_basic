# 이전에 작성한 theater_module 모듈 사용

'''
import theater_module  # theater_module.py 모듈에서 확장자명은 입력할 필요 없음

#모듈 사용방법1 : theater_module 모듈명 입력 후 뒤에 .price() 처럼 함수를 호출해서 사용
theater_module.price(3)  # 3명이 영화 보러 갔을 때 가격
theater_module.price_mornig(4)  # 4명이 조조 할인 영화 보러 갔을 때 가격
theater_module.price_soldier(5)  # 3명의 군인이 영화 보러 갔을 때 가격
'''

'''
# 모듈 사용방법2 : 모듈 이름이 길 경우 as 를 이용해 별칭을 부여해 사용 
import theater_module as  mv   
mv.price(3)
mv.price_mornig(4)
mv.price_soldier(5)
'''

'''
# 모듈 사용방법3 : from을 이용해 theater_module 글자 안 적고 바로 price() 함수를 호출해서사용
from  theater_module import *  # theater_module 의 내용을 모두 가져와 사용하겠다는 의미
price(3)
price_mornig(4)
price_soldier(5)
'''


'''
# 모듈 사용방법4: 모듈에서 필요한 함수만 import 해서 사용하기
from theater_module import price, price_mornig  #내가 사용할 함수만 명시적으로 입력해서 사용
price(3)
price_mornig(4)
# price_soldier(5)  # 사용 불가(x)
'''

# 모듈 사용방법5: 모듈에서 필요한 함수만 import한 이후 as를 이용해 별칭을 부여해서 사용하기
# theater_module 모듈내 price_soldier() 함수만 사용하는데, 별칭으로 as를 이용하겠다.
from theater_module import price_soldier as price
price(3)



