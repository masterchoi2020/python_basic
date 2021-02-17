# 파이썬 GUI 프로그램밍
from tkinter import *
root = Tk()
root.title("KITT GUI")
# root.geometry("640x480")    # 가로 x 세로
# root.geometry("640x480+100+300")  # 가로 x 세로 + x좌표 + y좌표
root.resizable(False, False)    # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)
root.mainloop()