import tkinter
#呼叫一個視窗
window = tkinter.Tk()
#視窗的大小
window.geometry("300x400+400+200")
#一個標題
lab = tkinter.Label(window,text = "王威騰好帥")
#讓標題停留在界面上
lab.pack()
but = tkinter.Button(window,text = "hello")
but.pack()
#一個死循環,讓視窗持續停留,監聽
tkinter.mainloop()