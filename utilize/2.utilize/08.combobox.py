import tkinter.ttk as ttk   # Combobox()함수 사용에 필요
from tkinter import *

root = Tk()
root.title("KITT GUI")
root.geometry("640x480")

# 읽기 쓰기가 가능한 콤보박스
values = [str(i) + "일" for i in range(1, 32)]  # 1 ~ 31까지의 숫자
commbobox = ttk.Combobox(root, height=5, values=values)
commbobox.pack()
commbobox.set("카드 결제일")  # 최초 목록 제목 설정(버튼 클릭을 통한 값 설정도 가능)

# 읽기 전용 콤보 박스
readonly_commbobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_commbobox.current(0)  # 0번째 인덱스 값 선택
readonly_commbobox.pack()

def btncmd():
    print(commbobox.get())  # 선택된 값 표시
    print(readonly_commbobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()