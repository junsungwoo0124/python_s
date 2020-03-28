import tkinter as tk
import random as r
q_nam = r.randint(1,100)

root = tk.Tk()
root.geometry("300x200")
#숫자 판독하기
def check_num(num):
   global q_nam
   if num == q_nam:
      msg = "정답"
      txt.configure(state='readonly')
   elif num>q_nam:
      msg = "더 작은 수를 넣어봐"
   else:
      msg = "더 큰 수를 넣어봐"
   return msg

def disp_msg():
   num = int(inum.get())
   msg = check_num(num)
   lbl.configure(text=msg)

#화면 객체 생성
inum = tk.StringVar()
lbl = tk.Label()
txt = tk.Entry(textvariable=inum)
btn = tk.Button(text="시도(정말로 시도하시겠습니까 다시한번, 아니두번, 아니 천번만 생각해보세요)", command = disp_msg)

lbl.pack()
txt.pack()
btn.pack()

tk.mainloop()