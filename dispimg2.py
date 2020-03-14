import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    newImage = PIL.Image.open(path).resize( (300,300))
    gImage = PIL.Image.open(path).convert("L").resize( (250, 250) )
    mImage = PIL.Image.open(path).convert("L").resize( (20, 20) ).resize( (300, 300) )

    #이미지 레이블에 출력하기
    ImageData = PIL.ImageTk.PhotoImage(mImage)
    imageLabel.configure(image=ImageData)
    imageLabel.image = ImageData
    jLable.configure(text=path)

def openFile():
    fpath = fd.askopenfilename()

    if fpath:
        dispPhoto(fpath)


#윈도우 창 생성
root = tk.Tk()
root.geometry('400x350')

#버튼과 레이블 생성
btn = tk.Button(text="파일 열기", command=openFile)
imageLabel = tk.Label()
jLable = tk.Label()
#컨트롤 화면에 배치
btn.pack()
imageLabel.pack()
jLable.pack()

# 화면유지
tk.mainloop()
