import tkinter as tk
import random as r

root = tk.Tk()
root.geometry("200x100")

def dispLabel():
    if int(usr_ans.get()) == ans:
        lbl_judge.configure(text="정답")
    else:
        lbl_judge.configure(text="오답")

#문제 출제 함수
def make_quiz():
    num1 = r.randint(0,100)
    num2 = r.randint(0,100)
    quiz = "%d + %d" % (num1, num2)
    return quiz
usr_ans = tk.StringVar()

# 윈도우 배치 컨트롤 선언
quiz = make_quiz()
ans = eval(quiz)
lbl_quiz = tk.Label(text="%s ="% quiz)
txt = tk.Entry(textvariable=usr_ans)
btn = tk.Button(text="계산", command=dispLabel)
lbl_judge = tk.Label(text="")

lbl_quiz.pack()
txt.pack()
btn.pack()
lbl_judge.pack()
tk.mainloop()





