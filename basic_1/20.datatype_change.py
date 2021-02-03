# 자료구조의 변경

# set으로 자료생성
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

# set을 list 자료형으로 변경
menu = list(menu)
print(menu, type(menu))

# list를 tuple 자료형으로 변경
menu = tuple(menu)
print(menu, type(menu))

# tule을 set 자료형으로 변경
menu = set(menu)
print(menu, type(menu))