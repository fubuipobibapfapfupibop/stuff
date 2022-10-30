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
velocity = 2*(1/fps)
difficulty = fps
shotspeed = 600*(1/fps)
py = pos.y
direction = 0
screencenter = [screendimensions[0]/2,screendimensions[1]/2]
rl = False
rr = False
shots = []
enemies = []
WHITE = [255,255,255]
count = 0
def drawshots():
    #[progress,x1,y1,ll]
    global shots
    for i in range(len(shots)):
        try:
            item = shots[i]
            ll = shots[i][3]
            shots[i][3] += shotspeed
            shots[i][1] = sc.x-(numpy.cos(item[0])*(ll))
            shots[i][2] = sc.y-(numpy.sin(item[0])*(ll))
            x = item[1]
            y = item[2]
            pygame.draw.circle(screen,WHITE,[x,y],10)
            if x < 0 or y < 0 or x > screendimensions[0] or y > screendimensions[1]:
                del shots[i]
        except Exception as e:
            print(e)

def drawenemies():
    global difficulty
    global count
    global enemies
    try:
        if count == round(difficulty):
            randypos = random.randint(-35,435)
            enemies.append([-20,randypos])
            count = 0
        for item in enemies:
            pygame.draw.circle(screen,WHITE,item,50)
    except:
        pass
    #check collision
    enemydeleltelist = []
    for a in range(len(enemies)):
        enemy = enemies[a]
        enemyxpos = -20
        enemyypos = enemy[1]
        for b in range(len(shots)):
            shot = shots[b]
            shotxpos = abs(shot[1])
            shotypos = abs(shot[2])
            xdifference = shotxpos-enemyxpos
            ydifference = shotypos-enemyypos
            difference = numpy.sqrt(xdifference**2+(ydifference**2))
            if difference < 60:
                enemydeleltelist.append(a)
    print(len(enemies))
    enemydeleltelist.sort()
    enemydeleltelist.reverse()
    for i in range(len(enemydeleltelist)):
        item = enemydeleltelist[i]
        del enemies[int(item)]
    count+=1
    difficulty-= 5*(1/fps)
    difficulty = abs(difficulty)
    if round(difficulty) == 0:
        difficulty = 5
    print(difficulty)
    
    
            


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
                shots.append([progress,pos.x,pos.y,linelength])
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
