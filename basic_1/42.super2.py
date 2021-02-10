# super() 를 이용하여 클래스 초기화하면 다중 상속에서 문제가 발생할 수 있다.

class Unit:
    def __init__(self): # Unit 클래스 초기화
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__() # super()를 이용하면 다중 상속시 뒤에 나오는 생성자는 반영아됨
        # 다중 상속을 사용해 모두 부모 클래스를 초기화 해야 한다면, 각각의 클래스를 초기화 해 줘야 한다.
        Unit.__init__(self)
        Flyable.__init__(self)


# 드랍쉽 클래스를 이용해 생성
dropship = FlyableUnit()  # Unit생성자는 초기화되어 생성됨, 그러나 Flyable은 생성안됨