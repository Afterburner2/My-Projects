import random 
import pygame
import numpy as np
pygame.init()
win=pygame.display.set_mode((800,600))
x=350
y=566
x1=0
y1=0
width=50
height=50
player_alive=True
clock = pygame.time.Clock()

pygame.mixer.init()
s_started=False
def playdie():
    
    global y
    y += 30
    global s_started,player_alive
    s_started=True
    player_alive=False
    pygame.mixer.music.load("exp.wav")
    pygame.mixer.music.play(loops=0)


enemey_y=-1200 
enemey_2y=-800
enemey_3y=-500      
enemey_4y=-902     
enemey_5y=-1111      
xxx=0
yyy=0
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
class bulllet():
    
    def __init__(self,bx,by,xxx=0,yyy=0):
       # self.bx=bx
     #   self.by=by
        self.bx=bx
        self.by=by
     #   print('sss')
    
      #  self.hot_point_x=hot_point_x
      #  self.hot_point_y=hot_point_y
      #  self.xx=xx
      #  self.yy=yy
      #  self.x_way=x_way
     #   self.y_way=y_way
       # self.gox=gox
      #  self.goy=goy
    def move(self,gx,gy):
     #   global x_way,y_way
       # print('sssaa')
      #  shot=True
        hot_point_x=gx
        hot_point_y=gy
        x_way=np.linspace(self.bx,hot_point_x,50)
        y_way=np.linspace(self.by,hot_point_y,50)
        bulls=pygame.draw.rect(win,'blue',(x_way[xxx],y_way[yyy],5,5))
     #   print(x_way)
#bll=bulllet(x,y,m[0],m[1])
#bll.make
#def bullet(f):
  #  global hot_point_x,hot_point_y,xx,y,x_way,y_way,gox,goy,xxx,yyy
   # hot_point_x=f[0]
   # hot_point_y=f[1]
   # xx=x+10
   # yy=y+10
    #print(x_way)
 #   x_way=np.linspace(xx,hot_point_x,50)
  #  y_way=np.linspace(yy,hot_point_y,50)
   # xxx=0
   # yyy=0

   # print('x')
  #  print(f)


    
   # pygame.display.update()
shot=False 
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
    m=pygame.mouse.get_pos()
    
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
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        bll=bulllet(x,y)
        shot=True
    pl=pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    
    if shot ==True:
        if xxx<48:
            xxx+=1
            
        if yyy <48:
            yyy+=1
        else:
            shot=False
        bll.move(m[0],m[1])
    print(shot)
       
       # print(xxx)
 #   if pl.colliderect(a) or pl.colliderect(b) or pl.colliderect(c) or pl.colliderect(d) or pl.colliderect(e):
        
      #  player_alive=False
     #   if s_started ==False:
       # print('xxxxxxxxxxxxxxx')
     #   print('xx')
      #  playdie()
      #  else:
            #s_started==False
    pygame.display.update()

pygame.quit()
 