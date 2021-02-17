from tkinter import *

root = Tk()
root.title("KITT GUI")
root.geometry("640x480")

# selectmod = "extended" : 리스트 여러 개 선택가능(single: 하나만 선택가능), 
# height=0 은 모든 리스트를 보여줌(지정된 숫자만큼 보여준다.)
listbox = Listbox(root, selectmod="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")  # END는 끝에 추가
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # 리스트 목록 삭제
    # listbox.delete(END)  # 맨 뒤에 항목 삭제
    # listbox.delete(0)    # 맨 앞에 항목 삭제

    # 갯수 확인
    print("리스트에는", listbox.size(), "개가 있습니다.")

    # 항목 확인(시작 idx, 끝 idx)
    print("1번째 부터 3번째 까지의 항목: ", listbox.get(0, 2))

    # 선택된 항목 확인 (위치로 반환 (ex: (1, 2, 3))
    print("선택된 항목: ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()