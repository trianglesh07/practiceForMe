#학업 계획&진행 여부 기록 프로그램 만들기
import tkinter

tk = tkinter

win = tk.Tk()
win.title('엘든컴')
win.geometry("600x840+0+0")
win.resizable(1,1)  #크기 조절 가능

logo = tk.Label(win, text='스케줄 매니저\n엘든컴', anchor='center', fg='black', font=('SimSun-ExtB',12,"bold"))
logo.place(relx=0.5, rely=0, anchor='n')

win.mainloop()