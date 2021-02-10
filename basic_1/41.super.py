# super


# 일반 유닛 클래스 만들기
class Unit:
    def __init__(self, name, hp, speed):  # speed 추가
        self.name = name
        self.hp = hp
        self.speed = speed
        
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도{2}]".format(self.name, location, self.speed))


# 공격 유닛 클래스로 만들기
# AttackUint(상속받을 클래스 입력)
class AttackUint(Unit):  #공격 유닛은 일반유닛을 상속 받아서 만들어 짐
    def __init__(self, name, hp, speed, damage):  # speed 추가
        # 유닛의 생성자를 호출해서 name, hp를 정의해야 함
        Unit.__init__(self, name, hp, speed)  #이름과 체력(hp)를 일반 유닛 클래스를 상속받아 생성
        self.damage = damage  # 추가로 damage에 대해서만 재정의 해 주면 됨

# self는 자기 자신을 의미하고, 클래스 내에서 메소드 앞에는 self를 항상 적어줘야 한다.
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다.[공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) 
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0: 
            print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기, 마린/파이어뱃/탱크 등을 수송 (공격 기능 없음)

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUint, Flyable):  # AttackUnit과 Flyable 클래스를 상속 받음
    def __init__(self, name, hp, damage, flying_speed):
        AttackUint.__init__(self, name, hp, 0, damage)  #날아다니는 스피드가 있으므로 지상 스피드는 0으로 설정
        Flyable.__init__(self, flying_speed)

    # 연산자 오버로딩을 사용하기 위해 move()함수를 새롭게 정의
    def move(self, location): # move() 함수 재정의
        print("[공중 유닛 이동]")
        self.fly(self.name, location)  # 공중 유닛은 fly()함수를 통해서 이동 함


# 건물 생성 클래스
class BuildingUnit(Unit):   # BuildingUint클래스는 Unit 클래스를 상속받음
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)   # 상속받은 클래스 초기화 방법1 : 상속받을 클래스(부모클래스).__init__()  으로 초기화
        super().__init__(name, hp, 0)# 상속받은 클래스 초기화 방법2 (super 이용) : super로 초기화하면 self없이 사용한다.
        self.location = location

