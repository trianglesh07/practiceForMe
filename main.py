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
    dLWhat.place(relx=0.5, rely=0.85, relwidth=0.6, anchor="center")

    def mon_rad():
        global dlMonth
        dlMonth = month.get()

    def nal_rad():
        global dlNal
        dlNal = nal.get()

    month = tk.IntVar()
    dLDateBtn1 = tk.Radiobutton(dL, text="1월", variable=month, value=1, command=mon_rad)
    dLDateBtn1.place(relx=0.1, rely=0.55, anchor="center")
    dLDateBtn2 = tk.Radiobutton(dL, text="2월", variable=month, value=2, command=mon_rad)
    dLDateBtn2.place(relx=0.25, rely=0.55, anchor="center")
    dLDateBtn3 = tk.Radiobutton(dL, text="3월", variable=month, value=3, command=mon_rad)
    dLDateBtn3.place(relx=0.4, rely=0.55, anchor="center")
    dLDateBtn4 = tk.Radiobutton(dL, text="4월", variable=month, value=4, command=mon_rad)
    dLDateBtn4.place(relx=0.55, rely=0.55, anchor="center")
    dLDateBtn5 = tk.Radiobutton(dL, text="5월", variable=month, value=5, command=mon_rad)
    dLDateBtn5.place(relx=0.7, rely=0.55, anchor="center")
    dLDateBtn6 = tk.Radiobutton(dL, text="6월", variable=month, value=6, command=mon_rad)
    dLDateBtn6.place(relx=0.85, rely=0.55, anchor="center")
    dLDateBtn7 = tk.Radiobutton(dL, text="7월", variable=month, value=7, command=mon_rad)
    dLDateBtn7.place(relx=0.1, rely=0.6, anchor="center")
    dLDateBtn8 = tk.Radiobutton(dL, text="8월", variable=month, value=8, command=mon_rad)
    dLDateBtn8.place(relx=0.25, rely=0.6, anchor="center")
    dLDateBtn9 = tk.Radiobutton(dL, text="9월", variable=month, value=9, command=mon_rad)
    dLDateBtn9.place(relx=0.4, rely=0.6, anchor="center")
    dLDateBtn10 = tk.Radiobutton(dL, text="10월", variable=month, value=10, command=mon_rad)
    dLDateBtn10.place(relx=0.55, rely=0.60, anchor="center")
    dLDateBtn11 = tk.Radiobutton(dL, text="11월", variable=month, value=11, command=mon_rad)
    dLDateBtn11.place(relx=0.7, rely=0.60, anchor="center")
    dLDateBtn12 = tk.Radiobutton(dL, text="12월", variable=month, value=12, command=mon_rad)
    dLDateBtn12.place(relx=0.85, rely=0.60, anchor="center")

    nal = tk.IntVar()
    dLDateBtn1 = tk.Radiobutton(dL, text="1일", variable=nal, value=1, command=nal_rad)
    dLDateBtn1.place(relx=0.1, rely=0.65, anchor="center")
    dLDateBtn2 = tk.Radiobutton(dL, text="2일", variable=nal, value=2, command=nal_rad)
    dLDateBtn2.place(relx=0.25, rely=0.65, anchor="center")
    dLDateBtn3 = tk.Radiobutton(dL, text="3일", variable=nal, value=3, command=nal_rad)
    dLDateBtn3.place(relx=0.4, rely=0.65, anchor="center")
    dLDateBtn4 = tk.Radiobutton(dL, text="4일", variable=nal, value=4, command=nal_rad)
    dLDateBtn4.place(relx=0.55, rely=0.65, anchor="center")
    dLDateBtn5 = tk.Radiobutton(dL, text="5일", variable=nal, value=5, command=nal_rad)
    dLDateBtn5.place(relx=0.7, rely=0.65, anchor="center")
    dLDateBtn6 = tk.Radiobutton(dL, text="6일", variable=nal, value=6, command=nal_rad)
    dLDateBtn6.place(relx=0.85, rely=0.65, anchor="center")
    dLDateBtn7 = tk.Radiobutton(dL, text="7일", variable=nal, value=7, command=nal_rad)
    dLDateBtn7.place(relx=0.1, rely=0.7, anchor="center")
    dLDateBtn8 = tk.Radiobutton(dL, text="8일", variable=nal, value=8, command=nal_rad)
    dLDateBtn8.place(relx=0.25, rely=0.7, anchor="center")
    dLDateBtn9 = tk.Radiobutton(dL, text="9일", variable=nal, value=9, command=nal_rad)
    dLDateBtn9.place(relx=0.4, rely=0.7, anchor="center")
    dLDateBtn10 = tk.Radiobutton(dL, text="10일", variable=nal, value=10, command=nal_rad)
    dLDateBtn10.place(relx=0.55, rely=0.7, anchor="center")
    dLDateBtn11 = tk.Radiobutton(dL, text="11일", variable=nal, value=11, command=nal_rad)
    dLDateBtn11.place(relx=0.7, rely=0.7, anchor="center")
    dLDateBtn12 = tk.Radiobutton(dL, text="12일", variable=nal, value=12, command=nal_rad)
    dLDateBtn12.place(relx=0.85, rely=0.7, anchor="center")
    dLDateBtn13 = tk.Radiobutton(dL, text="13일", variable=nal, value=13, command=nal_rad)
    dLDateBtn13.place(relx=0.1, rely=0.75, anchor="center")
    dLDateBtn14 = tk.Radiobutton(dL, text="14일", variable=nal, value=14, command=nal_rad)
    dLDateBtn14.place(relx=0.25, rely=0.75, anchor="center")
    dLDateBtn15 = tk.Radiobutton(dL, text="15일", variable=nal, value=15, command=nal_rad)
    dLDateBtn15.place(relx=0.4, rely=0.75, anchor="center")
    dLDateBtn16 = tk.Radiobutton(dL, text="16일", variable=nal, value=16, command=nal_rad)
    dLDateBtn16.place(relx=0.55, rely=0.75, anchor="center")
    dLDateBtn17 = tk.Radiobutton(dL, text="17일", variable=nal, value=17, command=nal_rad)
    dLDateBtn17.place(relx=0.7, rely=0.75, anchor="center")
    dLDateBtn18 = tk.Radiobutton(dL, text="18일", variable=nal, value=18, command=nal_rad)
    dLDateBtn18.place(relx=0.85, rely=0.75, anchor="center")
    dLDateBtn19 = tk.Radiobutton(dL, text="19일", variable=nal, value=19, command=nal_rad)
    dLDateBtn19.place(relx=0.1, rely=0.8, anchor="center")

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