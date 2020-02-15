import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def disp_img(path):
    newImage = PIL.Image.open(path)

    ImageData = PIL.ImageTk.PhotoImage(newImage)
    lbl_img.configure(image=ImageData)
    lbl_img.image = ImageData


def op():
    fpath = fd.askopenfilename()

    if fpath:
        disp_img(fpath)

#윈도우 창 생성
root = tk.Tk()
root.geometry('400x350')

#버튼과 레이블 생성
btn = tk.Button(text="파일 열기", command=op)
lbl_img = tk.Label()

#컨트롤 화면에 배치
btn.pack()
lbl_img.pack()

# 화면유지
tk.mainloop()