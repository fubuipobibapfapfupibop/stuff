import pygame

start = -1000
end = 1000
fps = 100

screendimensions = [800,400]
scx = screendimensions[0]/2
scy = screendimensions[1]/2
screen = pygame.display.set_mode(screendimensions)
clock = pygame.time.Clock()

def graph_function(x):
    return x**2

def make_graph_array(start,end):
    #make array
    array = []
    while start<end:
        res = graph_function(start)
        array.append(scy-res)
        start+=1
    #make array in couiples of two numbers
    final_array = []
    couple_to_append = []
    count = 0
    for i in range(len(array)):
        item = array[i]
        print(item)
        if count ==2:
            count = 0
            final_array.append(couple_to_append)
            couple_to_append = []
        else:
            couple_to_append.append(item)
            count+=1
    print(final_array)
    return final_array




def display_graph_array(array):
    print(array)
    for i in range(len(array)):
        item = array[i]
        try:
            item2 = array[i+1]
        except Exception:
            pass
        print(item)
        pygame.draw.line(screen,[40,40,255],item,item2,1)
        i+=1
    while True:
        pygame.display.update()
        clock.tick(fps)


array = make_graph_array(start,end)
display_graph_array(array)
