# 마린 : 공격 유닛, 군인 총을 쏠 수 있음

# name = "마린" # 유닛의 이름
# hp = 40  #유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반모드 /시즈모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))


# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)


#1. 클래스를 이용하여 유닛 생성하기
# 일반 유닛 클래스 만들기
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 클래스 사용
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)


#2. __init__ 는 생성자로써 marin1 또는 tank가 생성될 때 자동으로 호출된다.
# 객체 : 클래스로 부터 만들어지는 것들을 객체라고 한다.
# marine과 tank는 Unit 클래스의 인스턴스라고 부른다.
# 객체 생성시에는 __init__함수에 제시된 매개변수의 개수와 동일 개수의 값을 넣어줘야 객체를 만들 수 있다.한다.


#3.멤버 변수
# 멤버변수는 클래스 안에서 생성된 변수로 .name, .hp , .damage 처럼 점(.)을 이용해 멤버변수에 접근해사용할 수 있다.

# 레이스 생성 : 공중유닛, 비행기 , 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))


# 마인트 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True  # 클래스로 생성된 객체에 변수를 추가해서 사용 가능 (변수확장 가능)

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

#4. 메소드
class AttackUint:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

# self는 자기 자신을 의미하고, 클래스 내에서 메소드 앞에는 self를 항상 적어줘야 한다.
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다.[공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) 
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0: 
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUint("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

