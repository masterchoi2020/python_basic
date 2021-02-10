from random import *

# 일반 유닛 클래스 만들기
class Unit:
    def __init__(self, name, hp, speed):  # speed 추가
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
        
    def move(self, location):
        # print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도{2}]".format(self.name, location, self.speed))


    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) 
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0: 
            print("{0} : 파괴되었습니다.".format(self.name))



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

    
# 마린 클래스 만들기
class Marine(AttackUint):
    def __init__(self):
        AttackUint.__init__(self, "마린", 40, 1, 5)

    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크 클래스 생성
class Tank(AttackUint):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
    seiz_developed = False  # 시즈모드 개발 여부

    def __init__(self):
        AttackUint.__init__(self, "탱크", 150, 1, 35)
        self.seiz_mode = False

    def set_seize_mode(self):
        if Tank.seiz_developed == False:
            return

        # 현재 시즈모드가 이닐 때 -> 시즈 모드
        if self.seiz_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seiz_mode = True
        # 현재 시즈모드일 때 -> 시즈 모드 해제  
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seiz_mode = False


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
        # print("[공중 유닛 이동]")
        self.fly(self.name, location)  # 공중 유닛은 fly()함수를 통해서 이동 함

# 레이스 클래스 생성
class wraith(FlyableAttackUnit):

    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.cloked = False #클로킹 모드(해제 상태)

    def clocking(self):
        if self.cloked == True:   # 클로킹 모드 -> 모드 해제
            print("{0} : 클로킹 모드 해제 합니다.".format(self.name))
            self.cloked == False

        else:  # 클로킹 모드 해제 -> 모드 설정
            print("{0} : 클로킹 모드 설정 합니다.".format(self.name))
            self.cloked == True

def game_start():
    print("[알리] 새로운 게임을 시작합니다.")

def game_over():
    print("player : gg")
    print("[player] 님이 게임에서 퇴장하셨습니다.")


# 게임 진행
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = wraith()

# 유닛 일괄 관리 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)


# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료 되었습니다.") 

# 공격 모드 준비 (마린 : 스팀팩탱크: 시즈모드, 레이스: 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, wraith):
        unit.cloked
    
# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for uint in attack_units:
    unit.damaged(randint(5, 21))  # 공격은 랜덤으로 받음 (5 ~ 20)

# 게임 종료
game_over()