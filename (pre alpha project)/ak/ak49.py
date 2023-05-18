import pygame
import random

pygame.init()

width=800
height=600

plx=width//2
ply=height//2


win=pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
lazers=[]
class ak():
    def __init__(self,player_x,player_y,player_w,player_h,x,y) :
        self.player_x=player_x
        self.player_y=player_y
        self.player_w=player_w
        self.player_h=player_h
        self.x=x
        self.y=y
    def draw(self,win):
        apl=pygame.draw.rect(win,'red',(self.player_x-self.player_w//2,self.player_y-self.player_h//2,
        self.player_w,self.player_h))
    def laser(self,win):
        for i in lazers:
            laz=pygame.draw.rect(win,'blue',(self.x-5,self.y+250,10,10))
        self.y-=1
        print(lazers)




class Laser:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw(self,win):
        alz=pygame.draw.rect(win,'blue',(self.x-5,self.y-5,10,10))
    def move(self,vel,dir):
        print(dir)
        if dir=='Y':
            self.y +=vel
        if dir=='X':
            self.x  +=vel

ak1=ak(plx,ply,50,50,plx,ply)
#laser=Laser(plx,ply)



run=True

def draw_win(): 
        pygame.display.update()
        ak1.draw(win)
        ak1.laser(win)
    #    laser.draw(win)
      
        pygame.display.update()
def movee():
        pygame.display.update()
vel=0
while run:
    draw_win()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    clock.tick(30)
    win.fill('black')
    
    keys=pygame.key.get_pressed()
    if keys [pygame.K_UP]:
        vel=-5
        dir='Y'
    if keys [pygame.K_DOWN]:
        vel=5
        dir='Y'
    if keys [pygame.K_LEFT]:
        vel=-5
        dir='X'
    if keys [pygame.K_RIGHT]:
        vel=5
        dir='X'
    if keys [pygame.K_w]:
        lazers.append(1)
        ak1.laser(win)
       # laser=Laser(plx,ply)
       # laser.move(vel,dir)
    



pygame.quit()
