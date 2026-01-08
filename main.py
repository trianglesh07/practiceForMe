#학업 계획&진행 여부 기록 프로그램 만들기

#함수 호출
import tkinter
import tkinter.ttk
from tkinter import simpledialog

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

#할일 작성 창 띄우기
dateSche = None

def whatYouWillDo(n1, n2):
    global doList
    scheDo = tk.simpledialog.askstring("할 일", "어떤 계획이 있으신가요?")
    sche = (f"{n1} {n2} {scheDo}")
    doList.append(sche) #할일 목록으로 이동시켜야 함

#달력 만들기
cal = tkinter.ttk.Notebook(win, width=560, height=500)

cal1 = None
cal2 = None
cal1 = None
cal2 = None
cal3 = None
cal4 = None
cal5 = None
cal6 = None
cal7 = None
cal8 = None
cal9 = None
cal10 = None
cal11 = None
cal12 = None

monthList = {1: cal1, 2: cal2, 3: cal3, 4: cal4, 5: cal5, 6: cal6, 7: cal7, 8: cal8, 9: cal9, 10: cal10, 11: cal11, 12: cal12}

for i in range(1,13):
    monthList[i] = tk.Frame(cal, bg="#D3D3D3")
    date = 0
    for a in range(5):
        for b in range(7):
            date += 1
            if date <= 31:
                cell = tk.Label(monthList[i], text=str(date), borderwidth=1)
                cell.place(rely=0.2*a, relx=0.14*b, anchor="nw", relwidth=(1/6), relheight=0.1)
                writeBtn = tk.Button(monthList[i], borderwidth=1, command=lambda n1=i, n2=date: whatYouWillDo(n1, n2))
                writeBtn.place(rely=0.2*a+0.1, relx=0.14*b, anchor="nw", relwidth=(1/6), relheight=0.1)
            else:
                cell = tk.Label(monthList[i], text="Elden Ring\nis badass", borderwidth=1)
                cell.place(rely=0.2 * a, relx=0.14 * b, anchor="nw", relwidth=(1 / 6), relheight=0.2)
    cal.add(monthList[i], text="%d월"%i)

def CalBtn():
    cal.place(relx=0.5, rely=0.95, anchor="s", relwidth=0.9, relheight=0.65)

calBtn = tk.Button(win, text='달력', command=CalBtn, font=('SimSun-ExtB',15,"bold"), relief="groove")
calBtn.place(relx=0.05, rely=0.2, anchor='w', relwidth=0.2, relheight=0.1)

#할일 목록 호출 버튼
doList=[]
dLtext = "해야 할 일들"

def DolistRe():
    global dLtext
    for i in doList:
        dLtext += (f"\n{i}")

def DoList():
    global dL
    global dLtext
    global dLWhat
    DolistRe()
    dL = tk.Toplevel()
    dL.title("할 일 목록")
    dL.geometry("300x500+0+0")
    doListAppear = tk.Label(dL, text=dLtext)
    doListAppear.pack()

    #목록에 추가하기
    dLWhat = tk.Entry(dL, relief="solid")
    dLWhat.place(relx=0.5, rely=0.7, relwidth=0.6, anchor="center")     #라디오버튼으로 날짜 입력 추가해야 함
    dLplus = tk.Button(dL, text="추가", command=(DoListWhat, DolistRe))
    dLplus.place(relx=0.75, rely=0.9, anchor="center")

    #창 닫기
    dLclose = tk.Button(dL, text="닫기", command=dL.destroy)
    dLclose.place(relx=0.9, rely=0.9, anchor="center")

def DoListWhat():
    global dLWhat
    dLQuestion = dLWhat.get()   #날짜 입력 추가 필요


dlBtn = tk.Button(win, text='해야 할 일', command=DoList, font=('SimSun-ExtB',15,"bold"), relief="groove")
dlBtn.place(relx=0.3, rely=0.2, anchor='w', relwidth=0.2, relheight=0.1)

#타이머 호출 버튼
def Timer():
    pass

tmBtn = tk.Button(win, text='타이머', command=Timer, font=('SimSun-ExtB',15,"bold"), relief="groove")
tmBtn.place(relx=0.55, rely=0.2, anchor='w', relwidth=0.2, relheight=0.1)

win.mainloop()