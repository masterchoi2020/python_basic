from tkinter import *

root = Tk()
root.title("KITT GUI")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y") # fill="y" : scrollbar 가 frame 크기에 맞게 꽉 채워짐

# yscrollcommand : y축 (상/하)으로 스크롤바 작성
# scrollbar.set : set 이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmod="extended", height=10, yscrollcommand=scrollbar.set)

for i in range(1, 32):   # 1 ~ 31일
    listbox.insert(END, str(i) + "일")  # 1일, 2일 ...
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)  # listbox도 scrollbar와 연동하도록 맵핑(설정)하기

root.mainloop()