from tkinter import *

root = Tk()
root.title("KITT GUI")
root.geometry("640x480")


Label(root, text="메뉴를 선택해 주세요").pack(side="top")  # Label이 생성될 위치 top
Button(root, text="주문하기").pack(side="bottom")   # Button이 생성될 위치 bottom


# label이 없는 메뉴 프레임
frame_burger = Frame(root, relief="solid", bd=1)  # relief: 테두리 모양, bd: border
frame_burger.pack(side="left", fill="both", expand=True)  # fill="both": label을 위/아래로 꽉 채우기, expand=True : 좌우로펼치기

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

# label이 있는 음료 frame
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()

root.mainloop()