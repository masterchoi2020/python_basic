#6.다중 상속 :  2개 이상의 부모 클래스로 부터 상속을 받는 경우

# 공중유닛 : 1)일반 유닛 속성, 2)공격 유닛 속성, 3)수송기 속성


# 일반 유닛 클래스 만들기
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        

# 공격 유닛 클래스로 만들기
# 유닛의 내용을 상속 받아 어텍 유닛 만들기
# AttackUint(상속받을 클래스 입력)
class AttackUint(Unit):  #공격 유닛은 일반유닛을 상속 받아서 만들어 짐
    def __init__(self, name, hp, damage):
        # self.name = name  #(self.name, self.hp 는 따로 설정할 필요 없어짐)
        # self.hp = hp
        
        # 유닛의 생성자를 호출해서 name, hp를 정의해야 함
        Unit.__init__(self, name, hp)  #이름과 체력(hp)를 일반 유닛 클래스를 상속받아 생성
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
        AttackUint.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5) #체력 200, 데미지 6, 스피드 5
valkyrie.fly(valkyrie.name, "3시")  # Flyable 클래스는 나는 정보만 있고 이름 정보가 없어 valkyrie.name으로 이름 정보 추가
