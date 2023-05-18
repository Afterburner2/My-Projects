from tkinter import *
import time
import threading
root=Tk()
def yilmaz():
    print('ret.')

    c3=Label(text="senin taşaklarını beton yetmez",fg='white',font=("times",34),bg='black')
    c3.pack()
    time.sleep(0.5)
    c3.destroy()
    time.sleep(0.5)
    threading.Thread(target=yilmaz).start()
    
root.geometry("800x600")
root.config(bg='black')
x=Label(text="İBRAHİM",fg='Red',font=("times",44),bg='black')
x.pack()
c=Label(text="YILMAZ",fg='yellow',font=("times",44),bg='black')
def but():
    s.destroy()
    threading.Thread(target=yilmaz).start()
c.pack()
s=Button(text='bas gardaaş',fg='white',font=("times",24),bg='black',command=but)
s.pack()


root.mainloop()