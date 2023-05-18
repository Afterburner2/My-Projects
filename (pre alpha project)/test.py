import random 
import pygame
pygame.init()
WIDTH=1000

win=pygame.display.set_mode((WIDTH,680))
pygame.display.set_caption("Escape")
x=350
y=566
x1=0
y1=0
width=50
height=50
player_alive=True
score=0
clock = pygame.time.Clock()
pygame.font.init()

pygame.mixer.init()
s_started=False
def playdie():
    global y,x
    global s_started,player_alive
    s_started=True
    player_alive=False
    pygame.mixer.music.load("exp.wav")
    pygame.mixer.music.play(loops=0)

vel=10
enemey_y=-1200 
enemey_2y=-800
enemey_3y=-500      
enemey_4y=-902     
enemey_5y=-1111      

def move(plc):
        global enemey_y,enemey_4y,enemey_3y,enemey_2y,enemey_5y,a,b,c,d,e,score,vel
        if player_alive==True:
            enemey_y+=vel
            enemey_2y+=vel
            enemey_3y+=vel
            enemey_4y+=vel
            enemey_5y+=vel
            score+=0.1
            vel+=0.005
        a=pygame.draw.rect(win,'gold',(plc,enemey_y,30,30))
        b=pygame.draw.rect(win,'gold',(plc2,enemey_2y,30,30))
        c=pygame.draw.rect(win,'gold',(plc3,enemey_3y,30,30))
        d=pygame.draw.rect(win,'gold',(plc4,enemey_4y,30,30))
        e=pygame.draw.rect(win,'gold',(plc5,enemey_5y,30,30))
        

        pygame.display.update()
        
main_font=pygame.font.SysFont("conicsans",50)       
plc=random.randint(0,1000)
plc2=random.randint(0,1000)
plc3=random.randint(0,1000)
plc4=random.randint(0,1000)
plc5=random.randint(0,1000)

run=True
while run:
   
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                run=False
    
    keys=pygame.key.get_pressed()

    if keys [pygame.K_LEFT] and x > 0:
        x1=-15
        x += x1
    if keys [pygame.K_RIGHT] and x< 970:
        x1=+15
        x += x1
    if keys [pygame.K_UP] and y > 0:
        y1=-15
        y += y1
    if keys [pygame.K_DOWN] and y< 670:
        y1=+15
        y += y1
    if enemey_y<600:
        move(plc)
    lives_label=main_font.render (f"Score: {int(score)}",1,'green')
    level_label=main_font.render(f"Speed: {int(vel)}",1,'green')

  #  win.blit(lives_label,(10,10))
  #  win.blit(level_label,(WIDTH-level_label.get_width()-10,10))
        
    if player_alive==True:          
        if enemey_y>=600:
            plc=random.randint(0,1000)
            enemey_y=-905
        if enemey_2y>=600:
            plc2=random.randint(0,1000)
            enemey_2y=-623
        if enemey_3y>=600:
            plc3=random.randint(0,1000)
            enemey_3y=-1800
        if enemey_4y>=600:
            plc4=random.randint(0,1000)
            enemey_4y=-751
        if enemey_5y>=600:
            plc5=random.randint(0,1000)
            enemey_5y=-148
    
    clock.tick(30)
    win.fill('black')
    pl=pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    if pl.colliderect(a):
        if enemey_y<y:
            y += 30
        else:
            if plc<x:
                x+=30
            else:
                x-=30
        playdie()
    elif pl.colliderect(b):
        if enemey_2y<y:
            y += 30
        else:
            if plc2<x:
                x+=30
            else:
                x-=30
        playdie()
    elif pl.colliderect(c):
        if enemey_3y<y:
            y += 30
        else:
            if plc3<x:
                x+=30
            else:
                x-=30
        playdie()
    elif pl.colliderect(d):
        if enemey_4y<y:
            y += 30
        else:
            if plc4<x:
                x+=30
            else:
                x-=30
        playdie()
    elif pl.colliderect(e):
        if enemey_5y<y:
            y += 30
        else:
            if plc5<x:
                x+=30
            else:
                x-=30
        playdie()
    win.blit(level_label,(WIDTH-level_label.get_width()-10,10))
    win.blit(lives_label,(10,10))
    pygame.display.update()
    
pygame.quit()
 