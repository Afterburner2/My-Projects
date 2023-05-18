from tkinter import *
import time
import random
import colorama
from colorama  import Fore,Back,Style
import threading

root=Tk()
colorama.init()

print (Fore.RED)
print("deneme")

#root.attributes('-fullscreen', True)
root.geometry("100x100")

renkler=['black','blue','aqua',"#f4a460","#006400"]

def rgp():
    for i in range(100):
                x=random.choice(renkler)
                root.config(bg=x)
                time.sleep(0.6)
    print('basarili' )

                    
    print (Fore.BLUE)
    print('basarili' )
    print (Fore.RED)
                

threading.Thread(target=rgp).start()
    
root.mainloop()
