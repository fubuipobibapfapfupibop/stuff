import pygame
from sys import argv
#essantial setup
pygame.init()
pygame.font.init()
path0 = argv[0]
path1 = len(path0.split('/')[-1])
path = path0[0:-path1]+"assets/"

#constants
RES = [600,750]
BGCOLOR = '#00203F'
TEXTCOLOR = '#AEEFD1'
FPS = 127
SCROLLLIMITN = -450
SCROLLLIMITP = 100

#variables
run = True
buttons = []
screen = pygame.display.set_mode(RES)
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
clock = pygame.time.Clock()
string = []
new_press = False
p_new_press = False
pos = 0
pos0 = 0
ppos = 0
end = 0
start = 0
calibri40 = pygame.font.SysFont("Calibri",40)
calibri30 = pygame.font.SysFont("Calibri",30)
mmt5 = False

#images
images = []
imagenames = ['plus','minus','times','over','pow','sqrt','root','logarithm','natural_logarithm','pi','e',
    'opening_bracket','closing_bracket','dot','comma','opening_curly_bracket','closing_curly_bracket','clear','backspace','equals','trig/sin',
    'trig/cos','trig/tan','trig/sec','trig/csc','trig/cot','trig/asin','trig/acos','trig/asec','trig/acsc','trig/acot',
    'trig/sinh','trig/cosh','trig/sech','trig/csch','trig/coth','trig/asinh','trig/acosh','trig/atanh','trig/asech',
    'trig/acsch','trig/acoth','cal/definite_integral','cal/integral','cal/summation','cal/product'
]
for i in range(10):
    images.append(pygame.image.load(f'{path}{i}.png').convert_alpha())
for imagename in imagenames:
    images.append(pygame.image.load(f'{path}{imagename}.png').convert_alpha())
functions = [str(i) for i in range(10)]
functions+= '+','-','*','/','**','sqrt','root','log','ln','pi','e','(',')','.',',','[',']','?CLS','?BCK','=','sin','cos','tan','sec','csc'
functions+='cot','asin','acos','asec','acsc','acot','sinh','cosh','tanh','sech','csch','coth','asinh','acosh','asech',
functions+='acsch','acoth','di','integral','sum','prod'
seperationMessages = ['Numbers:','Basic Math:','Calculator Specific:','Trigonometric functions:','Calculus:']
entryimg = pygame.image.load(f'{path}entry.png').convert_alpha()
#classes
class btn:
    def __init__(self,x_pos,y_pos,image,width,height):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = image
        self.width = width
        self.height = height

    def draw(self):
        screen.blit(self.image,[self.x_pos,self.y_pos])
    
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        button_rect = pygame.rect.Rect([self.x_pos,self.y_pos],[self.width,self.height])
        if button_rect.collidepoint(mouse_pos):
            return True
        else:
            return False

#functions
def makestring(n):
    global string
    string.append(n)
    if string[-1] == '=':
        string = ' '.join(string[0:(len(string)-1)])
        string = [str(eval(string))]
    elif string[-1] == '?CLS':
        string = []
    elif string[-1] == '?BCK':
        try:
            del string[-1]
            del string[-1]
        except:
            pass
    print(string)
 
def entry():
    global string
    string2 = ''.join(string)
    #display intersectiob rec
    rectrect = pygame.Rect([0,0],[600,145])
    pygame.draw.rect(screen,BGCOLOR,rectrect)
    #display entry image
    screen.blit(entryimg,[10,10])
    #display string
    renderedString = calibri40.render(string2,1,BGCOLOR)
    screen.blit(renderedString,[20,57])

def scroll(ypos,new_press,p_new_press,btnpress):
    stepsize = 75
    y2 = ypos+180
    x2 = 0
    sepcount = 0
    xcount = 0
    for i,image in enumerate(images):
        func = functions[i]
        if func == '0' or func == '+' or func == '(' or func == 'sin' or func == 'di':
            if functions[i] != '0':
                y2+=stepsize
            x2 = 0
            renderedString = calibri30.render(seperationMessages[sepcount],1,TEXTCOLOR)
            screen.blit(renderedString,[x2,y2])
            y2+=50
            sepcount+=1
            xcount = 0
        button = btn(x2,y2,image,64,64)
        button.draw()
        if button.check_click() and not new_press and p_new_press and btnpress:
            makestring(functions[i])
        if xcount == 7:
            y2+=stepsize
            x2 = 0
            xcount = 0
        else:
            x2+=stepsize
            xcount+=1


#main loop:
while run:
    screen.fill(BGCOLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('exiting...')
            run = False
    
    #main loop code
    #vars
    isLPressed = pygame.mouse.get_pressed()[0]
    cursorpos = pygame.mouse.get_pos()

    #update position
    if isLPressed:
        if start == -1:
            start = cursorpos[1]
            pdiff = 0
        end = cursorpos[1]
        #scroll
        difference = end-start
        pos0+=difference
        ddiff = difference-pdiff
        pos+=ddiff
        pdiff = difference
    else:
        start = -1
    
    #check if left mouse button has been released
    if isLPressed:
        new_press = True
    else:
        new_press = False
    if pos < SCROLLLIMITN:
        pos = SCROLLLIMITN
    elif pos > 0:
        pos = 0
    scroll(pos,new_press,p_new_press,mmt5)
    entry()
    #previous variables
    p_new_press = new_press
    mmt5 = start in range(end-5,end+5)
    #essential updating
    pygame.display.update()
    clock.tick(FPS)
#exit
pygame.display.quit()
pygame.quit()
print('exited')