import tkinter as tk
import random

def lotto():
    l=list(range(1, 46))
    random.shuffle(l)
    lbl.configure(text=l[:6])

root = tk.Tk()
root.geometry("200x100")

lbl=tk.Label(text='')
btn=tk.Button(text='로또번호', command=lotto)

lbl.pack()
btn.pack()
tk.mainloop()
