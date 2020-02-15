import tkinter as tk
import random

def dis_label():
    fortune=['행복','매우행복','많이행복','조금행복']
    lbl.configure(text=random.choice(fortune))
# 200x100 픽셀 창 만들기
root = tk.Tk()
root.geometry("200x100")

#레이블과 버튼 컬트롤 생성하기
lbl=tk.Label(text='')
btn = tk.Button(text="오늘의 운세", command=dis_label)

#레이블 버튼 화면에 배치하기
lbl.pack()
btn.pack()
tk.mainloop()