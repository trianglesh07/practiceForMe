#학업 계획&진행 여부 기록 프로그램 만들기

#함수 호출
import tkinter

tk = tkinter

#창 설정
win = tk.Tk()
win.title('엘든컴')
win.geometry("600x840+0+0")
win.resizable(1,1)  #크기 조절 가능

#로고
logo = tk.Label(win, text='스케줄 매니저\n엘든컴', anchor='center', fg='black', font=('SimSun-ExtB',30,"bold"))
logo.place(relx=0.5, rely=0, anchor='n')


#달력 호출 버튼
#달력 만들기
cal = tk.Frame(win, width=560, height=500, bg="#D3D3D3")
for a in range(7):
    for b in range(5):
        date=(a+7*b+1)
        if date <= 31:
            cell = tk.Label(cal, text=str(date), borderwidth=1)
            cell.place(relx=0.14*a, rely=0.2*b, anchor="nw", relwidth=(1/6), relheight=0.2)
        else:
            cell = tk.Label(cal, text="Elden Ring\nis badass", borderwidth=1)
            cell.place(relx=0.14 * a, rely=0.2 * b, anchor="nw", relwidth=(1 / 6), relheight=0.2)
def CalBtn():
    cal.place(relx=0.5, rely=0.9, anchor="s", relwidth=0.9, relheight=0.65)

calBtn = tk.Button(win, text='달력', command=CalBtn, font=('SimSun-ExtB',15,"bold"), relief="groove")
calBtn.place(relx=0.05, rely=0.2, anchor='w', relwidth=0.2, relheight=0.1)

#할일 목록 호출 버튼
def DoList():
    pass

dlBtn = tk.Button(win, text='해야 할 일', command=DoList, font=('SimSun-ExtB',15,"bold"), relief="groove")
dlBtn.place(relx=0.3, rely=0.2, anchor='w', relwidth=0.2, relheight=0.1)

#타이머 호출 버튼
def Timer():
    pass

tmBtn = tk.Button(win, text='타이머', command=Timer, font=('SimSun-ExtB',15,"bold"), relief="groove")
tmBtn.place(relx=0.55, rely=0.2, anchor='w', relwidth=0.2, relheight=0.1)

win.mainloop()