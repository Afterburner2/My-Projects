from winsound import PlaySound
import pygame
from level_rect import *

pygame.init()
win=pygame.display.set_mode((800,600))

bg=pygame.image.load('Katman.png').convert_alpha()
plr=pygame.image.load('plr.png').convert_alpha()



level=1
bg_rec=bg.get_rect()
width=80
height=80

clock = pygame.time.Clock()
timer=True
plar=pygame.draw.rect(win,'red',(50,50,30,30))
win.blit(plr,(50,50))
def count3():

    global timer
    pygame.time.delay(1000)
    print('1')
    pygame.time.delay(1000)
    print('2')
    pygame.time.delay(1000)
    print('3')
    timer=False
    track1()
def draw():
    global run
    win.blit(bg,(0,0))
    plar=pygame.draw.rect(win,'red',(mouse_pos[0]-15,mouse_pos[1]-15,30,30))
    win.blit(plr,(mouse_pos[0]-15,mouse_pos[1]-15))
   

    for i in rectlist:
        if i.colliderect(plar):
            print('yes')
           # run=False
  #  if plar.colliderect(rect4):
    #    print('yee')
    else:
        print('no')
    

    pygame.display.update()
    win.fill('white')
run=True
while run:
    mouse_pos=pygame.mouse.get_pos()
    
    draw()
    
    pygame.time.delay(100)
    if timer==True:
        count3()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                run=False
    
    
    clock.tick(30)

    
pygame.quit()
 