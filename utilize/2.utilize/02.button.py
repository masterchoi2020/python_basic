from tkinter import *

root = Tk()
root.title("KITT GUI")

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼222222222222") # padx, pady 는 가변적 여백
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")

btn4 = Button(root, width=10, height=3, text="버튼4444444444")  # width, height는 고정된 크기
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file=r"D:\python_workspace\python_basic_1\utilize\2.utilize\img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭 되었습니다.")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()