from tkinter import *

root = Tk()
root.title("KITT GUI")
root.geometry("640x480")

label = Label(root, text="안녕하세요.")
label.pack()

photo = PhotoImage(file=r"D:\python_workspace\python_basic_1\utilize\2.utilize\img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label.config(text="또 만나요")  #클릭 시 설정 내용 변경

    # Garbage Collection : 불필요한 메모리 공간 해제 -> photo2를 지워버리므로 지워지지 않게 global 변수로 photo2 선언
    global photo2
    photo2 = PhotoImage(file=r"D:\python_workspace\python_basic_1\utilize\2.utilize\img2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()