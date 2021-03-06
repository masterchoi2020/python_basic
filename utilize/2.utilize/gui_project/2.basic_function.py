import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *   # __all__ 에 정의하지 않으면 서브모듈은 별로 명시 해 줘야 한다.
from tkinter import filedialog  # 서브모듈을 별도 명시적으로 import 해 줌

root = Tk()
root.title("KITT GUI")

# 파일 추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", \
            filetype = (("PNG 파일", "*.png"), ("모든파일", "*.*")), \
            initialdir = r"C:Users\KITT")
            # 최초에 사용자가 지정한 경로를 보여줌

    # 사용자가 선택한 파일 목록
    for file in files:
        # print(file)
        list_file.insert(END, file)
        

# 선택 삭제
def del_file():
    # print(list_file.curselection())

    for index in reversed(list_file.curselection()):
        list_file.delete(index)


# 저장 경로(폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':  # 사용자가 취소를 눌렀을 때
        return

    # print(folder_selected)
    txt_dest_path.delete(0, END)  # 기존에 값이 있었다면 기존 값을 삭제하기 위한 구문
    txt_dest_path.insert(0, folder_selected)


# 시작
def start():
    # 각 옵션들 값을 확인
    print("가로넓이 : ", cmb_width.get())
    print("간격 : ", cmb_space.get())
    print("포멧 : ", cmb_format.get())

    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return

    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")
        return


# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file =Button(file_frame, padx=5, pady=5, width=12, text="파일 추가", command=add_file )
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택 삭제", command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

# height=15 한번에 15개 목록 확인 가능
# yscollcommand=scrollbar.set 을 해줘야 연동이 가능함(스크롤바를 리스트박스와 맵핑)
list_file = Listbox(list_frame, selectmod="extended", height=15, yscrollcommand=scrollbar.set)

list_file.pack(side="left", fill="both", expand=True)   # fill="both" : 위/아래, 좌/우로 펼침
scrollbar.config(command=list_file.yview)  # yview로 scrollbar 맵핑 시키기(리스트박스를 스크롤바와 맵핑)

# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)  # 만약 text 위젯이었으면, "1.0" END 로 설정해야 함
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)
# fill="x" : 좌/우 로 펼침(fill="y" : 상/하로 펼침)
# ipady=4 : (inner padding) ->높이 변경(박스 안쪽을 넓히는 효과)

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1.가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

# 가로 넓이 콤보
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2.간격 옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# 간격 옵션 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 3.파일 포멧 옵션
# 파일 포멧 옵션 레이블
lbl_format = Label(frame_option, text="포멧", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

# 파일 포멧 옵션 콤보
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=8)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# 진행 상황 progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(False, False)
root.mainloop()