#이름과 나이를 묻고 답하기
#app5.py

import tkinter as tk

#출력 함수 선언
def dispLabel():
    cal_age = int(txt_age.get())
    lbl.configure(text="hello, %s next year, your age is %d"%(txt_name.get(),cal_age + 1))

#윈도우 생성
root = tk.Tk()
root.geometry("200x100")

#텍스트 상자 값 저장 변수 선언
name = tk.StringVar()
age = tk.StringVar()

#윈도우 컨트롤 생성
lbl = tk.Label(text="")
txt_name = tk.Entry(textvariable=name)
txt_age = tk.Entry(textvariable=age)
btn = tk. Button(text="PUSH", command=dispLabel)

#윈도우에 컨트롤 배치
lbl.pack()
btn.pack()
txt_name.pack()
txt_age.pack()
tk.mainloop()