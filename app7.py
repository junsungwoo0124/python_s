import tkinter as tk

root = tk.Tk()
root.geometry("200x100")


height = tk.StringVar()
weight = tk.StringVar()


def displabel():
    cal_height = int(txt_height.get())
    cal_weight = int(txt_weight.get())
    BMI = cal_weight / (cal_height/100*cal_height/100)
    if BMI <= 18.5:
        msg = "저체중"
    elif BMI <=23:
        msg = "정상"
    elif BMI <=25:
        msg = "과체중"
    else:
        msg = "비만"
    lbl.configure(text = "BMI 지수 = %.2f, 당신은 %s 입니다" %(BMI, msg))



#윈도우 컨트롤 생성
lbl = tk.Label(text="")
txt_height = tk.Entry(textvariable=height)
txt_weight = tk.Entry(textvariable=weight)
btn = tk. Button(text="PUSH", command=displabel)

#윈도우에 컨트롤 배치
lbl.pack()
btn.pack()
txt_height.pack()
txt_weight.pack()
tk.mainloop()
