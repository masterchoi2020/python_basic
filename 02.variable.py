#변수

# 애완동물을 소개해 주세요~
animal = '고양이'
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >=3

print("우리집" + animal + "의 이름은" + name + "에요")
hobby = '공놀이'
# print(name + "는" + str(age)+ "살이며," + hobby +"을 아주 좋아해야")

#콤마(,)를 이용하면 str(age)하지 않고 age로 사용가능(단 (콤마(,) 가 들어하면 한칸씩 띄어쓰기가 이뤄진다.)
print(name, "는", age, "살이며, ", hobby, "을 아주 좋아해야")
print( name + "는 어른일까요?" + str(is_adult))