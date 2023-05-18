from  tkinter import *

root=Tk()
#root.geometry('800x600')
#root.attributes('-fullscreen', True)

is_winner=0

frame1=LabelFrame(root,width=200,bg="#00EE76")

root.config(bg="#00EE76")
liste=[1,2,3,4,5,6,7,8,9]
t1=[]
t2=[]
f1=[1,2,3]
f2=[4,5,6]
f3=[7,8,9]
f4=[1,5,9]
f5=[3,5,7]
f6=[1,4,7]
f7=[2,5,8]
f8=[3,6,9]
pl=1
win=0
    
s=0

def box(a):
    
    
    global pl,is_winner
    global win,winner2,winer,tie
    global s,result
    is_winner=0
    
    s+=1
    if a==1 and win !=1:
        if pl==1:            
            box1=Button(frame1,text="X",padx=47,pady=42,state="disabled",fg="red",font=("Courier",40),bg="#AEEEEE")
            box1.grid(row=0,column=0)
            t1.append(a)
            pl=2
        elif pl ==2:
            box1=Button(frame1,text="O",padx=47,pady=42,state="disabled",fg="blue",font=("Courier", 40),bg="#AEEEEE")
            box1.grid(row=0,column=0)
            t2.append(a)
            pl=1               
    elif a==2 and win !=1:
        if pl==1:         
            box2=Button(frame1,text="X",padx=47,pady=42,state="disabled",fg="red",font=("Courier", 40),bg="#AEEEEE")
            box2.grid(row=0,column=1)
            t1.append(a)
            pl=2
        elif pl ==2:
            box2=Button(frame1,text="O",padx=47,pady=42,state="disabled",fg="blue",font=("Courier", 40),bg="#AEEEEE")
            box2.grid(row=0,column=1)
            t2.append(a)
            pl=1               
    elif a==3 and win !=1:
        if pl==1: 
            box3=Button(frame1,text="X",padx=47,pady=42,state="disabled",fg="red",font=("Courier", 40),bg="#AEEEEE")
            box3.grid(row=0,column=2) 
            t1.append(a)
            pl=2
        elif pl ==2:
            box3=Button(frame1,text="O",padx=47,pady=42,state="disabled",fg="blue",font=("Courier", 40),bg="#AEEEEE")
            box3.grid(row=0,column=2) 
            t2.append(a)
            pl=1
    elif a==4 and win !=1:
        if pl==1: 
            box4=Button(frame1,text="X",padx=47,pady=42,state="disabled",fg="red",font=("Courier", 40),bg="#AEEEEE")
            box4.grid(row=1,column=0)  
            t1.append(a)
            pl=2
        elif pl ==2:
            box4=Button(frame1,text="O",padx=47,pady=42,state="disabled",fg="blue",font=("Courier", 40),bg="#AEEEEE")
            box4.grid(row=1,column=0)  
            t2.append(a)
            pl=1
    elif a==5 and win !=1:
        if pl==1: 
            box5=Button(frame1,text="X",padx=47,pady=42,state="disabled",fg="red",font=("Courier", 40),bg="#AEEEEE")
            box5.grid(row=1,column=1)
            t1.append(a)
            pl=2
        elif pl ==2:
            box5=Button(frame1,text="O",padx=47,pady=42,state="disabled",fg="blue",font=("Courier", 40),bg="#AEEEEE")
            box5.grid(row=1,column=1)
            t2.append(a)
            pl=1
    elif a==6 and win !=1:
        if pl==1: 
            box6=Button(frame1,text="X",padx=47,pady=42,state="disabled",fg="red",font=("Courier", 40),bg="#AEEEEE")
            box6.grid(row=1,column=2)
            t1.append(a)
            pl=2
        elif pl ==2:
            box6=Button(frame1,text="O",padx=47,pady=42,state="disabled",fg="blue",font=("Courier", 40),bg="#AEEEEE")
            box6.grid(row=1,column=2)
            t2.append(a)
            pl=1
    elif a==7 and win !=1:
        if pl==1: 
            box7=Button(frame1,text="X",padx=47,pady=42,state="disabled",fg="red",font=("Courier", 40),bg="#AEEEEE")
            box7.grid(row=2,column=0) 
            t1.append(a)
            pl=2
        elif pl ==2:
            box7=Button(frame1,text="O",padx=47,pady=42,state="disabled",fg="blue",font=("Courier", 40),bg="#AEEEEE")
            box7.grid(row=2,column=0)
            t2.append(a)
            pl=1
    elif a==8 and win !=1:
        if pl==1: 
            box8=Button(frame1,text="X",padx=47,pady=42,state="disabled",fg="red",font=("Courier", 40),bg="#AEEEEE")
            box8.grid(row=2,column=1) 
            t1.append(a)
            pl=2
        elif pl ==2:
            box8=Button(frame1,text="O",padx=47,pady=42,state="disabled",fg="blue",font=("Courier", 40),bg="#AEEEEE")
            box8.grid(row=2,column=1) 
            t2.append(a)
            pl=1
    elif a==9 and win !=1:
        if pl==1:
            box9=Button(frame1,text="X",padx=47,pady=42,state="disabled",fg="red",font=("Courier", 40),bg="#AEEEEE")
            box9.grid(row=2,column=2)
            t1.append(a)
            pl=2
        elif pl ==2:
            box9=Button(frame1,text="O",padx=47,pady=42,state="disabled",fg="blue",font=("Courier", 40),bg="#AEEEEE")
            box9.grid(row=2,column=2)
            t2.append(a)
            pl=1


    
   
    for i in(f1,f2,f3,f4,f5,f6,f7,f8):
        for x in i :
            if x not in t1:
                break
        else:

            print("player1 winner")
            is_winner=1
            win=1
            result=True
            winer=Label(frame5,text="  X  WINNER",fg="red",bg="#00EE76",font=("BLOD",22))
            winer.grid(row=1,column=0,ipadx=0,ipady=0)
            for i in  range (len(t1)):
                t1.pop(0)
                
            for i in  range (len(t2)):
                t2.pop(0)
                           
               
    for i in(f1,f2,f3,f4,f5,f6,f7,f8):
        for x in i :
            if x not in t2:
                break
        else:
            
            print("player2 winner")
            win=1
            result=True
            is_winner=2
            winner2=Label(frame5,text="  O   WINNER",fg="blue",bg="#00EE76",font=("BLOD",22))
            winner2.grid(row=1,column=0,ipadx=0,ipady=0)

            for i in  range (len(t2)):
                t2.pop(0)
                
            for i in  range (len(t1)):
                t1.pop(0)
    if s ==10 and win == 0:
        print("Tie")
        result=True
        tie=Label(frame5,text="  TIE",fg="white",bg="#00EE76",font=("BLOD",22))
        tie.grid(row=1,column=0,ipadx=0,ipady=0)
        for i in  range (len(t2)):
                t2.pop(0) 
        for i in  range (len(t1)):
                t1.pop(0)
    print(result)

     
result=False
def s_play():
    a=0
    global frame4
    global win
    global s,result
    global tie
    global winer
    global winner2
    s=0
    frame4.after(10,frame4.destroy)
    result=False

    win=0
    frame1.grid(row=0,column=0,ipadx=0,ipady=0,padx=0,pady=0)
    frame5.grid(row=1,column=0,ipadx=0,ipady=20,padx=0,pady=0,columnspan=10)

    
   
    r.grid(row=0,column=0,ipadx=202,ipady=10)
    q.grid(row=0,column=1,ipadx=10,ipady=10)
 
    
    box1=Button(frame1,text="-",padx=80,pady=80,fg="#66CDAA",command=lambda :box(1),bg="#66CDAA",activebackground='#C6E2FF')
    box2=Button(frame1,text="-",padx=80,pady=80,fg="#66CDAA",command=lambda :box(2),bg="#66CDAA",activebackground='#C6E2FF')
    box3=Button(frame1,text="-",padx=80,pady=80,fg="#66CDAA",command=lambda :box(3),bg="#66CDAA",activebackground='#C6E2FF')
    box4=Button(frame1,text="-",padx=80,pady=80,fg="#66CDAA",command=lambda :box(4),bg="#66CDAA",activebackground='#C6E2FF')
    box5=Button(frame1,text="-",padx=80,pady=80,fg="#66CDAA",command=lambda :box(5),bg="#66CDAA",activebackground='#C6E2FF')
    box6=Button(frame1,text="-",padx=80,pady=80,fg="#66CDAA",command=lambda :box(6),bg="#66CDAA",activebackground='#C6E2FF')
    box7=Button(frame1,text="-",padx=80,pady=80,fg="#66CDAA",command=lambda :box(7),bg="#66CDAA",activebackground='#C6E2FF')
    box8=Button(frame1,text="-",padx=80,pady=80,fg="#66CDAA",command=lambda :box(8),bg="#66CDAA",activebackground='#C6E2FF')
    box9=Button(frame1,text="-",padx=80,pady=80,fg="#66CDAA",command=lambda :box(9),bg="#66CDAA",activebackground='#C6E2FF')
    box1.grid(row=0,column=0)
    box2.grid(row=0,column=1)
    box3.grid(row=0,column=2)
    box4.grid(row=1,column=0)
    box5.grid(row=1,column=1)
    box6.grid(row=1,column=2)
    box7.grid(row=2,column=0)
    box8.grid(row=2,column=1)
    box9.grid(row=2,column=2)
    box(a)
           
         



    
frame4=Frame(root,padx=10,pady=30, borderwidth = 4,bg="orange")
frame4.grid(row=1,column=0)
frame5=LabelFrame(root,bg="#00EE76")







def restart():
    
   ## x=Label(frame5,text="                                               ",fg="white",bg="#00EE76",font=("BLOD",8))
   ## x.grid(row=1,column=0,ipadx=0,ipady=0)


    for i in  range (len(t2)):
                t2.pop(0) 
    for i in  range (len(t1)):
                t1.pop(0)
    if result==True:
        print(is_winner)
        if is_winner==1:
            winer.destroy()
        elif is_winner==2:
            winner2.destroy()
        elif is_winner==0:
            tie.destroy()
    
    s_play()


def exit():
    root.destroy()


r=Button(frame5,text="Restart",fg="black",font=("Courier", 8),bg="#90EE90",activebackground = 'sky blue',command=restart)
q=Button(frame5,text="Exit",fg="black",font=("Courier", 8),bg="#90EE90",activebackground = 'sky blue',command=exit)


 

s_play()



root.mainloop()



