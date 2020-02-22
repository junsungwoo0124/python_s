import tkinter as tk

root = tk.Tk()
root.geometry("200x100")

wbt = tk.StringVar()
dbt = tk.StringVar()

def displabel():
    cal_wbt = int(txt_wbt.get())
    cal_dbt = int(txt_dbt.get())
    dfi = (cal_wbt + cal_dbt)*0.72+40.6
    lbl.configure(text = "불쾌지수도는  %.2f 입니다" %dfi)

#윈도우 컨트롤 생성
lbl = tk.Label(text = "")
txt_wbt = tk.Entry(textvariable = wbt)
txt_dbt = tk.Entry(textvariable = dbt)
btn = tk.Button(text="PUSH", command=displabel)

#윈도우에 컨트롤 배치
lbl.pack()
btn.pack()
txt_wbt.pack()
txt_dbt.pack()
tk.mainloop()

