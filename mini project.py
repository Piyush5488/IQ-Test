# Mini Project
import tkinter
from tkinter import *
import time

def close():
    leaderboard_screen.destroy()

def goback():
    leaderboard_screen.destroy()
    results_screen.destroy()
    main_page()

def leaderboard():
    global leaderboard_screen
    leaderboard_screen = Tk()
    leaderboard_screen.geometry="500x500"
    leaderboard_screen.resizable(False,False)
    leaderboard_screen.title("Leaderboards")

    k = open("results.txt", "r")
    x = k.readlines()
    h = []
    for i in x:
        stats = i.split()
        if(len(stats)>4):
            for j in range(len(stats)-4):
                stats[0]=stats[0]+" "+stats[1]
                stats.pop(1)
        h.append(stats)

    Label(leaderboard_screen, text="Leaderboards", font="10", bg="black", fg="white", width="25", height="3").grid(column=1, row=0)
    Label(leaderboard_screen, text="").grid()
    #Label(leaderboard_screen, text="Username                 Entry Number                  Score", font=("arial 15 bold"), padx="30").grid()
    Label(leaderboard_screen, text="Name", font=("arial 15 bold"), padx="30").grid(column=0, row=1)
    Label(leaderboard_screen, text="Entry Number", font=("arial 15 bold"), padx="30").grid(column=1,row=1)
    Label(leaderboard_screen, text="Score", font=("arial 15 bold"), padx="30").grid(column=2,row=1)
    Label(leaderboard_screen, text="").grid()


    score=[]
    for i in range(len(h)):
        if(len(h[i])==0):
            h.pop(i)
            continue
        score.append(int(h[i][2]))

    stats = []
    rownum=2
    for i in range(len(h)):
        x = score.index(max(score))
        stats = h[x]
        score.pop(x)
        h.pop(x)
        USERNAME = stats[0]
        ENTRY_NUM = stats[1]
        SCORE = stats[2]
        Label(leaderboard_screen, text=USERNAME, font=("arial 11")).grid(column=0,row=rownum)
        Label(leaderboard_screen, text=ENTRY_NUM, font=("arial 11")).grid(column=1,row=rownum)
        Label(leaderboard_screen, text=SCORE, font=("arial 11")).grid(column=2,row=rownum)
        rownum = rownum + 1

    Label(leaderboard_screen, text="").grid()
    Button(leaderboard_screen, text="Close", font=("Algerian 10"),bg="grey", fg="white", command=close).grid(column=1,row=rownum+2)
    Button(leaderboard_screen, text="Home Page", font=("Algerian 10"), bg="grey", fg="white", command=goback).grid(column=2, row=rownum + 2)


def showresults():
    global results_screen
    ques10_screen.destroy()
    results_screen = Tk()
    results_screen.geometry="200x200"
    results_screen.resizable(False, False)
    results_screen.title("RESULTS")

    Label(results_screen, text="YOUR RESULTS", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(results_screen,text="").pack()
    Label(results_screen, text="You have got", font=5).pack()
    Label(results_screen, text=NUM_RIGHT_ANS+" CORRECT ANSWERS", fg="green", font=10).pack()
    x=10-int(NUM_RIGHT_ANS)
    x = str(x)
    Label(results_screen, text=x + " INCORRECT ANSWERS", fg="red", font=10).pack()
    Label(results_screen, text="").pack()
    Label(results_screen, text="YOUR SCORE IS "+total_ans+"/1400", font=("arial 20 italic"), bg="yellow").pack()
    Label(results_screen, text="").pack()
    Button(results_screen, text="Leaderboards", font=("arial 10 italic"), bg="black", fg="white", padx="25", command=leaderboard).pack(anchor=E)
    Label(results_screen, text="").pack()


def store_stats():
    global total_ans
    total_ans=maxcount+maxcount1+maxcount2+maxcount3+maxcount4+maxcount5+maxcount6+maxcount7+maxcount8+maxcount9
    total_ans = str(total_ans)

    global NUM_RIGHT_ANS
    NUM_RIGHT_ANS = anscount1+anscount2+anscount3+anscount4+anscount5+anscount6+anscount7+anscount8+anscount9+anscount10
    NUM_RIGHT_ANS = str(NUM_RIGHT_ANS)

    f = open("results.txt", "a")
    f.write(UserName+"  ")
    f.write(EntryNum+"  ")
    f.write(total_ans+"  ")
    f.write(NUM_RIGHT_ANS)
    f.write("\n")

    showresults()




def first_assign():
    global maxcount
    maxcount = IntVar()
    maxcount = M[-1]


    global anscount1
    anscount1 = IntVar()
    if(maxcount>10):
        anscount1 = 1
    else:
        anscount1 = 0
    ques2()


def second_assign():
    global maxcount1
    maxcount1 = IntVar()
    maxcount1 = M[-1]


    global anscount2
    anscount2 = IntVar()
    if (maxcount1 > 10):
        anscount2 = 1
    else:
        anscount2 = 0
    ques3()


def third_assign():
    global maxcount2
    maxcount2 = IntVar()
    maxcount2 = M[-1]


    global anscount3
    anscount3 = IntVar()
    if (maxcount2 > 10):
        anscount3 = 1
    else:
        anscount3 = 0
    ques4()


def fourth_assign():
    global maxcount3
    maxcount3 = IntVar()
    maxcount3 = M[-1]


    global anscount4
    anscount4 = IntVar()
    if (maxcount3 > 10):
        anscount4 = 1
    else:
        anscount4 = 0
    ques5()


def fifth_assign():
    global maxcount4
    maxcount4 = IntVar()
    maxcount4 = M[-1]


    global anscount5
    anscount5 = IntVar()
    if (maxcount4 > 10):
        anscount5 = 1
    else:
        anscount5 = 0
    ques6()


def sixth_assign():
    global maxcount5
    maxcount5 = IntVar()
    maxcount5 = M[-1]


    global anscount6
    anscount6 = IntVar()
    if (maxcount5 > 10):
        anscount6 = 1
    else:
        anscount6 = 0
    ques7()


def seventh_assign():
    global maxcount6
    maxcount6 = IntVar()
    maxcount6 = M[-1]


    global anscount7
    anscount7 = IntVar()
    if (maxcount6 > 10):
        anscount7 = 1
    else:
        anscount7 = 0
    ques8()


def eighth_assign():
    global maxcount7
    maxcount7 = IntVar()
    maxcount7 = M[-1]


    global anscount8
    anscount8 = IntVar()
    if (maxcount7 > 10):
        anscount8 = 1
    else:
        anscount8 = 0
    ques9()


def ninth_assign():
    global maxcount8
    maxcount8 = IntVar()
    maxcount8 = M[-1]


    global anscount9
    anscount9 = IntVar()
    if (maxcount8 > 10):
        anscount9 = 1
    else:
        anscount9 = 0
    ques10()


def tenth_assign():
    global maxcount9
    maxcount9 = IntVar()
    maxcount9 = M[-1]


    global anscount10
    anscount10 = IntVar()
    if (maxcount9 > 10):
        anscount10 = 1
    else:
        anscount10 = 0
    store_stats()


def ques1():
    global ques1_screen
    detailscreen.destroy()
    ques1_screen=Tk()
    ques1_screen.geometry("500x500")
    ques1_screen.title("QUESTION-1")
    ques1_screen.resizable(False,False)


    global v
    v = IntVar()
    global M
    M=[]
    
    Label(ques1_screen, text="QUESTION-1", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(ques1_screen, text="").pack()
    Label(ques1_screen, text="Replace ? by suitable options \n"
                              " BF, CH, ?, HO, LT", font="7").pack()
    Label(ques1_screen, text="").pack()
    Radiobutton(ques1_screen, text='DN', value=1, padx="80", font=("arial",15,"italic"), command=lambda : M.append(0)).pack(anchor=W)
    Label(ques1_screen, text="").pack()
    Radiobutton(ques1_screen, text="EL", value=2, padx="80", font=("arial",15,"italic"), command=lambda : M.append(0)).pack(anchor=W)
    Label(ques1_screen, text="").pack()
    Radiobutton(ques1_screen, text="EK", value=3, padx="80", font=("arial",15,"italic"), command=lambda : M.append(100)).pack(anchor=W)
    Label(ques1_screen, text="").pack()
    Radiobutton(ques1_screen, text="EM", value=4, padx="80", font=("arial",15,"italic"), command=lambda : M.append(0)).pack(anchor=W)
    Label(ques1_screen, text="").pack()
    btn = Button(ques1_screen, text="NEXT", font="1", fg="white", bg="black", command=first_assign).pack()
    Label(ques1_screen, text="").pack()


def ques2():
    global ques2_screen
    ques1_screen.destroy()
    ques2_screen=Tk()
    ques2_screen.geometry("500x500")
    ques2_screen.title("QUESTION-2")
    ques2_screen.resizable(False,False)

    global v
    v = IntVar()
    global M
    M = []
    
    Label(ques2_screen, text="QUESTION-2", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(ques2_screen, text="").pack()
    Label(ques2_screen, text=" Replace the ? \n"
                              "15, 15, 30, 10, 40, ?, 48", font="7").pack()
    Label(ques2_screen, text="").pack()
    Radiobutton(ques2_screen, text='8', value=1, padx="80", font=("arial",15,"italic"), command=lambda : M.append(150)).pack(anchor=W)
    Label(ques2_screen, text="").pack()
    Radiobutton(ques2_screen, text='20', value=2, padx="80", font=("arial",15,"italic"), command=lambda : M.append(0)).pack(anchor=W)
    Label(ques2_screen, text="").pack()
    Radiobutton(ques2_screen, text='24', value=3, padx="80", font=("arial",15,"italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques2_screen, text="").pack()
    Radiobutton(ques2_screen, text='40', value=4, padx="80", font=("arial",15,"italic"), command=lambda: M.append(0)).pack(anchor=W)
    Button(ques2_screen, text="NEXT", font="1", fg="white", bg="black", command=second_assign).pack()
    Label(ques2_screen, text="").pack()


def ques3():
    global ques3_screen
    ques2_screen.destroy()
    ques3_screen=Tk()
    ques3_screen.geometry("500x500")
    ques3_screen.title("QUESTION-3")
    ques3_screen.resizable(False,False)
    
    Label(ques3_screen, text="QUESTION-3", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(ques3_screen, text="").pack()
    Label(ques3_screen, text=" Adequate : Enough :: Veracity : ? \n", font="7").pack()
    Label(ques3_screen, text="").pack()
    Radiobutton(ques3_screen, text='Antagonist', value=1, padx="80", font=("arial",15,"italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques3_screen, text="").pack()
    Radiobutton(ques3_screen, text='Animate', value=2, padx="80", font=("arial",15,"italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques3_screen, text="").pack()
    Radiobutton(ques3_screen, text='Little', value=3, padx="80", font=("arial",15,"italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques3_screen, text="").pack()
    Radiobutton(ques3_screen, text='Truth', value=4, padx="80", font=("arial",15,"italic"), command=lambda: M.append(100)).pack(anchor=W)
    Button(ques3_screen, text="NEXT", font="1", fg="white", bg="black", command=third_assign).pack()
    Label(ques3_screen, text="").pack()


def ques4():
    global ques4_screen
    ques3_screen.destroy()
    ques4_screen=Tk()
    ques4_screen.geometry("500x500")
    ques4_screen.title("QUESTION-4")
    ques4_screen.resizable(False,False)
    
    Label(ques4_screen, text="QUESTION-4", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(ques4_screen, text="").pack()
    Label(ques4_screen, text="Statements:  Z>B=S , Y≥B>F , H<S≤Y , Z>S≥T\n"
                             "Conclusions:\n"
                             "1. Y>T\n"
                             "2. Y=T\n", font="7").pack()
    Label(ques4_screen, text="").pack()
    Radiobutton(ques4_screen, text='None of the conclusion follow', value=1, padx="80", font=("arial",15,"italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques4_screen, text="").pack()
    Radiobutton(ques4_screen, text='Only I follow', value=2, padx="80", font=("arial",15,"italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques4_screen, text="").pack()
    Radiobutton(ques4_screen, text='Only II follow', value=3, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques4_screen, text="").pack()
    Radiobutton(ques4_screen, text='Either I or II follow', value=4, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(200)).pack(anchor=W)
    Button(ques4_screen, text="NEXT", font="1", fg="white", bg="black", command=fourth_assign).pack()
    Label(ques4_screen, text="").pack()


def ques5():
    global ques5_screen
    ques4_screen.destroy()
    ques5_screen=Tk()
    ques5_screen.geometry("500x500")
    ques5_screen.title("QUESTION-5")
    ques5_screen.resizable(False,False)
    
    Label(ques5_screen, text="QUESTION-5", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(ques5_screen, text="").pack()
    Label(ques5_screen, text="Complete the given sequence \n 7, 23, 55, 109, __", font="7").pack()
    Label(ques5_screen, text="").pack()
    Radiobutton(ques5_screen, text='193', value=1, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques5_screen, text="").pack()
    Radiobutton(ques5_screen, text='191', value=2, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(100)).pack(anchor=W)
    Label(ques5_screen, text="").pack()
    Radiobutton(ques5_screen, text='190', value=3, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques5_screen, text="").pack()
    Radiobutton(ques5_screen, text='192', value=4, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(0)).pack(anchor=W)
    Button(ques5_screen, text="NEXT", font="1", fg="white", bg="black", command=fifth_assign).pack()
    Label(ques5_screen, text="").pack()

    

def ques6():
    global ques6_screen
    ques5_screen.destroy()
    ques6_screen=Tk()
    ques6_screen.geometry("500x500")
    ques6_screen.title("QUESTION-6")
    ques6_screen.resizable(False,False)
    
    Label(ques6_screen, text="QUESTION-6", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(ques6_screen, text="").pack()
    Label(ques6_screen, text="Pointing to a photograph, a lady tells Pramod "
                             '"I am the\nonly daughter of this lady and her son is your maternal\nuncle".'
                             "How is the speaker related to pramod's father? \n", font="7").pack()
    Label(ques6_screen, text="").pack()
    Radiobutton(ques6_screen, text='Sister-in-law', value=1, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques6_screen, text="").pack()
    Radiobutton(ques6_screen, text='Wife', value=2, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(150)).pack(anchor=W)
    Label(ques6_screen, text="").pack()
    Radiobutton(ques6_screen, text='Neice', value=3, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques6_screen, text="").pack()
    Radiobutton(ques6_screen, text='None', value=4, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques6_screen, text="").pack()
    Button(ques6_screen, text="NEXT", font="1", fg="white", bg="black", command=sixth_assign).pack()
    Label(ques6_screen, text="").pack()

def ques7():
    global ques7_screen
    ques6_screen.destroy()
    ques7_screen=Tk()
    ques7_screen.geometry("500x500")
    ques7_screen.title("QUESTION-7")
    ques7_screen.resizable(False,False)
    
    Label(ques7_screen, text="QUESTION-7", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(ques7_screen, text="").pack()
    Label(ques7_screen, text="Find the missing term in the series \n"
                             "1,5,19,?,211,665", font="7").pack()
    Label(ques7_screen, text="").pack()
    Radiobutton(ques7_screen, text='102', value=1, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques7_screen, text="").pack()
    Radiobutton(ques7_screen, text='197', value=2, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques7_screen, text="").pack()
    Radiobutton(ques7_screen, text='113', value=3, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques7_screen, text="").pack()
    Radiobutton(ques7_screen, text='65', value=4, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(200)).pack(anchor=W)
    Label(ques7_screen, text="").pack()
    Button(ques7_screen, text="NEXT", font="1", fg="white",bg="black", command=seventh_assign).pack()
    Label(ques7_screen, text="").pack()

def ques8():
    global ques8_screen
    ques7_screen.destroy()
    ques8_screen=Tk()
    ques8_screen.geometry("500x500")
    ques8_screen.title("QUESTION-8")
    ques8_screen.resizable(False,False)
    
    Label(ques8_screen, text="QUESTION-8", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(ques8_screen, text="").pack()
    Label(ques8_screen, text="Find the missing term in the series \n"
                             "18,36,54,72,?,108", font="7").pack()
    Label(ques8_screen, text="").pack()
    Radiobutton(ques8_screen, text='90', value=1, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(50)).pack(anchor=W)
    Label(ques8_screen, text="").pack()
    Radiobutton(ques8_screen, text='84', value=2, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques8_screen, text="").pack()
    Radiobutton(ques8_screen, text='91', value=3, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques8_screen, text="").pack()
    Radiobutton(ques8_screen, text='97', value=4, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques8_screen, text="").pack()
    Button(ques8_screen, text="NEXT", font="1", fg="white",bg="black", command=eighth_assign).pack()
    Label(ques8_screen, text="").pack()


def ques9():
    global ques9_screen
    ques8_screen.destroy()
    ques9_screen=Tk()
    ques9_screen.geometry("500x500")
    ques9_screen.title("QUESTION-9")
    ques9_screen.resizable(False,False)
    
    Label(ques9_screen, text="QUESTION-9", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(ques9_screen, text="").pack()
    Label(ques9_screen, text="Find the missing term in the series \n"
                             "0,?,26,255,3124,", font="7").pack()
    Label(ques9_screen, text="").pack()
    Radiobutton(ques9_screen, text='3', value=1, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(200)).pack(anchor=W)
    Label(ques9_screen, text="").pack()
    Radiobutton(ques9_screen, text='17', value=2, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques9_screen, text="").pack()
    Radiobutton(ques9_screen, text='22', value=3, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques9_screen, text="").pack()
    Radiobutton(ques9_screen, text='9', value=4, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques9_screen, text="").pack()
    Button(ques9_screen, text="NEXT", font="1", fg="white",bg="black", command=ninth_assign).pack()
    Label(ques9_screen, text="").pack()

def ques10():
    global ques10_screen
    ques9_screen.destroy()
    ques10_screen=Tk()
    ques10_screen.geometry("500x500")
    ques10_screen.title("QUESTION-10")
    ques10_screen.resizable(False,False)
    
    Label(ques10_screen, text="QUESTION-10", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(ques10_screen, text="").pack()
    Label(ques10_screen, text=" If PIYUSH is ZYIKCX\n"
                              "THEN WHAT IS SAKTH LAUNDE", font="7").pack()
    Label(ques10_screen, text="").pack()
    Radiobutton(ques10_screen, text='CQUIR VQEDNU', value=1, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(250)).pack(anchor=W)
    Label(ques10_screen, text="").pack()
    Radiobutton(ques10_screen, text='CQTJX VQISTR', value=2, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques10_screen, text="").pack()
    Radiobutton(ques10_screen, text='CWUMS JWYUAR', value=3, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques10_screen, text="").pack()
    Radiobutton(ques10_screen, text='CWGIO JWLAUR', value=4, padx="80", font=("arial", 15, "italic"), command=lambda: M.append(0)).pack(anchor=W)
    Label(ques10_screen, text="").pack()
    Button(ques10_screen, text="SUBMIT", font="1", fg="white", bg="black", command=tenth_assign).pack()
    Label(ques10_screen, text="").pack()


def details():
    global detailscreen
    loginscreen.destroy()
    detailscreen=Tk()
    detailscreen.geometry="500x500"
    detailscreen.title("RULES")
    detailscreen.resizable(False,False)

    Label(detailscreen, text="RULES", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(detailscreen, text="").pack()
    Label(detailscreen, text="Now you will be solving 10 Questions \n "
                             "in the TIME-SPAN of 10 minutes \n", font="7").pack()
    Label(detailscreen, text="").pack()
    Label(detailscreen, text="*Each Question is compulsory\n\n"
                             "*If you move on the next question you can not come back", fg="red").pack()
    Label(detailscreen, text="").pack()
    Label(detailscreen, text="ALL THE BEST!!", font="7", fg="blue").pack()
    Label(detailscreen, text="").pack()
    Button(detailscreen, text="BEGIN ==>", font="1", fg="white", bg="black", command=ques1).pack()
    Label(detailscreen, text="").pack()
    

def check_validity_entrynum():

    global EntryNum
    EntryNum = entrynum.get()

    if(entrynum.get() == ""):
        loginscreen.destroy()
        login_page()
    else:
        details()


def check_validity_username():

    global UserName
    UserName = username.get()

    if(UserName == ""):
        loginscreen.destroy()
        login_page()
    else:
        check_validity_entrynum()

def mainpage_to_loginpage():
    mainscreen.destroy()
    login_page()

def login_page():

    global loginscreen
    loginscreen = Tk()
    loginscreen.geometry="500x500"
    loginscreen.title("Login")
    loginscreen.resizable(False,False)

    global username
    global entrynum
    username = StringVar()
    entrynum = StringVar()

    Label(loginscreen, text="LOGIN", font="10", bg="black", fg="white", width="40", height="3").pack()

    Label(loginscreen, text="").pack()
    Label(loginscreen, text="Name", font="7").pack()
    Entry(loginscreen, font="2", textvariable=username, width=26).pack()
    Label(loginscreen, text="").pack()
    Label(loginscreen, text="Entry Number",font="7").pack()
    Entry(loginscreen, font="2", textvariable=entrynum, width=26).pack()
    Label(loginscreen, text="").pack()

    Button(loginscreen, text="NEXT!!!", font="5", bg="grey", fg="black", command=check_validity_username).pack()
    Label(loginscreen, text="").pack()

def main_page():
    global mainscreen
    mainscreen = Tk()
    mainscreen.geometry="500x500"
    mainscreen.title("IQ TEST")
    mainscreen.resizable(False,False)

    Label(mainscreen, text="Welcome To The IQ TEST", font="1", bg="black", fg="white", width="50", height="3").pack()

    Label(mainscreen, text="").pack()
    Label(mainscreen, text="THIS IS AN IQ TEST WHICH CONSISTS OF 10 QUESTIONS",
          font="3").pack()

    Label(mainscreen, text="").pack()
    Label(mainscreen, text="").pack()
    Button(mainscreen, text="START!", font="5", bg="grey", fg="black", command=mainpage_to_loginpage).pack()
    Label(mainscreen, text="").pack()
    mainscreen.mainloop()


main_page()