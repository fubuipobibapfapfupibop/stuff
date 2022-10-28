import pygame
import numpy
import random
pygame.init()

fps = 127
screendimensions = [800,400]
linelength = 50

screen = pygame.display.set_mode(screendimensions)
stopmainloop = False
clock = pygame.time.Clock()
class screencenter:
    pass
class positions:
    pass
sc = screencenter()
sc.x = screendimensions[0]/2
sc.y = screendimensions[1]/2
pos = positions()
pos.x = sc.x-(numpy.cos(0)*linelength)
pos.y = sc.y-(numpy.sin(0)*linelength)
progress = numpy.arccos(-1)*linelength
velocity = 3.5*(1/fps)
shotspeed = 600*(1/fps)
py = pos.y
direction = 0
screencenter = [screendimensions[0]/2,screendimensions[1]/2]
rl = False
rr = False
shots = []
enemies = []
WHITE = [255,255,255]
def drawshots():
    #[progress,x1,y1,x2,y2,linelength]
    global shots
    for i in range(len(shots)):
        try:
            item = shots[i]
            shots[i][5] += shotspeed
            ll = shots[i][5]
            shots[i][1] = sc.x-(numpy.cos(item[0])*(ll))
            shots[i][2] = sc.y-(numpy.sin(item[0])*(ll))
            shots[i][3] = sc.x-(numpy.cos(item[0])*(ll+50))
            shots[i][4] = sc.y-(numpy.sin(item[0])*(ll+50))
            x = item[1]
            y = item[2]
            x2 = item[3]
            y2 = item[4]
            pygame.draw.aaline(screen,WHITE,[x,y],[x2,y2],True)
            if x < 0 or y < 0 or x > screendimensions[0] or y > screendimensions[1]:
                del shots[i]
        except Exception as e:
            print(e)

def drawenemies():
    randlist = [[[-100,-100],[900,-100]],[[-100,-100],[-100,500]],[[-100,500],[900,500]],[[900,500],[900,-100]]]
    rand1 = random.randint(0,3)
    randenemyposx = random.randint(randlist[rand1][0][0],randlist[rand1][1][0])
    print(f'x: {randenemyposx}')
    randenemyposy = random.randint(randlist[rand1][0][1],randlist[rand1][1][1])
    print(f'x: {randenemyposx}  y: {randenemyposy}')

def checkhitbox():
    global enemies
    for item in enemies:
        pass

def rotate(direction,rotation):
    #direction can be r or l
    if rotation:
        global progress
        global velocity
        global pos
        global py
        if direction == 'r':
            if velocity > 0:
                velocity = -velocity
        else:
            velocity = abs(velocity)
        progress -= velocity
        pos.x = sc.x-(numpy.cos(progress)*linelength)
        pos.y = sc.y-(numpy.sin(progress)*linelength)
    pygame.draw.aaline(screen,WHITE,[pos.x,pos.y],[sc.x,sc.y],True)

while not stopmainloop:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('exiting...')
            stopmainloop = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rl = True
            elif event.key == pygame.K_RIGHT:
                rr = True
            elif event.key == pygame.K_SPACE:
                shots.append([progress,pos.x,pos.y,0,0,linelength])
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                rl = False
            elif event.key == pygame.K_RIGHT:
                rr = False
    screen.fill([0,0,0])
    if rl == True:
        rotate('l',True)
    elif rr == True:
        rotate('r',True)
    rotate(None,False)
    drawshots()
    drawenemies()
    #update values
    #update display
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
print('exited!')