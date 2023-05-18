import random 
import pygame
import threading
pygame.init()
win=pygame.display.set_mode((800,600))
x=350
y=566
x1=0
y1=0
width=80
height=80
player_alive=True
clock = pygame.time.Clock()

pl_col='red'
pygame.mixer.init()
s_started=False
def playdie():
    global y,pl_col
    y += 30
    pl_col='black'
    global s_started,player_alive
    s_started=True
    player_alive=False
    pygame.mixer.music.load("expo3.wav")
    pygame.mixer.music.play(loops=0)


enemey_y=-1200 
enemey_2y=-800
enemey_3y=-500      
enemey_4y=-902     
enemey_5y=-1111      

def move(plc):
        global enemey_y,enemey_4y,enemey_3y,enemey_2y,enemey_5y,a,b,c,d,e
        if player_alive==True:
            enemey_y+=10
            enemey_2y+=10
            enemey_3y+=10
            enemey_4y+=10
            enemey_5y+=10

        a=pygame.draw.rect(win,'gold',(plc,enemey_y,30,30))
        b=pygame.draw.rect(win,'gold',(plc2,enemey_2y,30,30))
        c=pygame.draw.rect(win,'gold',(plc3,enemey_3y,30,30))
        d=pygame.draw.rect(win,'gold',(plc4,enemey_4y,30,30))
        e=pygame.draw.rect(win,'gold',(plc5,enemey_5y,30,30))


        pygame.display.update()
        
        
plc=random.randint(0,700)
plc2=random.randint(0,700)
plc3=random.randint(0,700)
plc4=random.randint(0,700)
plc5=random.randint(0,700)

run=True
while run:
   
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                run=False
    
    keys=pygame.key.get_pressed()

    if keys [pygame.K_LEFT] and x > 0:
        x1=-15
        x += x1
   
    if keys [pygame.K_RIGHT] and x< 700:
        x1=+15
        x += x1
         
    if keys [pygame.K_UP] and y > 0:
        y1=-15
        y += y1
    if keys [pygame.K_DOWN] and y< 500:
        y1=+15
        y += y1
    if enemey_y<600:
        move(plc)
        
    if player_alive==True:          
        if enemey_y>=600:
            plc=random.randint(0,700)
            enemey_y=-905
        if enemey_2y>=600:
            plc2=random.randint(0,700)
            enemey_2y=-623
        if enemey_3y>=600:
            plc3=random.randint(0,700)
            enemey_3y=-1800
        if enemey_4y>=600:
            plc4=random.randint(0,700)
            enemey_4y=-751
        if enemey_5y>=600:
            plc5=random.randint(0,700)
            enemey_5y=-148
    



    clock.tick(30)
    win.fill('black')
    pl=pygame.draw.rect(win,pl_col,(x,y,width,height))
    if pl.colliderect(a) or pl.colliderect(b) or pl.colliderect(c) or pl.colliderect(d) or pl.colliderect(e):
      #  player_alive=False
     #   if s_started ==False:
        print('xxxxxxxxxxxxxxx')
        print('xx')
        playdie()
      #  else:
            #s_started==False
    pygame.display.update()
    
pygame.quit()
 