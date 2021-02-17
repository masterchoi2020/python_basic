from tkinter import  *

root = Tk()
root.title("KITT GUI")
root.geometry("640x480")

label = Label(root, text="메뉴를 선택하세요").pack()
burger_var = IntVar()  # burger_var 변수에 int형으로 값을 저장한다.
btn_burget1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burget1.select()   # 기본값으로 선택

btn_burget2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burget3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var)

btn_burget1.pack()
btn_burget2.pack()
btn_burget3.pack()


label2 = Label(root, text="음료를 선택하세요").pack()
drink_var = StringVar()  # drink_var변수에 String형으로 값을 저장
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()  #기본값으로 선택
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get())  # 햄거버 중 선택된 라디오 항목의 value(값) 반환
    print(drink_var.get())  # 음료 중 선택된 라디오 항목의 value(값) 반환
 
btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()

