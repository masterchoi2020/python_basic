
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

# 메딕 : 의무병 (공격력이 없다.)

# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUint("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)




#5. 상속